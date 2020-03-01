import pygame
# import schedule
# import os
import time

recipes = {'basicFurnace': {'ironPlate': [60, ['ironOre', 'coal']], 'copperPlate': [60, ['copperOre', 'coal']],
                            'SteelBeam': [320, ['ironPlate', 'coal']]},
           'steelFurnace': {'ironPlate': [30, ['ironOre', 'coal']], 'copperPlate': [30, ['copperOre', 'coal']],
                            'SteelBeam': [160, ['ironPlate', 'coal']]},
           'basicCrafter': {'copperCable': [10, ['copperPlate']], 'ironRod': [10, ['ironPlate']],
                            'ironGear': [10, ['ironPlate', 'ironPlate']],
                            'electronicCircuit': [10, ['copperCable', 'copperCable', 'copperCable', 'ironPlate']],
                            'advancedCircuit': [120, ['copperCable', 'copperCable', 'copperCable', 'copperCable',
                                                      'electronicCircuit', 'electronicCircuit',
                                                      'plasticBar', 'plasticBar']],
                            'engineUnit': [200, ['ironGear', 'pipe', 'pipe', 'SteelBeam']],
                            'robotFrame': [400, ['battery', 'battery', 'electricEngineUnit', 'electronicCircuit',
                                                 'electronicCircuit', 'electronicCircuit', 'SteelBeam']],
                            'lowDensityStructure': [400, ['copperPlate', 'copperPlate', 'copperPlate', 'copperPlate',
                                                          'copperPlate', 'plasticBar', 'plasticBar', 'plasticBar',
                                                          'plasticBar', 'plasticBar', 'SteelBeam', 'SteelBeam']]
                            },
           'advancedCrafter': [1], 'basicDrill': [0.5], 'eDrill': [1],
           'oilRig': [1], 'refinery': [1], 'chemicalPlant': [1],
           'inventoryCrafting': {'copperCable': [10, ['copperPlate']], 'ironRod': [10, ['ironPlate']],
                                 'ironGear': [10, ['ironPlate', 'ironPlate']],
                                 'electronicCircuit': [10, ['copperCable', 'copperCable', 'copperCable', 'ironPlate']],
                                 'advancedCircuit': [120, ['copperCable', 'copperCable', 'copperCable', 'copperCable',
                                                           'electronicCircuit', 'electronicCircuit',
                                                           'plasticBar', 'plasticBar']],
                                 'engineUnit': [200, ['ironGear', 'pipe', 'pipe', 'SteelBeam']],
                                 'robotFrame': [400, ['battery', 'battery', 'electricEngineUnit', 'electronicCircuit',
                                                      'electronicCircuit', 'electronicCircuit', 'SteelBeam']],
                                 'lowDensityStructure': [400,
                                                         ['copperPlate', 'copperPlate', 'copperPlate', 'copperPlate',
                                                          'copperPlate', 'plasticBar', 'plasticBar', 'plasticBar',
                                                          'plasticBar', 'plasticBar', 'SteelBeam', 'SteelBeam']]}}

