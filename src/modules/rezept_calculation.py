class RezeptCalculation:
    def __init__(self, total: int, contact: int) -> None:
        self.total: int = total
        self.contact: int = contact
        self.percent: float = self._division(total, contact)

    def _rezept_calculation(self, total: int, contact: int) -> float:
        if total < contact:
            return 0, 0, 0
        percent: float = self._division(total, contact)
        while self._check_percent(percent):
            total -= 1
            contact -= 1
            percent = self._division(total, contact)
        return percent, total, contact

    def _division(self, denominator: int, molecule: int) -> float:
        try:
            return (molecule / denominator) * 100
        except ZeroDivisionError:
            return 0

    def _check_percent(self, percernt: float) -> bool:
        return 40.0 <= percernt and percernt != 0

    def _parse_percent(self, percent: float) -> str:
        return_val = str(percent)[:4]
        if return_val == "100.":
            return_val = "100.0"
        return f"{return_val}%"

    def main(self):
        percent, total, contact = self._rezept_calculation(
            self.total,
            self.contact
        )
        reduction = self.total - total
        percent = self._parse_percent(percent)
        self.percent = self._parse_percent(self.percent)

        result_dict = {
                    "reduction": reduction,
                    "total": self.total,
                    "contact": self.contact,
                    "percent": self.percent,
                    "result_total": total,
                    "result_contact": contact,
                    "result_percent": percent
                }
        return result_dict

    def serialization(self, result_dict: dict) -> str:
        
        return_txt = "【計算結果】\n"
        return_txt += f"削除数: {result_dict['reduction']}人\n"
        return_txt += "\n"
        return_txt += f"削除前: {result_dict['percent']}\n"
        return_txt += f"削除後: {result_dict['result_percent']}\n"
        return_txt += "\n"
        return_txt += "\n"
        return_txt += "--------------------\n"
        return_txt += "🧐エビデンス🧐\n"
        return_txt += "--------------------\n"
        return_txt += "\n"
        return_txt += "【削除前】"
        return_txt += f"全数: {result_dict['total']}人\n"
        return_txt += f"CL数: {result_dict['contact']}人\n"
        return_txt += "\n"
        return_txt += "【削除後】"
        return_txt += f"全数: {result_dict['result_total']}人\n"
        return_txt += f"CL数: {result_dict['result_contact']}人"
        return return_txt
