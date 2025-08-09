import speedtest
st = speedtest.Speedtest()
print("🔄 Testing... Please wait.\n")
st.get_best_server()
download_speed = st.download()
upload_speed = st.upload()
ping = st.results.ping

download_mbps = download_speed / 1_000_000
upload_mbps = upload_speed / 1_000_000

print("🌐 Internet Speed Test Results:")
print(f"📶 Ping        : {ping:.2f} ms")
print(f"⬇️ Download    : {download_mbps:.2f} Mbps")
print(f"⬆️ Upload      : {upload_mbps:.2f} Mbps")
