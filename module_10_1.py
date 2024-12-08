import threading

import time

def write_words(word_count, file_name):

    with open(file_name, 'w+', encoding = 'utf-8') as file:
        for i in range(word_count):
            # started_at = time.time()
            file.write(f'Какое-то слово № {i+1} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')



started_at_1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at_1 = time.time()
res_time_1 = ended_at_1 - started_at_1
print(f' Работа функций составила {res_time_1} секунд')




started_at_2 = time.time()

thr1 = threading.Thread(target=write_words, args=(10, 'example5.txt') )
thr2 = threading.Thread(target=write_words, args=(30, 'example6.txt') )
thr3 = threading.Thread(target = write_words, args=(200, 'example7.txt'))
thr4 = threading.Thread(target= write_words, args=(100, 'example8.txt'))

thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr1.join()
thr2.join()
thr3.join()
thr4.join()

ended_at_2 = time.time()
res_time_2 = ended_at_2 - started_at_2

print(f' Работа потоков составила {res_time_2} секунд')