FileNamesOfItems = {'coal': 'data/items/32px-Coal.png', 'copperOre': 'data/items/32px-Copper_ore.png',
                    'ironOre': 'data/items/32px-Iron_ore.png',
                    'stone': 'data/items/32px-Stone.png', 'uraniumOre': 'data/items/32px-Uranium_ore.png',
                    'advancedCircuit': 'data/items/Advanced_circuit.png',
                    'battery': 'data/items/Battery.png', 'copperCable': 'data/items/Copper_cable.png',
                    'copperPlate': 'data/items/Copper_plate.png',
                    'crudeOil': 'data/items/Crude_oil.png', 'electricEngineUnit': 'data/items/Electric_engine_unit.png',
                    'electronicCircuit': 'data/items/Electronic_circuit.png',
                    'engineUnit': 'data/items/Engine_unit.png', 'heavyOil': 'data/items/Heavy_oil.png',
                    'ironGear': 'data/items/Iron_gear_wheel.png',
                    'ironPlate': 'data/items/Iron_plate.png', 'ironRod': 'data/items/Iron_stick.png',
                    'lightOil': 'data/items/Light_oil.png',
                    'lubricant': 'data/items/Lubricant.png', 'petroleumGas': 'data/items/Petroleum_gas.png',
                    'plasticBar': 'data/items/Plastic_bar.png',
                    'processingUnit': 'data/items/Processing_unit.png',
                    'rocketControlUnit': 'data/items/Rocket_control_unit.png',
                    'rocketPart': 'data/items/Rocket_part.png',
                    'satellite': 'data/items/Satellite.png', 'steam': 'data/items/Steam.png',
                    'SteelBeam': 'data/items/Steel_beam.png',
                    'sulfur': 'data/items/Sulfur.png', 'sulfuricAcid': 'data/items/Sulfuric_acid.png',
                    'uraniumFuelCell': 'data/items/Uranium_fuel_cell.png',
                    'uranium235': 'data/items/Uranium-235.png', 'uranium238': 'data/items/Uranium-238.png',
                    'water': 'data/items/Water.png', 'pipe': 'data/items/pipe.png',
                    'robotFrame': 'data/items/robot_frame.png',
                    'lowDensityStructure': 'data/items/low_density_structure.png',
                    'logistics': 'data/item-group/logistics.png', 'production': 'data/item-group/production.png',
                    'intermediate-products': 'data/item-group/intermediate-products.png',
                    'advancedCrafter': 'data/machines/advancedCrafter.png',
                    'basicCrafter': 'data/machines/basicCrafter.png', 'basicDrill': 'data/machines/basicDrill.png',
                    'basicFurnace': 'data/machines/basicFurnace.png',
                    'chemicalPlant': 'data/machines/chemicalPlant.png',
                    'eDrill': 'data/machines/eDrill.png', 'oilRig': 'data/machines/oilRig.png',
                    'refinery': 'data/machines/refinery.png', 'steelFurnace': 'data/machines/steelFurnace.png'}
# '':'data/items/.png'

exceptions = ['coal', 'copperOre', 'ironOre', 'stone', 'uraniumOre', 'production', 'logistics', 'intermediate-products']

machines = {'basicFurnace': [], 'steelFurnace': [], 'basicCrafter': [],
            'advancedCrafter': [], 'basicDrill': [], 'eDrill': [],
            'oilRig': [], 'refinery': [], 'chemicalPlant': [], 'inventoryCrafting': []}  # 'eliteCrafter': [],


def load_image(name, colorkey=None):
    # fullname = os.path.join('data', name)
    image = pygame.image.load(name).convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def allCrafts():
    for i in allCafters:
        i.craft()


class Crafter:
    def __init__(self, name_of_machine, recipe):
        self.name = name_of_machine
        self.recipe = recipe
        if self.recipe in recipes[self.name]:
            self.ticks_to_craft = recipes[self.name][self.recipe][0]
            self.local_ticks = self.ticks_to_craft

    def craft(self):
        # print(self.local_ticks)
        if self.local_ticks == 0:
            successful = True
            self.local_ticks = self.ticks_to_craft
            for i in range(len(recipes[self.name][self.recipe][1])):
                if not inventory.addItem(recipes[self.name][self.recipe][1][i], -1):
                    successful = False
                    ended = i
                    break
            if not successful:
                # print(False)
                for j in range(len(recipes[self.name][self.recipe][1][:ended])):
                    inventory.addItem(recipes[self.name][self.recipe][1][j], 1)
            else:
                inventory.addItem(self.recipe, 1)
                # print(True)
        else:
            self.local_ticks -= 1


class InventoryCrafter(Crafter):
    def craft(self):
        # print(self.recipe)
        if self.recipe in recipes[self.name]:
            super().craft()
            if self.local_ticks == self.ticks_to_craft:
                # print(True)
                self.recipe = ''

    def addRecipe(self, recipe):
        self.recipe = recipe
        if self.recipe in recipes[self.name]:
            self.ticks_to_craft = recipes[self.name][self.recipe][0]
            self.local_ticks = self.ticks_to_craft


