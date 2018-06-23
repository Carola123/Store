from bottle import route, run, template, static_file, get, post, delete, request
import json
import pymysql

connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='store',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
print(connection)

@get("/admin")
def admin_portal():
	return template("pages/admin.html")


@get("/")
def index():
    return template("index.html")

@get("/categories")
def categories():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM category"
            cursor.execute(sql)
            categories = cursor.fetchall()
            result = {
                'STATUS': "SUCCESS",
                'MSG': "",
                'CATEGORIES': categories,
                'CODE': 200}
    except:
        result = {
            'STATUS': "ERROR",
            'MSG': "Internal error",
            'CATEGORIES': "",
            'CODE': 500}
    return json.dumps(result)

@get("/category/<id>/products")
def category_id_products(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product WHERE category =" + id
            cursor.execute(sql)
            products = cursor.fetchall()
            result = {
                'STATUS': "SUCCESS",
                'MSG': "",
                'PRODUCTS': products,
                'CODE': 200}
    except:
        result = {
            'STATUS': "ERROR",
            'MSG': "Internal error",
            'PRODUCTS': "",
            'CODE': 500}
    return json.dumps(result)

@get("/products")
def products():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product"
            cursor.execute(sql)
            products = cursor.fetchall()
            result = {
                'STATUS': "SUCCESS",
                'MSG': "",
                'PRODUCTS': products,
                'CODE': 200
            }
    except:
        result = {
            'STATUS': "ERROR",
            'MSG': "Internal error",
            'PRODUCTS': "",
            'CODE': 500
        }
    return json.dumps(result)

@get("/product/<id>")
def products_id(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product WHERE id =" + id
            cursor.execute(sql)
            product = cursor.fetchone()
            result = {
                'STATUS': "SUCCESS",
                'MSG': "",
                'PRODUCT': product,
                'CODE': 200
            }
    except:
        result = {
            'STATUS': "ERROR",
            'MSG': "Internal error",
            'PRODUCT': "",
            'CODE': 500
        }
    return json.dumps(result)

@post("/category")
def category():
    name = request.forms.get("name")
    print(name)
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO category (name) VALUES ('"+ name +"')"
            cursor.execute(sql)
            connection.commit()
            cat_id= cursor.lastrowid
            result = {'STATUS': "SUCCESS",
                      'MSG': "",
                      'CAT_ID': cat_id,
                      'CODE':200}
            print(result)

    except:
        result = {'STATUS': "ERROR",
                  'MSG': "Internal error",
                  'CAT_ID': "",
                  'CODE': 500}
    return json.dumps(result)

@post("/product")
def product():
    id = request.forms.get("id")
    title = request.forms.get("title")
    descrip = request.forms.get("desc")
    price = request.forms.get("price")
    img_url  = request.forms.get("img_url")
    category  = request.forms.get("category")
    favorite  = request.forms.get("favorite")
    if id == "":
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO product (title, descrip, price, img_url, category, favorite) VALUES('" + title + "', '" + descrip + "', " + price + ",  '" + img_url + "', '" + category + "', '" + favorite + "')"
                print(sql)
                cursor.execute(sql)
                product_id = cursor.lastrowid
                result = {'STATUS': "SUCCESS",
                          'MSG': "",
                          'PRODUCT_ID':product_id,
                          'CODE': 201}
        except:
            result = {'STATUS': "ERROR",
                      'MSG': "Internal error",
                      'PRODUCT_ID': "",
                      'CODE': 500}
    else:
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE product SET title='"+title+"', descrip='"+ descrip +"', price='"+ price +"', img_url='" + img_url + "', category='"+ category +"', favorite= '"+ favorite +"' WHERE id=" + id
                cursor.execute(sql)
                product_id = cursor.lastrowid
                result = {'STATUS': "SUCCESS",
                          'MSG': "",
                          'PRODUCT_ID':product_id,
                          'CODE': 201}
        except:
            result = {'STATUS': "ERROR",
                      'MSG': "Internal error",
                      'PRODUCT_ID': "",
                      'CODE': 500}

    return json.dumps(result)

@delete("/product/<id>")
def deleteProduct(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM product WHERE id = " + id
            cursor.execute(sql)
            result = {
                'STATUS' : "SUCCESS",
                'MSG' : "",
                'CODE': 201}
    except:
        result = {
            'STATUS': "ERROR",
            'MSG': "Internal error",
            'CODE': 500}
    return json.dumps(result)

@delete('/category/<id>')
def deleteCategory(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM category WHERE id = " + id
            cursor.execute(sql)
            result = {'STATUS':"SUCCESS",
                      'MSG':"",
                      'CODE': 201}
    except:
        result = {'STATUS': "ERROR",
                  'MSG': "Internal error",
                  'CODE': 500}
    return json.dumps(result)

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


run(host='localhost', port=7000)

if __name__ == '__main__':
    main()


