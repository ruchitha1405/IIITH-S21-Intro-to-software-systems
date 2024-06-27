from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return {"key" : "value"}

@app.route("/info", methods=['GET', 'POST'])
def info():
    # print(request.method)
    print(request.json)
    if request.method == 'GET':
        return "Get request called"
    elif request.method == 'POST':
        ans = 0
        try:
            data = request.args
            print(data)
            val1 = int(data['val1'])
            val2 = int(data['val2'])
            op = data['op']
            ans = 0
            if op == "add":
                ans = val1 + val2
            elif op == "sub":
                ans = val1 - val2
            elif op == "mul":
                ans = val1 * val2
            elif op == "div":
                if val2 == 0:
                    ans = "division by 0"
                else:
                    ans = val1/val2    
        except:
            ans = "Not enough parameters passed, something wrong"
        finally:
            return { "answer": ans}

app.run(debug=True)