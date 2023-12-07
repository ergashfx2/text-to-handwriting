from filters.admins import AdminFilter
from loader import bot, dp
from utils.db_api.sqlite import db


def block_user(cid, is_blocked):
    db.update_user_block(is_blocked, cid)


def get_user_data(cid):
    return db.select_user(cid=cid)


def create_user(cid, full_name, font, rang):
    block_user(cid, 0)
    if not get_user_data(cid):
        db.add_user(cid, full_name, font, rang)


async def fmessage(i, cid, mid, rm, count_group, blocked):
    try:
        await bot.copy_message(i, cid, mid, reply_markup=rm)
        count_group += 1
        print('ID si ' + str(i) + " bo'lgan userga yuborildi!")
    except Exception as exception:
        if "was blocked" in str(exception) or "deactivated" in str(exception) or "chat not found" in str(exception):
            block_user(i, 1)
            blocked += 1
        print(str(i) + " ------ ga bormadi!!!! \n" + str(exception))

    return count_group, blocked


@dp.message_handler(AdminFilter(), commands=['send'], state="*")
async def message_send(m):
    cid = m.from_user.id
    if m.reply_to_message:
        count_group = 0
        blocked = 0
        await bot.send_message(cid, "<b>Boshlandi!</b>", parse_mode="HTML")
        leng = db.select_users_all_ids()

        mid = m.reply_to_message.message_id
        rm = m.reply_to_message.reply_markup

        for u in leng:
            a = await fmessage(u[0], cid, mid, rm, count_group, blocked)
            count_group, blocked = a
        await bot.send_message(cid,
                               f"*Hammaga sms bordi!*\n\n{count_group} ta userga bordi\n{blocked} ta userga bormadi",
                               parse_mode="Markdown")


@dp.message_handler(AdminFilter(), commands=['stat'], state="*")
async def handler_users(m):
    try:
        cid = m.from_user.id
        all_users = db.count_users()[0]
        faol_users = db.count_active_users()[0]

        stat_text = f"""<b>
📊┌ STATISTIKA
👥├ A`zolar: {all_users}
👥├ Faol a'zolar: {faol_users}
</b>"""
        await bot.send_message(cid, stat_text, parse_mode="HTML")
    except Exception as exception:
        print("command_ss error: " + str(exception))
