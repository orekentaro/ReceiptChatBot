from typing import Any, Tuple


class ReceiptCalculation:
    """レセプトの計算を行うクラス"""

    def __init__(self, total: int, contact: int) -> None:
        """初期化"""
        self.total: int = total
        self.contact: int = contact
        self.percent: float = self._division(total, contact)
        self.percent_string: str = self._parse_percent(self.percent)

    def _receipt_calculation(self, total: int, contact: int) -> Tuple[float, int, int]:
        """計算メイン関数"""
        if total < contact:
            return 0, 0, 0
        percent = self._division(total, contact)
        if not self._check_percent(percent):
            while not self._check_percent(percent):
                if self._check_percent_under(total, contact):
                    break
                total += 1
                contact += 1
                percent = self._division(total, contact)
        else:
            while self._check_percent(percent):
                if self._check_percent_over(total, contact):
                    break
                total -= 1
                contact -= 1
                percent = self._division(total, contact)
        return percent, total, contact

    def _division(self, denominator: int, molecule: int) -> float:
        """割合を計算"""
        try:
            return (molecule / denominator) * 100
        except ZeroDivisionError:
            return 0.0

    def _check_percent(self, percent: float) -> bool:
        """40%以上の判定"""
        return 39.85 <= percent and percent != 0

    def _check_percent_under(self, total: int, contact: int) -> bool:
        """割合の下限の確認"""
        percent = self._division(total + 1, contact + 1)
        return 39.90 <= percent and percent != 0

    def _check_percent_over(self, total: int, contact: int) -> bool:
        """割合の下限の確認"""
        percent = self._division(total - 1, contact - 1)
        return 39.90 >= percent and percent != 0

    def _parse_percent(self, percent: float) -> str:
        """%形式にフォーマット"""
        return_val = str(percent)[:5]
        if return_val == "100.":
            return_val = "100.0"
        return f"{return_val}%"

    def main(self) -> dict[str, Any]:
        """main関数"""
        percent, total, contact = self._receipt_calculation(self.total, self.contact)
        reduction = self.total - total
        percent_string = self._parse_percent(percent)
        self.percent_string = self._parse_percent(self.percent)

        result_dict = {
            "reduction": reduction,
            "total": self.total,
            "contact": self.contact,
            "percent": self.percent_string,
            "result_total": total,
            "result_contact": contact,
            "result_percent": percent_string,
        }
        return result_dict

    def serialization(self, result_dict: dict) -> str:
        """LINEのテキストにフォーマット"""
        return_txt = "【計算結果】\n"
        if result_dict["reduction"] > 0:
            return_txt += "🔥40%を超えました🔥\n"
            return_txt += "\n"
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
            return_txt += "【削除前】\n"
            return_txt += f"全数: {result_dict['total']}人\n"
            return_txt += f"CL数: {result_dict['contact']}人\n"
            return_txt += "\n"
            return_txt += "【削除後】\n"
            return_txt += f"全数: {result_dict['result_total']}人\n"
            return_txt += f"CL数: {result_dict['result_contact']}人"
        elif result_dict["reduction"] < 0:
            return_txt += "💰40%を下回りました💰\n"
            return_txt += "\n"
            return_txt += f"増加数: {result_dict['reduction'] * -1}人\n"
            return_txt += "\n"
            return_txt += f"増加前: {result_dict['percent']}\n"
            return_txt += f"増加後: {result_dict['result_percent']}\n"
            return_txt += "\n"
            return_txt += "\n"
            return_txt += "--------------------\n"
            return_txt += "🤔エビデンス🤔\n"
            return_txt += "--------------------\n"
            return_txt += "\n"
            return_txt += "【増加前】\n"
            return_txt += f"全数: {result_dict['total']}人\n"
            return_txt += f"CL数: {result_dict['contact']}人\n"
            return_txt += "\n"
            return_txt += "【増加後】\n"
            return_txt += f"全数: {result_dict['result_total']}人\n"
            return_txt += f"CL数: {result_dict['result_contact']}人"
        else:
            return_txt += "🎉今の数字で大丈夫だよ🎉\n"
            return_txt += "\n"
            return_txt += f"結果: {result_dict['percent']}"
        return return_txt


# TODO: 39.85%
