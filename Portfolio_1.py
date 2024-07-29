import tkinter as tk

root = tk.Tk()
root.title('Планировщик')
root.configure(background='bisque')

def add_task():
    task = entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def mark_done():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks_listbox.get(selected_task_index)
        done_listbox.insert(tk.END, task)
        tasks_listbox.delete(selected_task_index)

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        selected_done_task_index = done_listbox.curselection()
        if selected_done_task_index:
            done_listbox.delete(selected_done_task_index)

# Ввод задачи
text1 = tk.Label(root, background='bisque', text='Введите задачу')
text1.pack(pady=5)

entry = tk.Entry(root, width=50, bg='burlywood1')
entry.pack(pady=10)

# Создаем фрейм для кнопок
buttons_frame = tk.Frame(root, background='bisque')
buttons_frame.pack(pady=5)

# Кнопки внутри фрейма
add_task_btn = tk.Button(buttons_frame, background='DarkGoldenrod1', text='Добавить задачу', command=add_task)
add_task_btn.pack(side=tk.LEFT, padx=5)

done_btn = tk.Button(buttons_frame, background='green3', text='Задача выполнена', command=mark_done)
done_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(buttons_frame, background='firebrick', text='Удалить задачу', command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=5)

# Создаем фрейм для подписи списка задач и выполненных задач
labels_frame = tk.Frame(root, background='bisque')
labels_frame.pack(pady=10)

tasks_label = tk.Label(labels_frame, bg='bisque', text='Текущие задачи')
tasks_label.pack(side=tk.LEFT, padx=100)

done_label = tk.Label(labels_frame, bg='bisque', text='В процессе исполнения')
done_label.pack(side=tk.LEFT, padx=100)


# Создаем фрейм для списка задач и выполненных задач
lists_frame = tk.Frame(root, background='bisque')
lists_frame.pack(pady=5)

tasks_listbox = tk.Listbox(lists_frame, width=50, height=10, bg='burlywood1', selectmode=tk.SINGLE)
tasks_listbox.pack(side=tk.LEFT, padx=10)

done_listbox = tk.Listbox(lists_frame, width=50, height=10, bg='burlywood1', selectmode=tk.SINGLE)
done_listbox.pack(side=tk.LEFT, padx=10)

root.mainloop()
