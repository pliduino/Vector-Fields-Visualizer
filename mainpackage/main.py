import sys

import plotting
import ui

app = ui.gui.MyApp()
#window = Window('Program Name')
window = ui.gui.LoadUI()
window.show()
sys.exit(app.exec())

#plotter = plotting.plotter.PlotClass
#plotter.plot(input('Enter X function: '), input('Enter Y function: '))