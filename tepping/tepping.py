import pygame
import matplotlib.pyplot as plt

class TeppingTest:
	"""Класс для управления ресурсами и поведением программы."""
	
	def __init__(self):
		"""Инициализирует программу и создает необходимые ресурсы."""
		pygame.init()
		self.sc = pygame.display.set_mode((600, 400))
		pygame.display.set_caption("CrocoClo Tepping-test")

		# Набор цветов
		self.white = (255, 255, 255)
		self.croco_blue = (60, 185, 199)
		self.black = (0, 0, 0)
		
		# Настройки перемещающейся повехности
		self.start_time = None
		self.place = pygame.Surface((200, 200))
		self.place.fill(self.croco_blue)
		self.x, self.y = 0, 0

		# Настойки подсчета количества нажатий
		self.pl_1 = self.pl_2 = self.pl_3 = self.pl_4 = self.pl_5 = self.pl_6 = 0

		self.rect_1 = pygame.Rect(0, 0, 200, 200) 
		self.rect_2 = pygame.Rect(200, 0, 200, 200) 
		self.rect_3 = pygame.Rect(400, 0, 200, 200)
		self.rect_4 = pygame.Rect(400, 200, 200, 200)
		self.rect_5 = pygame.Rect(200, 200, 200, 200)
		self.rect_6 = pygame.Rect(0, 200, 200, 200)


		self.sc.fill(self.white)
		self.f1 = pygame.font.Font(None, 56)
		self.start_text1 = self.f1.render("НАЖМИТЕ ENTER", True, self.black)
		self.start_text2 = self.f1.render("чтобы начать тестирование", True, self.black)

		

		pygame.display.update()

		self.start = False

	def run_game(self):
		"""Запуск основного цикла программы."""
		while True:			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1 and self.start == False:
						self.start_time = pygame.time.get_ticks()
						self.start = True
					if event.button == 1 and self.start == True:
						ev = event.pos
						self.check_collide(ev)
			if self.start == True :
				self.surface_change()
				pygame.display.update()

	def check_collide(self, ev):
		if self.rect_1.collidepoint(ev) and 0 < pygame.time.get_ticks() - self.start_time < 5000:
			self.pl_1 += 1
		if self.rect_2.collidepoint(ev) and 5000 < pygame.time.get_ticks() - self.start_time < 10000:
			self.pl_2 += 1
		if self.rect_3.collidepoint(ev) and 10000 < pygame.time.get_ticks() - self.start_time < 15000:
			self.pl_3 += 1
		if self.rect_4.collidepoint(ev) and 15000 < pygame.time.get_ticks() - self.start_time < 20000:
			self.pl_4 += 1			
		if self.rect_5.collidepoint(ev) and 20000 < pygame.time.get_ticks() - self.start_time < 25000:
			self.pl_5 += 1			
		if self.rect_6.collidepoint(ev) and 25000 < pygame.time.get_ticks() - self.start_time< 30000:
			self.pl_6 += 1
				
	def surface_change(self):
		# Выделенная область перемещается по часовой стрелке каждые 5 секунд.
		if pygame.time.get_ticks() - self.start_time >= 0:
			self.sc.fill(self.white)
			self.sc.blit(self.place, (0, 0))
		if pygame.time.get_ticks() - self.start_time> 5000:
			self.sc.fill(self.white)
			self.sc.blit(self.place, (200, 0))
		if pygame.time.get_ticks() - self.start_time > 10000:
			self.sc.fill(self.white)
			self.sc.blit(self.place, (400, 0))
		if pygame.time.get_ticks() - self.start_time > 15000:
			self.sc.fill(self.white)
			self.sc.blit(self.place, (400, 200))
		if pygame.time.get_ticks() - self.start_time> 20000:
			self.sc.fill(self.white)
			self.sc.blit(self.place, (200, 200))
		if pygame.time.get_ticks() - self.start_time> 25000:
			self.sc.fill(self.white)
			self.sc.blit(self.place, (0, 200))
		if pygame.time.get_ticks() - self.start_time> 30000:
			self.sc.fill(self.white)
			self.finish_page()
			input_values = [1, 2, 3, 4, 5, 6]
			res = [self.pl_1, self.pl_2, self.pl_3, self.pl_4, self.pl_5, self.pl_6]

			plt.style.use('seaborn')
			fig, ax = plt.subplots()
			ax.plot(input_values, res, linewidth=3)

			# Назначение заголовка диаграммы и меток осей.
			
			ax.set_title("Результаты теппинг-теста", fontsize=24)
			ax.set_xlabel("Временные интервалы", fontsize=14)
			ax.set_ylabel("Количество точек", fontsize=14)

			# Назначение размера шрифта делений на осях.
			ax.tick_params(axis='both', labelsize=14)

			plt.show()
			exit()	

	def finish_page(self):
			f2 = pygame.font.Font(None, 30)
			finish_text = f2.render("Вы удачно завершили тестирование", True, self.black)
			result = f"Ваш результат {self.pl_1, self.pl_2, self.pl_3, self.pl_4, self.pl_5, self.pl_6}"
			result_text = f2.render(result, True, self.black)
			self.sc.blit(finish_text, (100, 120))
			self.sc.blit(result_text, (100, 170))

	def start_input(self):
	
		
		font = pygame.font.Font(None, 32)
		
		input_box = pygame.Rect(100, 100, 140, 32)
		color_inactive = pygame.Color('lightskyblue3')
		color_active = pygame.Color('dodgerblue2')
		color = color_inactive
		active = False
		input_step = True
		while input_step:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if input_box.collidepoint(event.pos):
						active = True
					else:
						active = False
					color = color_active if active else color_inactive
				if event.type == pygame.KEYDOWN:
					if active:
						if event.key == pygame.K_RETURN:
							print(self.text)
							self.text = ''
							input_step = False
						elif event.key == pygame.K_BACKSPACE:
							self.text = self.text[:-1]
						else:
							self.text += event.unicode
							
			self.sc.fill((self.white))
			self.sc.blit(self.start_text1, (100, 120))
			self.sc.blit(self.start_text2, (60, 170))
			txt_surface = font.render(self.text, True, color)
			width = max(200, txt_surface.get_width()+10)
			input_box.w = width
			self.sc.blit(txt_surface, (input_box.x+5, input_box.y+5))

			pygame.draw.rect(self.sc, color, input_box, 2)
			
			pygame.display.flip()

if __name__ == '__main__':
	# Создание экземпляра и запуск программы.
	tt = TeppingTest()
	tt.run_game()