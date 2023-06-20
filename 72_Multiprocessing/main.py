import multiprocessing
import concurrent.futures
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"file/file{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == '__main__': 
    ## Method 1 
    url = "https://picsum.photos/3840/2160"    
    pros = []
    for i in range(5):
        # downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)
    for p in pros:
            p.join() 
    
    ## Method 2
    # url = "https://picsum.photos/3840/2160"    
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #         l1 = [url for i in range(5)]
    #         l2 = [i for i in range(5)]
    #         executor.map(downloadFile, l1, l2)


'''
OUTPUT

Started Downloading 1
Started Downloading 0
Started Downloading 2
Started Downloading 3
Started Downloading 4
Finished Downloading 0
Finished Downloading 4
Finished Downloading 3
Finished Downloading 2
Finished Downloading 1
'''