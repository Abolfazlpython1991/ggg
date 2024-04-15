from rubpy import Client, handlers, Message
from asyncio import run 
import json , requests , os
from re import search
save_path = "Photo.jpg"
save_pathe = "voice.ogg"
print("Bot Is On")
async def main():
    async with Client(session='bot') as client:
        @client.on(handlers.MessageUpdates())
        async def updates(message: Message):
            object_guid = message.object_guid
            msg = message.message_id
            print(object_guid)
            admin = await client.get_group_admin_members(object_guid)
            admin = [i.member_guid for i in admin.in_chat_members]
            if message.raw_text is not None and message.raw_text.startswith("/Photo:"):
                try:
                    first_name = "♡ HELLO, PLEASE BE PATIENT ♡"
                    textGpt = message.raw_text.split(":")[-1]
                    eg = await message.reply(f"[{first_name}]({message.author_guid})\n____________________________________________\n[ 🍭 ] - کاربر گرامی لطفاً منتظر باشید .\n[ 🥢 ] - نوبت سوالتون : [ 1 ]\n[ ✅ ] - سوال های پاسخ داده شده : [ 1 ]")
                    jd = eg['message_update']['message_id']
                    await client.delete_messages(object_guid=object_guid,message_ids=jd)
                    jd = json.loads(requests.get(f"https://api.irateam.ir/Image/test.php?text={textGpt}").text)
                    result = jd["result"]
                    first_link = result[0]
                    response = requests.get(first_link)
                    response.raise_for_status()
                    with open(save_path, 'wb') as file:
                        file.write(response.content)
                    await client.send_photo("g0ChCjw034fd201dbcad5d4c252603b3",save_path,caption=f"**عکس شما اماده شد.❗**\n\n**موضوع : {textGpt}**\n\n❗ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕄𝕖 : @Id_Recod",reply_to_message_id=msg)
                except Exception as e:
                    # چاپ اطلاعات مربوط به ارور
                    print(f"An error occurred: {str(e)}")
            if message.raw_text is not None and message.raw_text.startswith("/Voice:"):
                textGpte = message.raw_text.split(":")[-1]
                try:
                    first_name = "♡ HELLO, PLEASE BE PATIENT ♡"
                    eggg = await message.reply(f"[{first_name}]({message.author_guid})\n____________________________________________\n[ 🍭 ] - کاربر گرامی لطفاً منتظر باشید .\n[ 🥢 ] - نوبت سوالتون : [ 1 ]\n[ ✅ ] - سوال های پاسخ داده شده : [ 1 ]")
                    jd = eggg['message_update']['message_id']
                    await client.delete_messages(object_guid=object_guid,message_ids=jd)
                    jd = json.loads(requests.get(f"https://haji-api.ir/text-to-voice/?text={textGpte}&Character=FaridNeural").text)
                    result = jd["results"]["url"]
                    response = requests.get(result)
                    with open("Voice.mp3", "wb") as f:
                        f.write(response.content)
                    music_bytes = response.content
                    reg = await client.send_music(
    object_guid=object_guid,
    music=music_bytes,
    caption=f"**ویس شما اماده شد.❗**\n\n**موضوع : {textGpte}**\n\n❗ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕄𝕖 : @Id_Recod",
    file_name="𝕐𝕠𝕦𝕣𝕍𝕠𝕚𝕔𝕖",
    performer="ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕄𝕖:@ℂ𝕠𝕕𝕖ℝ𝕦𝕓𝕚𝕜𝕒",
    reply_to_message_id=msg
)
                    os.remove("Voice.mp3")
                except Exception as e:
                    print(f"خطا در ارسال ویس: {e}")
            elif message.raw_text is not None and message.raw_text.startswith("/voice:"):
                textGpte = message.raw_text.split(":")[-1]
                try:
                    first_name = "♡ HELLO, PLEASE BE PATIENT ♡"
                    eggg = await message.reply(f"[{first_name}]({message.author_guid})\n____________________________________________\n[ 🍭 ] - کاربر گرامی لطفاً منتظر باشید .\n[ 🥢 ] - نوبت سوالتون : [ 1 ]\n[ ✅ ] - سوال های پاسخ داده شده : [ 1 ]")
                    jd = eggg['message_update']['message_id']
                    await client.delete_messages(object_guid=object_guid,message_ids=jd)
                    jd = json.loads(requests.get(f"https://haji-api.ir/text-to-voice/?text={textGpte}&Character=DilaraNeural").text)
                    result = jd["results"]["url"]
                    response = requests.get(result)
                    with open("Voice.mp3", "wb") as f:
                        f.write(response.content)
                    music_bytes = response.content
                    reg = await client.send_music(
    object_guid=object_guid,
    music=music_bytes,
    caption=f"**ویس شما اماده شد.❗**\n\n**موضوع : {textGpte}**\n\n❗ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕄𝕖 : @Id_Recod",
    file_name="𝕐𝕠𝕦𝕣𝕍𝕠𝕚𝕔𝕖",
    performer="ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕄𝕖:@ℂ𝕠𝕕𝕖ℝ𝕦𝕓𝕚𝕜𝕒",
    reply_to_message_id=msg
)
                    os.remove("Voice.mp3")
                except Exception as e:
                    print(f"خطا در ارسال ویس: {e}")
            elif message.raw_text is not None and message.raw_text.startswith("//"):
                textGptetg = message.raw_text.split("//")[-1]
                first_name = "♡ HELLO, PLEASE BE PATIENT ♡"
                eggggg = await message.reply(f"[{first_name}]({message.author_guid})\n____________________________________________\n[ 🍭 ] - کاربر گرامی لطفاً منتظر باشید .\n[ 🥢 ] - نوبت سوالتون : [ 1 ]\n[ ✅ ] - سوال های پاسخ داده شده : [ 1 ]")
                jd = eggggg['message_update']['message_id']
                await client.delete_messages(object_guid=object_guid,message_ids=jd)
                jd = json.loads(requests.get(f"https://api2.haji-api.ir/gpt/gpt.php?text={textGptetg}").text)
                resultg = jd["result"]["answer"]
                await message.reply(resultg)
            if message.raw_text is not None and not message.author_guid in admin and (search("https:", message.raw_text) or search("@", message.raw_text)):
                    reg = await message.delete_messages()
                    reg = await client.send_message(object_guid,"کاربر عزیز ارسال لینک در این گروه ممنوع میباشد.❗")
                    dell = reg['message_update']['message_id']
                    await client.delete_messages(object_guid,message_ids=dell)
            if not message.author_guid in admin and 'forwarded_from' in message.to_dict().get('message').keys():
                reg = await message.delete_messages()
                reg = await client.send_message(object_guid,"کاربر عزیز ارسال فوروارد در این گروه ممنوع میباشد.❗")
                dell = reg['message_update']['message_id']
                await client.delete_messages(object_guid,message_ids=dell)
        await client.run_until_disconnected()
run(main())