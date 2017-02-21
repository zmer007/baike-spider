class HtmlOutput(object):
    def __init__(self):
        self.dataList = []

    def collect_data(self, data):
        if data is None:
            return
        self.dataList.append(data)

    def output_html(self):
        file = open('output.html', 'w')
        file.write("<html>")
        file.write("<body>")
        file.write("<table>")

        # ascii
        for data in self.dataList:
            file.write("<tr>")
            file.write("<td> %s </td>" % data['url'])
            file.write("<td> %s </td>" % data['title'].encode('utf-8'))
            file.write("<td> %s </td>" % data['summary'].encode('utf-8'))
            file.write("</tr>")

        file.write("</table>")
        file.write("</body>")
        file.write("</html>")
