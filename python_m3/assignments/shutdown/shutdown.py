def shutdown(seconds):
    if seconds == 0:
        print("Shutting down now")
    else:
        print("Shutting down in", seconds)
        shutdown(seconds - 1)

shutdown(5)
