class Report:
    def __init__(self, content: str):
        self.content: str = content

    def generate(self):
        print("Report: ", self.content)

class ReportSaver:
    def __init__(self, report: Report):
        self.report: Report = report
    
    def file_saver(self, file_name: str):
        with open(file_name, "w") as f:
            f.write(self.report.content)

if __name__ == "__main__":
    report_content = "I did my homework."
    report = Report(report_content)

    report.generate()

    report_saver = ReportSaver(report)
    report_saver.file_saver("report")


