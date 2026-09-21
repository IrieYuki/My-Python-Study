def progress_bar(sleep_time, print_message):
    from time import sleep

    for i in range(101):
        sleep(sleep_time)
        print(f"\r进度条: [{'#' * (i)}{' ' * (100 - i)}], {i}%", end="")

    print("\n", print_message)


if __name__ == "__main__":
    try:
        progress_bar(0.05, "进度条完成！")
    except Exception as e:
        print("\n进度条被中断！")