class Inventory:
    def __init__(self, w, h, names_of_items):
        self.width = w
        self.height = h
        self.x = 0
        self.y = 0
        self.items = []
        self.cells = []
        for i in range((size[1] - self.height - 432) // 40 * 10):
            self.cells.append(Cell((self.width + self.x) * scale_x, (self.height + self.y) * scale_y))
            self.x += 40
            if self.x >= 400:
                self.x = 0
                self.y += 40
        self.x = 0
        self.y = 0
        for i in names_of_items:
            s = self.addItem(i[0], i[1])
            del s
            # self.x += 40
            # if self.x >= 400:
            #     self.x = 0
            #     self.y += 40

    def addItem(self, item_name, quantity):
        if len(self.items) > 0:
            is_added = False
            for i in self.items:
                if i.getItemName() == item_name and quantity > 0:
                    i.addToSlot(quantity)
                    is_added = True
                    break
                elif i.getItemName() == item_name and quantity < 0 and i.getQuantity() >= abs(quantity):
                    i.addToSlot(quantity)
                    is_added = True
                    print(228, i.getQuantity == 0)
                    break
            if not is_added and quantity > 0:
                self.items.append(Item(self.width + self.x, self.height + self.y, item_name, quantity))
                self.x += 40
                is_added = True
                if self.x >= 400:
                    self.x = 0
                    self.y += 40
            for i in range(len(self.items)):
                print(self.items[i].getItemName(), self.items[i].getQuantity())
                if self.items[i].getQuantity() == 0:
                    print('del')
                    self.items[i].kill()
                    del self.items[i]

                    self.render()
                    break
            if is_added:
                return True
            else:
                return False
        else:
            if quantity > 0:
                self.items.append(Item(self.width + self.x, self.height + self.y, item_name, quantity))
                self.x += 40
                if self.x >= 400:
                    self.x = 0
                    self.y += 40
                return True
            else:
                return False

    def render(self):
        it = self.items
        for i in self.items:
            i.kill()
        self.items = []
        self.x = 0
        self.y = 0
        for i in range(len(it)):
            self.items.append(Item((self.width + self.x) * scale_x,
                                   (self.height + self.y) * scale_y, it[i].getItemName(), it[i].getQuantity()))
            self.x += 40
            if self.x >= 400:
                self.x = 0
                self.y += 40
        for i in it:
            i.kill()

    def delItem(self, item_name):
        for i in range(len(self.items)):
            if self.items[i].getItemName() == item_name:
                self.items[i].kill()
                del self.items[i]


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_name, quantity=1):
        super().__init__(Item_sprites, intermediate_products_sprites)
        self.x = x
        self.y = y
        self.item_name = item_name
        self.quantity = quantity
        self.image = pygame.image.load(FileNamesOfItems[self.item_name]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(32 * scale_x), int(32 * scale_y)))
        self.rect = self.image.get_rect().move(self.x, self.y)

    def addToSlot(self, quantity):
        if self.quantity + quantity >= 0:
            self.quantity += quantity

    def getItemName(self):
        return self.item_name

    def getQuantity(self):
        return self.quantity

    def resize(self):
        self.image = pygame.image.load(FileNamesOfItems[self.item_name]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(32 * scale_x), int(32 * scale_y)))
        self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)


