import logging

from speedtest import Speedtest

from telegram import ParseMode



logger = logging.getLogger(__name__)


def speedtest():
    st = Speedtest()
    st.get_best_server()
    st.download()
    st.upload()
    st.results.share()
    result = st.results.dict()
    return result


def speed_convert(size):
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "MB/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


def speedtest_fun(update, context):
    message = update.effective_message
    del_msg = message.reply_text("Running Speed Test . . . ")

    result = speedtest()

    logger.info(f"Server; Name:- {result['server']['name']}, Country:- {result['server']['country']} ({result['server']['cc']}), Sponsor:- {result['server']['sponsor']}, Latency:- {result['server']['latency']}.")
    logger.info(f"SpeedTest Results; Upload:- {speed_convert(result['upload'] / 8)}, Download:- {speed_convert(result['download'] / 8)}, Ping:- {result['ping']} ms, ISP:- {result['client']['isp']}.")

    path = (result['share'])
    string_result = f'''
<b>Server</b>
<b>Name:</b> <code>{result['server']['name']}</code>
<b>Country:</b> <code>{result['server']['country']}, {result['server']['cc']}</code>
<b>Sponsor:</b> <code>{result['server']['sponsor']}</code>
<b>Latency:</b> <code>{result['server']['latency']}</code>

<b>SpeedTest Results</b>
<b>Upload:</b> <code>{speed_convert(result['upload'] / 8)}</code>
<b>Download:</b>  <code>{speed_convert(result['download'] / 8)}</code>
<b>Ping:</b> <code>{result['ping']} ms</code>
<b>ISP:</b> <code>{result['client']['isp']}</code>
'''

    del_msg.delete()
    try:
        message.reply_photo(path, string_result, parse_mode=ParseMode.HTML)
    except:
        message.reply_text(string_result, parse_mode=ParseMode.HTML)



