import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('800x800')

v = [
    'Bank',
    'Blackfriars',
    'Cannon Street',
    'Chancery Lane',
    'Charing Cross',
    'Covent Garden',
    'Embankment',
    'Goodge Street',
    'Holborn',
    'Leicester Square',
    'London Bridge',
    'Mansion House',
    "St Paul's",
    'Temple',
    'Tottenham Court Road',
]


menu1 = ttk.Combobox(root, values=v)
menu1.place(relx=0.55, rely=0.35, relheight=0.07, relwidth=0.3)

menu2 = ttk.Combobox(root, values=v)
menu2.place(relx=0.55, rely=0.55, relheight=0.07, relwidth=0.3)

start = menu1.get()
stop = menu2.get()
inf = float("inf")

graph = {}

graph["Bank"]["London Bridge"] = 1
graph["Bank"]["St Paul's"] = 1

graph["Blackfriars"] = {}
graph["Blackfriars"]["Mansion House"] = 1
graph["Blackfriars"]["Temple"] = 1

graph["Cannon Street"] = {}
graph["Cannon Street"]["Mansion House"] = 1
graph["Cannon Street"]["Monument"] = 1

graph["Chancery Lane"] = {}
graph["Chancery Lane"]["Holborn"] = 1
graph["Chancery Lane"]["St Paul's"] = 1


graph["Charing Cross"] = {}
graph["Charing Cross"]["Embankment"] = 1
graph["Charing Cross"]["Temple"] = 1

graph["Covent Garden"] = {}
graph["Covent Garden"]["Holborn"] = 2
graph["Covent Garden"]["Leicester Square"] = 1

graph["Embankment"] = {}
graph["Embankment"]["Charing Cross"] = 1
graph["Embankment"]["Temple"] = 1

graph["Goodge Street"] = {}
graph["Goodge Street"]["Tottenham Court Road"] = 1

graph["Holborn"] = {}
graph["Holborn"]["Chancery Lane"] = 1
graph["Holborn"]["Covent Garden"] = 2
graph["Holborn"]["Tottenham Court Road"] = 1

graph["Leicester Square"] = {}
graph["Leicester Square"]["Chancery Lane"] = 1
graph["Leicester Square"]["Covent Garden"] = 1
graph["Leicester Square"]["Tottenham Court Road"] = 1

graph["London Bridge"] = {}
graph["London Bridge"]["Bank"] = 1

graph["Mansion House"] = {}
graph["Mansion House"]["Blackfriars"] = 1
graph["Mansion House"]["Cannon Street"] = 1

graph["Monument"] = {}
graph["Monument"]["Cannon Street"] = 1

graph["St Paul's"] = {}
graph["St Paul's"]["Chancery Lane"] = 1
graph["St Paul's"]["Bank"] = 1

graph["Temple"] = {}
graph["Temple"]["Blackfriars"] = 1
graph["Temple"]["Embankment"] = 1

graph["Tottenham Court Road"] = {}
graph["Tottenham Court Road"]["Goodge Street"] = 1
graph["Tottenham Court Road"]["Leicester Square"] = 1
graph["Tottenham Court Road"]["Holborn"] = 1

costs = {}
parents = {}
for node in graph:
    costs[node] = inf
    parents[node] = {}

costs[start] = 0


def run_algorithm():
    def find_cheapest_node(costs, not_checked):
        cheapest_node = None
        lowest_cost = inf
        for node in not_checked:
            if costs[node] <= lowest_cost:
                lowest_cost = costs[node]
                cheapest_node = node
        return cheapest_node

    if __name__ == "__main__":
        not_checked = [node for node in costs]
        node = find_cheapest_node(costs, not_checked)
        while not_checked:
            if '' in graph:
                continue
            print(f"Not checked: {not_checked}")
            cost = costs[node]
            child_cost = graph[node]
            for c in child_cost:
                if costs[c] > cost + child_cost[c]:
                    costs[c] = cost + child_cost[c]
                    parents[c] = node

            not_checked.pop(not_checked.index(node))
            node = find_cheapest_node(costs, not_checked)

        print(f"Costs: {costs}")
        print(f"The costs to go from {start} to {stop} is {costs[stop]}!")

        if costs[stop] < inf:
            path = [stop]
            i = 0
            while start not in path:
                path.append(parents[path[i]])
                i += 1

            print(f"The shortest path is {path[::-1]}")
        else:
            print("A path could not be found")

    print('route found')


canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

frame = tk.Frame(root, bg='#FFEFD5')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

frame1 = tk.Frame(frame, bg='#00CED1', bd=10)
frame1.place(relwidth=0.9, relheight=0.15, relx=0.05, rely=0.3)

frame2 = tk.Frame(frame, bg='#00CED1', bd=10)
frame2.place(relwidth=0.9, relheight=0.15, relx=0.05, rely=0.5)

label = tk.Label(frame1, text='Select Starting Point', font=40)
label.place(relx=0, rely=0, relheight=1, relwidth=0.4)

label2 = tk.Label(frame2, text='Select Finishing Point', font=40)
label2.place(relx=0, rely=0, relheight=1, relwidth=0.4)

label3 = tk.Label(frame, text='Plan a Zone 1 Journey', font=40)
label3.place(relx=0.2, rely=0.1, relheight=0.1, relwidth=0.6)

menu1 = ttk.Combobox(root, values=v)
menu1.place(relx=0.55, rely=0.35, relheight=0.07, relwidth=0.3)

menu2 = ttk.Combobox(root, values=v)
menu2.place(relx=0.55, rely=0.55, relheight=0.07, relwidth=0.3)

button = tk.Button(frame, text='Go!', bg='#00CED1', command=run_algorithm)
button.place(relx=0.35, rely=0.8, relheight=0.07, relwidth=0.3)

root.mainloop()
