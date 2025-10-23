import speedtest

st = speedtest.Speedtest()

st.get_best_server()

download_speed = st.download() / 1_000_000
upload_speed = st.download() / 1_000_000
ping = st.results.ping

print(f"Download speed: {download_speed:.2f} Mbps")
print(f"Upload speed: {upload_speed:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")