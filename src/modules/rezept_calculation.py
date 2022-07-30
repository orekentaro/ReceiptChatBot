class RezeptCalculation:
    def __init__(self, total: int, contact: int) -> None:
        self.total: int = total
        self.contact: int = contact

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

    def main(self):
        percent, total, contact = self._rezept_calculation(
            self.total,
            self.contact
        )
        reduction = self.total - total
        percent = str(percent)[:4]

        percent = f"{percent}%"
        result_dict = {
                    "reduction": reduction,
                    "percent": percent,
                    "total": self.total,
                    "contact": self.contact,
                    "result_total": total,
                    "result_contact": contact
                }
        return result_dict

    def serialization(self, result_dict: dict) -> str:
        return_txt = f"削除人数: {result_dict['reduction']}\n"
        return_txt += f"トータル人数: {result_dict['total']}\n"
        return_txt += f"トータルコンタクト人数: {result_dict['contact']}\n"
        return_txt += f"削除後トータル人数: {result_dict['result_total']}\n"
        return_txt += f"削除後コンタクト人数: {result_dict['result_contact']}\n"
        return_txt += f"削除後パーセンテージ: {result_dict['percent']}"
        return return_txt
