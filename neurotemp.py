import numpy as np
 
 
def sigmoid(x):
    # Функция активации sigmoid:: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))
 
 
def deriv_sigmoid(x):
    # Производная от sigmoid: f'(x) = f(x) * (1 - f(x))
    fx = sigmoid(x)
    return fx * (1 - fx)
 
 
def mse_loss(y_true, y_pred):
    # y_true и y_pred являются массивами numpy с одинаковой длиной
    return ((y_true - y_pred) ** 2).mean()
 
 
class OurNeuralNetwork:
    """
    Нейронная сеть, у которой:
        - 2 входа
        - скрытый слой с двумя нейронами (h1, h2)
        - слой вывода с одним нейроном (o1)
 
    *** ВАЖНО ***:
    Код ниже написан как простой, образовательный. НЕ оптимальный.
    Настоящий код нейронной сети выглядит не так. НЕ ИСПОЛЬЗУЙТЕ этот код.
    Вместо этого, прочитайте/запустите его, чтобы понять, как работает эта сеть.
    """
    # Обновление Алексея: добавлен возраст.
    # Получается:
    #  - 3 входа
    #  - скрытый слой с тремя нейронами (h1, h2, h3)
    #  - слой вывода с одним нейроном (o1)
    def __init__(self):
        # Вес
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()
        self.w7 = np.random.normal()
        self.w8 = np.random.normal()
        self.w9 = np.random.normal()
        self.w10 = np.random.normal()
        self.w11 = np.random.normal()
        self.w12 = np.random.normal()
 
        # Смещения
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()
        self.b4 = np.random.normal()
 
    def feedforward(self, x):
        # x является массивом numpy с тремя элементами
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.w3 * x[2] + self.b1)
        h2 = sigmoid(self.w4 * x[0] + self.w5 * x[1] + self.w6 * x[2] + self.b2)
        h3 = sigmoid(self.w7 * x[0] + self.w8 * x[1] + self.w9 * x[2] + self.b3)
        o1 = sigmoid(self.w10 * h1 + self.w11 * h2 + self.w12 * h3 + self.b4)
        return o1
 
    def train(self, data, all_y_trues):
        """
        - data is a (n x 3) numpy array, n = # of samples in the dataset.
        - all_y_trues is a numpy array with n elements.
            Elements in all_y_trues correspond to those in data.
        """
        learn_rate = 0.1
        epochs = 2000 # количество циклов во всём наборе данных
 
        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # --- Выполняем обратную связь (нам понадобятся эти значения в дальнейшем)
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.w3 * x[2] + self.b1
                h1 = sigmoid(sum_h1)
 
                sum_h2 = self.w4 * x[0] + self.w5 * x[1] + self.w6 * x[2] + self.b2
                h2 = sigmoid(sum_h2)
 
                sum_h3 = self.w7 * x[0] + self.w8 * x[1] + self.w9 * x[2] + self.b3
                h3 = sigmoid(sum_h3)
 
                sum_o1 = self.w10 * h1 + self.w11 * h2 + self.w12 * h3 + self.b4
                o1 = sigmoid(sum_o1)
                y_pred = o1
 
                # --- Подсчет частных производных
                # --- Наименование: d_L_d_w1 представляет "частично L / частично w1"
                d_L_d_ypred = -2 * (y_true - y_pred)
 
                # Нейрон o1
                d_ypred_d_w10 = h1 * deriv_sigmoid(sum_o1)
                d_ypred_d_w11 = h2 * deriv_sigmoid(sum_o1)
                d_ypred_d_w12 = h3 * deriv_sigmoid(sum_o1)
                d_ypred_d_b4 = deriv_sigmoid(sum_o1)
 
                d_ypred_d_h1 = self.w10 * deriv_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w11 * deriv_sigmoid(sum_o1)
                d_ypred_d_h3 = self.w12 * deriv_sigmoid(sum_o1)
 
                # Нейрон h1
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
                d_h1_d_w3 = x[2] * deriv_sigmoid(sum_h1)
                d_h1_d_b1 = deriv_sigmoid(sum_h1)
 
                # Нейрон h2
                d_h2_d_w4 = x[0] * deriv_sigmoid(sum_h2)
                d_h2_d_w5 = x[1] * deriv_sigmoid(sum_h2)
                d_h2_d_w6 = x[2] * deriv_sigmoid(sum_h2)
                d_h2_d_b2 = deriv_sigmoid(sum_h2)
 
                # Нейрон h3
                d_h3_d_w7 = x[0] * deriv_sigmoid(sum_h3)
                d_h3_d_w8 = x[1] * deriv_sigmoid(sum_h3)
                d_h3_d_w9 = x[2] * deriv_sigmoid(sum_h3)
                d_h3_d_b3 = deriv_sigmoid(sum_h3)
 
                # --- Обновляем вес и смещения
                # Нейрон h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w3
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1
 
                # Нейрон h2
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w6
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2
 
                # Нейрон h3
                self.w7 -= learn_rate * d_L_d_ypred * d_ypred_d_h3 * d_h3_d_w7
                self.w8 -= learn_rate * d_L_d_ypred * d_ypred_d_h3 * d_h3_d_w8
                self.w9 -= learn_rate * d_L_d_ypred * d_ypred_d_h3 * d_h3_d_w9
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_h3 * d_h3_d_b3
 
                # Нейрон o1
                self.w10 -= learn_rate * d_L_d_ypred * d_ypred_d_w10
                self.w11 -= learn_rate * d_L_d_ypred * d_ypred_d_w11
                self.w12 -= learn_rate * d_L_d_ypred * d_ypred_d_w12
                self.b4 -= learn_rate * d_L_d_ypred * d_ypred_d_b4
 
            # --- Подсчитываем общую потерю в конце каждой фазы
            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = mse_loss(all_y_trues, y_preds)
                print("Epoch %d loss: %.3f" % (epoch, loss))
 
 
# Определение набора данных
data = np.array([
    [50-40, 165-130, 30-30],    # Alice
    [90-40, 185-130, 40-30],     # Bob
    [34-40, 110-130, 7-30],     # Charlie
    [20-40, 70-130, 5-30], # Diana
])
 
all_y_trues = np.array([
    1, # Alice
    0, # Bob
    0, # Charlie
    1, # Diana
])
 
# Тренируем нашу нейронную сеть!
network = OurNeuralNetwork()
network.train(data, all_y_trues)

# Делаем предсказания
margo = np.array([55-40, 170-130, 40-30])
vladimir = np.array([86-40, 186-130, 40-30])
alex = np.array([60-40, 170-130, 15-30])
print("Margo: %.3f" % network.feedforward(margo))  # 0.951 - F
print("Vladimir: %.3f" % network.feedforward(vladimir))  # 0.039 - M
print("Alex: %.3f" % network.feedforward(alex))  # 0.039 - M
