import wikipedia
import webbrowser
from flask import Flask, request,render_template,redirect,url_for
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip


@app.route('/show/<search1>')
def show(search1):
    result = wikipedia.search(search1)
    result = tuple(result)
    list1 = []
    url_list = []
    for i in range(len(result)):
        detail = wikipedia.summary(result[i], sentences=1)
        list1.append(detail)
        urlDetail = wikipedia.page(result[i])
        urls = urlDetail.url
        url_list.append(urls)
    tuple1 = tuple(list1)
    tuple2 = tuple(url_list)
    length = len(tuple1)
    return render_template('index.html', result=result, tuple1=tuple1, tuple2=tuple2, length=length)

@app.route('/search_result', methods = ['POST','GET'])
def search_result():
    if request.method == "POST":
        search = request.form['wiki_search']
    return redirect(url_for('show', search1 = search))

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/randompage', methods = ['POST','GET'])
def random_page():
    if request.method == "POST":
        ran_wiki = wikipedia.random()
        ran_url = wikipedia.page(ran_wiki)
        ran_urls = ran_url.url
        webbrowser.open(ran_urls)
    return '0',204

if __name__ == '__main__':
    app.run(debug=True)
