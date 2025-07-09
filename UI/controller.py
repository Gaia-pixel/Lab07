import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self.mese = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        self.mese = self._view.dd_mese.value
        if self.mese is None:
            self._view.lst_result.controls.append(ft.Text("Selezionare un mese di riferimento"))
            self._view.update_page()
            return
        umiditaMese = self._model.getUmidita(self.mese)
        for c, u in umiditaMese:
            self._view.lst_result.controls.append(ft.Text(f"{c}: {u}"))
        self._view.update_page()


    def handle_sequenza(self, e):
        costo, sequenza = self._model.getSequenza(self.mese)
        self._view.lst_result.controls.append(ft.Text(f"Sequenza ottima con costo : {costo}"))
        for s in sequenza:
            self._view.lst_result.controls.append(ft.Text(f"{s.localita}: {s.umidita}"))
        self._view.update_page()


    def read_mese(self, e):
        self._mese = int(e.control.value)

