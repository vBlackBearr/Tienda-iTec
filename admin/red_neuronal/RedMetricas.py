import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler

# Crear un DataFrame vacío para combinar los datos
combined_data = pd.DataFrame(columns=["Mes", "Cantidad"])

# Cargar los 8 archivos XLSX correspondientes a cada año
for year in range(2015, 2023):  
    file_name = f"{year}.xlsx"  
    data = pd.read_excel(file_name)
    combined_data = pd.concat([combined_data, data], ignore_index=True)

# Crear un diccionario que mapee los nombres de los meses a números
meses = {
    'Enero': 1,
    'Febrero': 2,
    'Marzo': 3,
    'Abril': 4,
    'Mayo': 5,
    'Junio': 6,
    'Julio': 7,
    'Agosto': 8,
    'Septiembre': 9,
    'Octubre': 10,
    'Noviembre': 11,
    'Diciembre': 12
}

# Usar el diccionario para mapear los nombres de los meses a números en tu DataFrame
combined_data['Mes'] = combined_data['Mes'].map(meses)

# Convertir los datos a formato flotante
combined_data = combined_data.astype({'Mes': float, 'Cantidad': float})

# Normalizar los datos (escalar entre 0 y 1)
scaler = MinMaxScaler()
combined_data[['Mes', 'Cantidad']] = scaler.fit_transform(combined_data[['Mes', 'Cantidad']])

# Ahora, tus datos de meses estarán normalizados
X = combined_data['Mes'].values
y = combined_data['Cantidad'].values

# Modelo 
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, input_dim=1, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X, y, epochs=50, batch_size=8)  # Aumenta las épocas y el tamaño del lote

y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("Error cuadrático medio (MSE):", mse)
print("Error absoluto medio (MAE):", mae)
print("Coeficiente de determinación (R²):", r2)

# Realizar predicciones para un nuevo mes (por ejemplo, mes 12)
new_month = np.array([12.0]).astype('float32')  # Puedes cambiar este valor para el mes que desees
predicted_sales = model.predict(new_month)

# Desnormalizar la predicción
predicted_sales = scaler.inverse_transform(np.array([[0, predicted_sales[0][0]]]))[0][1]

print("Predicción de ventas:", predicted_sales)

# Lógica para decidir cuándo realizar la solicitud de inventario
umbral_superior = 0.8  # Ajusta este umbral según tus necesidades
umbral_inferior = 0.2  # Ajusta este umbral según tus necesidades

if predicted_sales > umbral_superior:
    print("Realizar solicitud de inventario: ¡Ventas proyectadas muy altas!")
    # Aquí puedes agregar la lógica para generar la solicitud de reorden y enviarla a los proveedores.

elif predicted_sales < umbral_inferior:
    print("Realizar solicitud de inventario: ¡Ventas proyectadas muy bajas!")
    # Aquí puedes agregar la lógica para generar la solicitud de reorden y enviarla a los proveedores.

else:
    print("No es necesario realizar una solicitud de inventario en este momento.")