class TextForItems(pygame.sprite.Sprite):
    def __init__(self, x, y, text):
        super().__init__(intermediate_products_sprites, Item_text_sprites)
        self.x = x
        self.y = y
        self.text = text
        font = pygame.font.Font('data/fonts/Lato-Bold.ttf', (self.x, self.y))
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    def changeText(self, text):
        self.text = text


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(Cell_sprites, Lightable_sprites, intermediate_products_sprites)
        self.image = pygame.image.load('data/UI/cell_for_items.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(38 * scale_x), int(38 * scale_y)))
        self.rect = self.image.get_rect().move(self.x, self.y)
        self.is_lighted = False

    def light(self):
        if not self.is_lighted:
            self.image = pygame.image.load('data/UI/lighted_cell_for_items.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (int(38 * scale_x), int(38 * scale_y)))
            self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)
            self.is_lighted = True

    def unlight(self):
        if self.is_lighted:
            self.image = pygame.image.load('data/UI/cell_for_items.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (int(38 * scale_x), int(38 * scale_y)))
            self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)
            self.is_lighted = False

    def resize(self):
        self.image = pygame.transform.scale(self.image, (int(38 * scale_x), int(38 * scale_y)))
        self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, name_of_button, name_of_image, switch=True):
        self.kind = {'logistics': [200, 200], 'production': [200, 200], 'intermediate-products': [200, 200],
                     'craft': [36, 36]}
        self.x = x
        self.y = y
        self.item_name = name_of_image
        self.cell_name = name_of_button
        super().__init__(Interface_sprites, Lightable_sprites, Buttons_sprites)
        self.image = pygame.image.load('data/UI/Button.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.kind[self.cell_name][0] * scale_x),
                                                         int(self.kind[self.cell_name][1] * scale_y)))
        self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)
        self.img = ImageForButton(self.x, self.y, self.item_name,
                                  (self.kind[self.cell_name][0], self.kind[self.cell_name][1]))
        self.is_lighted = False
        self.is_switch = switch
        self.is_pressed = False

    def light(self):
        if not self.is_lighted or not self.is_pressed:
            self.image = pygame.image.load('data/UI/lightedButton.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (int(self.kind[self.cell_name][0] * scale_x),
                                                             int(self.kind[self.cell_name][1] * scale_y)))
            self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)
            self.img.resize()
            self.is_pressed = False
            self.is_lighted = True

    def unlight(self):
        if self.is_lighted and not self.is_pressed:
            self.image = pygame.image.load('data/UI/Button.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (int(self.kind[self.cell_name][0] * scale_x),
                                                             int(self.kind[self.cell_name][1] * scale_y)))
            self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)
            self.img.resize()
            self.is_lighted = False

    def getCellName(self):
        return self.cell_name

    def getItemName(self):
        return self.item_name

    def press(self):
        if self.is_switch and self.is_pressed:
            self.image = pygame.image.load('data/UI/Button.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (int(self.kind[self.cell_name][0] * scale_x),
                                                             int(self.kind[self.cell_name][1] * scale_y)))
            self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)
            self.img.resize()
            self.is_pressed = False
        elif self.is_switch and not self.is_pressed:
            self.image = pygame.image.load('data/UI/pressedButton.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (int(self.kind[self.cell_name][0] * scale_x),
                                                             int(self.kind[self.cell_name][1] * scale_y)))
            self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)
            self.img.resize()
            self.is_pressed = True
        elif not self.is_switch:
            self.image = pygame.image.load('data/UI/pressedButton.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (int(self.kind[self.cell_name][0] * scale_x),
                                                             int(self.kind[self.cell_name][1] * scale_y)))
            self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)
            self.is_pressed = True
            self.img.resize()

    def resize(self):
        self.image = pygame.transform.scale(self.image, (int(self.kind[self.cell_name][0] * scale_x),
                                                         int(self.kind[self.cell_name][1] * scale_y)))
        self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)
        self.img.resize()


class ImageForButton(pygame.sprite.Sprite):
    def __init__(self, x, y, name, sizes):
        super().__init__(Interface_sprites)
        self.x = x
        self.y = y
        self.sizes = sizes
        self.name = name
        self.image = pygame.image.load(FileNamesOfItems[self.name]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.sizes[0] * scale_x), int(self.sizes[1] * scale_y)))
        self.rect = self.image.get_rect().move(self.x * scale_x, self.y * scale_y)

    def getItemName(self):
        return self.name

    def resize(self):
        self.image = pygame.image.load(FileNamesOfItems[self.name]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.sizes[0] * scale_x), int(self.sizes[1] * scale_y)))
        self.rect = self.image.get_rect().move(int(self.x * scale_x), int(self.y * scale_y))


