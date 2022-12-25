from machine import create_machine

machine=create_machine()
with open('C:\\Users\\f74091310\\OneDrive\\圖片\\linebot_source\\fsm.png','bw') as f:
    machine.get_graph().draw(f, prog="dot", format="png")
print("done")