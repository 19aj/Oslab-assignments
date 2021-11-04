import csv

PRODUCTS=[]       #   list of dicts

def load_data():
    product_dict={}
    print('Stock :')
    with open ('database.csv') as f:
        reader=csv.reader(f)
        for line in reader:
            product_dict={'code':line[0],'name':line[1], \
                          'price':line[2],'count':line[3]}
            #info = line[:-1].split(',')
            #product_dict={'code':info[0],'name':info[1], \
                          #'price':info[2],'count':info[3]}
            
            PRODUCTS.append(product_dict)
    print('---------------------------------------------------------')
        #print(PRODUCTS)
            #print(info)
            #print(line,end='')


def show_menu():
    print('1. Add\n2. Edit\n3. Delete\n4. Show List\n'\
          '5. Search\n6. Buy\n7. Save & Exit\n')

def add():
    print('Adding Products ')
    new_product={'code':input('Product Code : '),'name':input('Product Name : '),
                'price':input('Product Price : '),'count':input('Product Count : ')}
    print(new_product)
    ex=0
    with open ('database.csv','a',newline='') as fa:
        writer=csv.DictWriter(fa,fieldnames=['code','name','price','count'])
        for product in PRODUCTS:
            if new_product['code'] == product['code'] or new_product['name'] == product['name'] :         
                ex=1
                print('Product Already Exists! You Can Edit It')
                return
            else :
                #writer=csv.DictWriter(fa,fieldnames=['code','name','price','count'])
                writer.writerow(new_product)
                print('--- Product Added ---')
                return
'''  
   ex=1
        for k,v in new_product.items():
            if v not in PRODUCTS:
                writer.write((v,','))
            else :
                print('Product Already Exists! You Can Edit It.')
                ex=0
 '''
                 
def edit():
    print('Editing Products')
    edit_name=input('Product Name : ')
    in_stock=False
    index=0
    for product in PRODUCTS:
        if product['name']==edit_name :
            in_stock=True
            break
        else:
            index+=1
    if in_stock:
        while True :
            choice=int(input('Edit\n1. Code\n2. Name\n3. Price\n4. Count/n5. Quit Edit'))
            if choice==1:
                new_code=inout('New Code : ')
                PRODUCTS[index]['code']=new_code
                with open ('database.csv','w',newline='') as fa:
                    writer=csv.DictWriter(fa,fieldnames=['code','name','price','count'])
                    for product in PRODUCTS:
                        writer.writerow(product)
            elif choice==2:
                new_name=inout('New Name : ')
                PRODUCTS[index]['name']=new_name
                with open ('database.csv','w',newline='') as fa:
                    writer=csv.DictWriter(fa,fieldnames=['code','name','price','count'])
                    for product in PRODUCTS:
                        writer.writerow(product)
            elif choice==3:
                new_price=inout('New Price : ')
                PRODUCTS[index]['price']=new_price
                with open ('database.csv','w',newline='') as fa:
                    writer=csv.DictWriter(fa,fieldnames=['code','name','price','count'])
                    for product in PRODUCTS:
                        writer.writerow(product)
            elif choice==4:
                new_code=inout('New Count : ')
                PRODUCTS[index]['count']=new_count
                with open ('database.csv','w',newline='') as fa:
                    writer=csv.DictWriter(fa,fieldnames=['code','name','price','count'])
                    for product in PRODUCTS:
                        writer.writerow(product)
            elif choice==5:
                print('--- Edit Saved ---')
                break
            else :
                print('Choose Between 1 and 5')
        else:
            print('Product is Out of Stock! You Can Add It.')
                    
        
    

def delete():
    print('Deleting Products')
    delete_name=input('Product Name')
    for i in range(0,len(PRODUCTS)):
        if PRODUCTS[i]['name']==delete_name:
            del PRODUCTS[i]
            break
            
    with open ('database.csv','w',newline='') as fd:
                    writer=csv.DictWriter(fd,fieldnames=['code','name','price','count'])
                    for product in PRODUCTS:
                        writer.writerow(product)
            
    


def show_list():
    #print('ID\tName\tPrice\tCount')
    print("{:<9} {:<13} {:<12} {:<11}".format('ID','Name','Price','Count'))
    #for product in PRODUCTS :
        #print(product['code'],'\t',product['name'],'\t',\
              #product['price'],'\t',product['count'])
    for product in PRODUCTS:
        print ("{:<9} {:<13} {:<12} {:<11}".format(product['code'],product['name'],\
              product['price'],product['count']))
        #for k, v in product.items():
            #cod, nam, pric, cnt = v
            #print ("{:<9} {:<11} {:<12} {:<11}".format(cod, nam, pric, cnt))
        #print ("{:<9} {:<11} {:<12} {:<11}".format(v))
        #print(product)

               
def search():
    print('Searching Product ')
    search_name=input('Product Name : ')
    for i in range(0,len(PRODUCTS)):
        if PRODUCTS[i]['name']==search_name:
            print('Product Found!')
            for k,v in PRODUCTS[i].items():
                print(k.upper(),' : ',v,end='  |  ')

                
def buy():
    print('Shopping')
    basket=[]
    
    while True:
        choice = int(input('1. Buy Product\n2. Show Basket\n3. Quit\n'))
        if choice==1:
            buy_name=input('Product Name : ')
            for product in PRODUCTS:
                if product['name']==buy_name:
                    qty=int(input('Quantity : '))
                    

    

    
load_data()
show_list()
#show_menu()
add()
#add()
#add()
delete()
print(PRODUCTS)
while True:
    break
    show_menu()
    choice=int(input('Enter Your Choice : '))
    
    
    