FPS = 60
pygame.init()
size = width, height = 1920, 1080
full_size = True
resize = False
color_palette = [(51, 51, 51), (76, 76, 76), (218, 145, 0), (187, 111, 36), (239, 217, 185), (31, 31, 31), (41, 41, 41)]
scale_x = width / 1920
scale_y = height / 1080
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
running = True
UI_sprites = pygame.sprite.Group()
Item_sprites = pygame.sprite.Group()
Cell_sprites = pygame.sprite.Group()
Interface_sprites = pygame.sprite.Group()
Lightable_sprites = pygame.sprite.Group()
intermediate_products_sprites = pygame.sprite.Group()
Item_text_sprites = pygame.sprite.Group()
Buttons_sprites = pygame.sprite.Group()
renderabel = 'intermediate-products'
inventory = Inventory(100, 100, [('ironPlate', 10), ('ironPlate', 20), ('lightOil', 10), ('copperPlate', 10)])
button_kinds = ['logistics', 'production', 'intermediate-products', 'craft']
Button(10, 700, 'logistics', button_kinds[0])
Button(260, 700, 'production', button_kinds[1])
Button(510, 700, 'intermediate-products', button_kinds[2])
craftButtons = []
local_x = 960
local_y = 50
for item in FileNamesOfItems:
    if item not in exceptions:
        craftButtons.append(Button(local_x, local_y, button_kinds[3], item, False))
        local_x += 40
        if local_x >= 1850:
            local_x = 960
            local_y += 40
del local_x, local_y
allCafters = [InventoryCrafter('inventoryCrafting', ''), Crafter('basicCrafter', 'copperCable')]
pygame.mixer.music.load('data/music/65daysofstatic - Tomorrow Lull Celestial Feedback lowQ.mp3')
pygame.mixer.music.play()
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN, 32)
# schedule.every(0.05).second().do(allCrafts)  # every(50).millisecond().do(allCrafts)
timer = time.process_time()
while running:
    # print(time.process_time())
    allCrafts()
    if time.process_time() % 0.05 == 0:
        # print(1, time.process_time())
        allCrafts()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_F11:
                if full_size:
                    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN, 32)
                    full_size = False
                else:
                    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                    full_size = True
        elif e.type == pygame.MOUSEBUTTONDOWN:
            for item in Buttons_sprites:
                if item.rect.collidepoint(e.pos):
                    if item.getCellName() in button_kinds and item.getCellName() != 'craft':
                        renderabel = button_kinds[button_kinds.index(item.getItemName())]
                        item.press()
                    elif item.getCellName() == 'craft':
                        print(item.getItemName())
                        allCafters[0].addRecipe(str(item.getItemName()))
                        item.press()
        elif e.type == pygame.MOUSEMOTION:
            for item in Lightable_sprites:
                if item.rect.collidepoint(e.pos):
                    item.light()
                else:
                    item.unlight()
            for j in Item_sprites:
                if j.rect.collidepoint(e.pos):
                    print(j.getQuantity())
        elif e.type == pygame.VIDEORESIZE:
            height = e.h
            width = e.h // 0.5625
            size = int(width), int(height)
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            scale_x = width / 1920
            scale_y = height / 1080
            resize = True
    screen.fill(color_palette[0])
    pygame.draw.rect(screen, color_palette[1], (0, 680 * scale_y, 1920, 240 * scale_y), 0)
    pygame.draw.rect(screen, color_palette[6], (900 * scale_x, 0, 1020 * scale_x, 680 * scale_y), 0)
    pygame.draw.rect(screen, color_palette[5], (900 * scale_x, 0, 1020 * scale_x, 680 * scale_y), 1)
    if renderabel == 'intermediate-products':
        intermediate_products_sprites.draw(screen)
        Item_sprites.draw(screen)
        if resize:
            for item in intermediate_products_sprites:
                item.resize()
            for item in Interface_sprites:
                item.resize()
    elif renderabel == 'logistics':
        if resize:
            for item in Interface_sprites:
                item.resize()
    elif renderabel == 'production':
        if resize:
            for item in Interface_sprites:
                item.resize()
    Interface_sprites.draw(screen)
    pygame.display.flip()
