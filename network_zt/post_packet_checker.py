import pyshark

capture = pyshark.FileCapture(
    "capture.pcapng",
    display_filter="dns"
)

for packet in capture:
    print(packet)