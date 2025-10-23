import speedtest


def speed_tester():
    st = speedtest.Speedtest()

    print("Loading server list...\n")
    st.get_servers()
    print("Choosing best server...")
    best = st.get_best_server()
    print(f"Found: {best['host']} located in {best['country']}")

    option = int(
        input(
            """What speed do you want to test:  
    
    1) Download Speed  
    
    2) Upload Speed  
    
    3) Ping 
    
    Your Choice: """
        )
    )

    if option == 1:
        print("Performing download speed test...")
        download_speed = st.download()
        print(f"Download speed: {download_speed/1024/1024:.2f} Mbit/s")
    elif option == 2:
        print("Performing upload speed test...")
        upload_speed = st.upload()
        print(f"Upload speed: {upload_speed/1024/1024:.2f} Mbit/s")
    elif option == 3:
        ping_speed = st.results.ping
        print(f"Ping: {ping_speed}ms")
    else:
        print("Please enter the correct choice!")

if __name__ == "__main__":
    speed_tester()