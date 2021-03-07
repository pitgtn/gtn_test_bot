class EpicGame:
    NO_IMAGE_TAG = 'no_image'

    def __init__(self, item_price, item_img, item_status_message, item_name, item_end_date_utc):
        self.item_price = item_price
        self.item_img = item_img
        self.item_status_message = item_status_message
        self.item_name = item_name
        self.item_end_date_utc = item_end_date_utc

    def pretty_print_me(self):
        if (self.item_img == self.NO_IMAGE_TAG):
            return (f"\n{self.item_status_message} - <b>{self.item_name}</b>, обычно по {self.item_price}")
        else:
            return (
                f"<a href=\"{self.item_img}\">&#8203;</a>\n{self.item_status_message} - <b>{self.item_name}</b>, обычно по {self.item_price}")
