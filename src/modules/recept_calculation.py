class ReceiptCalculation:
    def __init__(self, total: int, contact: int) -> None:
        self.total: int = total
        self.contact: int = contact
        self.percent: float = self._division(total, contact)

    def _receipt_calculation(self, total: int, contact: int) -> float:
        if total < contact:
            return 0, 0, 0
        percent: float = self._division(total, contact)
        if not self._check_percent(percent):
            while not self._check_percent(percent):
                if self._check_percent_under(total, contact):
                    break
                total += 1
                contact += 1
                percent = self._division(total, contact)
        else:
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

    def _check_percent(self, percent: float) -> bool:
        return 40.0 <= percent and percent != 0

    def _check_percent_under(self, total: int, contact: int) -> bool:
        percent = self._division(total+1, contact+1)
        return 39.95 < percent and percent != 0

    def _parse_percent(self, percent: float) -> str:
        return_val = str(percent)[:5]
        if return_val == "100.":
            return_val = "100.0"
        return f"{return_val}%"

    def main(self):
        percent, total, contact = self._receipt_calculation(
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
        return_txt = "??????????????????\n"
        if result_dict["reduction"] > 0:
            return_txt += "????40%??????????????????????\n"
            return_txt += "\n"
            return_txt += f"?????????: {result_dict['reduction']}???\n"
            return_txt += "\n"
            return_txt += f"?????????: {result_dict['percent']}\n"
            return_txt += f"?????????: {result_dict['result_percent']}\n"
            return_txt += "\n"
            return_txt += "\n"
            return_txt += "--------------------\n"
            return_txt += "???????????????????????\n"
            return_txt += "--------------------\n"
            return_txt += "\n"
            return_txt += "???????????????\n"
            return_txt += f"??????: {result_dict['total']}???\n"
            return_txt += f"CL???: {result_dict['contact']}???\n"
            return_txt += "\n"
            return_txt += "???????????????\n"
            return_txt += f"??????: {result_dict['result_total']}???\n"
            return_txt += f"CL???: {result_dict['result_contact']}???"
        elif result_dict["reduction"] < 0:
            return_txt += "????40%?????????????????????????\n"
            return_txt += "\n"
            return_txt += f"?????????: {result_dict['reduction'] * -1}???\n"
            return_txt += "\n"
            return_txt += f"?????????: {result_dict['percent']}\n"
            return_txt += f"?????????: {result_dict['result_percent']}\n"
            return_txt += "\n"
            return_txt += "\n"
            return_txt += "--------------------\n"
            return_txt += "???????????????????????\n"
            return_txt += "--------------------\n"
            return_txt += "\n"
            return_txt += "???????????????\n"
            return_txt += f"??????: {result_dict['total']}???\n"
            return_txt += f"CL???: {result_dict['contact']}???\n"
            return_txt += "\n"
            return_txt += "???????????????\n"
            return_txt += f"??????: {result_dict['result_total']}???\n"
            return_txt += f"CL???: {result_dict['result_contact']}???"
        else:
            return_txt += "??????????????????????????????????????\n"
            return_txt += "\n"
            return_txt += f"??????: {result_dict['percent']}"
        return return_txt
