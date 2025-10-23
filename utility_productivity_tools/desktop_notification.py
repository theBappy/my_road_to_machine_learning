
from win10toast import ToastNotifier

n = ToastNotifier()

n.show_toast(
    "Notification",
    "Here comes notification boyd",
    duration=20,
    icon_path="utility_productivity_tools\\logo.ico"
)
