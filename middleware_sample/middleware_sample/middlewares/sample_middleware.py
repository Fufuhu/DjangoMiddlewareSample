class SampleMiddleware(object):
    """
    サンプルのmiddleware、
    リクエストがviewで処理される前と、
    レスポンスがクライアントに返される前に画面に文字列表示を行うだけ
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)

        return response

    def process_request(self, request):
        print("リクエストの処理")

    def process_response(self, request, response):
        print("レスポンスの処理")

