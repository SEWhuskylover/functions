def calc_gst(net_price):
    return net_price * 1.15


#main
net_price_ = float(input("enter number \n"))
print(f"${calc_gst(net_price_):.2f}")
