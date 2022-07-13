from tkinter import*
import random
root=Tk()
root.geometry("400x400")
root.title("Sales profit application")
month = ("jan","feb","march","april","may","june","july","AUGUST","sep","oct","nov","dec")
profit=(14000, 23000, 50020, 43204, 49230, 42904, 84023, 99999, 10000, 93042, 93042, 14320)
maximum_profit=max(profit)
print(maximum_profit)
minimum_profit=min(profit)
print(minimum_profit)
maximum_index=profit.index(maximum_profit)
print(maximum_index)
print(month[maximum_index])

minimum_index=profit.index(minimum_profit)
print(minimum_index)
print(month[minimum_index])

print("the minimum profit is achieved in the month of",month[minimum_index],"THE PROFIT AMOUNT ACHIEVED IS",str(minimum_profit))

print("the maximum profit is achieved in the month of",month[maximum_index],"THE PROFIT AMOUNT ACHIEVED IS",str(maximum_profit))


label1=Label(root,text="")
label1.place(relx=0.5, rely=0.6, anchor=CENTER)

label2=Label(root,text="")
label2.place(relx=0.5, rely=0.5, anchor=CENTER)


def min_PROFIT():
    label1["text"]="the minimum profit is achieved in the month of",month[minimum_index],"THE PROFIT AMOUNT ACHIEVED IS",str(minimum_profit)
def max_PROFIT():
    label2["text"]="the maximum profit is achieved in the month of",month[maximum_index],"THE PROFIT AMOUNT ACHIEVED IS",str(maximum_profit)



button1=Button(root,text="the minimum profit is",command=min_PROFIT)
button1.place(relx=0.5, rely=0.8, anchor=CENTER)


button2=Button(root,text="the maximum profit is",command=max_PROFIT)
button2.place(relx=0.5, rely=0.7, anchor=CENTER)
















root.mainloop()