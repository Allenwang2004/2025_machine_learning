import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np

# 使用內建的 etree parser 來讀取 XML 並提取 <Content> 標籤的內容
tree = ET.parse("O-A0038-003.xml")
root = tree.getroot()

# 尋找 Content 標籤 (需要處理命名空間)
namespace = {'cwa': 'urn:cwa:gov:tw:cwacommon:0.1'}
content_element = root.find('.//cwa:Content', namespace)

if content_element is not None:
    content_text = content_element.text
    print("正在處理溫度格點數據...")
    
    # 將內容轉換成數值陣列
    # 先將內容按行分割，再處理每行的數據
    lines = content_text.strip().split('\n')
    all_values = []
    
    for line in lines:
        line = line.strip()  # 移除行首行尾空白
        if line:  # 如果行不為空
            line_values = line.split(',')
            all_values.extend(line_values)
    
    # 轉換為浮點數
    numeric_values = []
    for val in all_values:
        val = val.strip()
        if val:  # 確保值不為空
            try:
                numeric_val = float(val)
                numeric_values.append(numeric_val)
            except ValueError:
                continue
    
    # 將數據轉換成格點陣列（120 排, 每排 67 個數值）
    data_array = np.array(numeric_values)
    grid_data = data_array.reshape(120, 67)
    print(grid_data)
    
    print(f"數據形狀: {grid_data.shape}")
    print(f"總共有 {len(numeric_values)} 個數值")
    
    # 生成經緯度座標
    # 修改為從左上角開始：往下走緯度遞減，往右走經度遞增
    # 左上角座標為東經120.00度、北緯25.45度
    # 經向及緯向解析度均為0.03度
    
    start_lon = 120.00  # 起始經度 (左上角)
    start_lat = 25.45   # 起始緯度 (左上角)
    resolution = 0.03   # 解析度
    
    # 創建經緯度網格
    longitudes = np.arange(start_lon, start_lon + 67 * resolution, resolution)  # 往右遞增
    latitudes = np.arange(start_lat, start_lat - 120 * resolution, -resolution)  # 往下遞減
    
    print(f"經度範圍: {longitudes[0]:.2f}° 到 {longitudes[-1]:.2f}°")
    print(f"緯度範圍: {latitudes[0]:.2f}° 到 {latitudes[-1]:.2f}°")
    
    # 創建分類數據集 (Classification Dataset)
    print("\n=== 創建分類數據集 ===")
    classification_data = []
    
    for lat_idx in range(120):  # 緯度索引
        for lon_idx in range(67):  # 經度索引
            lon = longitudes[lon_idx]
            lat = latitudes[lat_idx]
            temp_value = grid_data[lat_idx, lon_idx]
            
            # 設定標籤：-999為無效值(label=0)，其他為有效值(label=1)
            label = 0 if temp_value == -999.0 else 1
            classification_data.append([lon, lat, label])
    
    classification_df = pd.DataFrame(classification_data, columns=['經度', '緯度', 'label'])
    
    # 統計分類數據
    valid_count = len(classification_df[classification_df['label'] == 1])
    invalid_count = len(classification_df[classification_df['label'] == 0])
    
    print(f"有效數據點: {valid_count}")
    print(f"無效數據點: {invalid_count}")
    print("分類數據集前5筆:")
    print(classification_df.head())
    
    # 創建回歸數據集 (Regression Dataset) - 僅保留有效值
    print("\n=== 創建回歸數據集 ===")
    regression_data = []
    
    for lat_idx in range(120):
        for lon_idx in range(67):
            lon = longitudes[lon_idx]
            lat = latitudes[lat_idx]
            temp_value = grid_data[lat_idx, lon_idx]
            
            # 僅保留有效的溫度觀測值（剔除 -999）
            if temp_value != -999.0:
                regression_data.append([lon, lat, temp_value])
    
    regression_df = pd.DataFrame(regression_data, columns=['經度', '緯度', '溫度'])
    
    print(f"回歸數據集大小: {len(regression_df)}")
    if len(regression_df) > 0:
        print(f"溫度範圍: {regression_df['溫度'].min():.1f}°C 到 {regression_df['溫度'].max():.1f}°C")
        print("回歸數據集前5筆:")
        print(regression_df.head())
    
    # 儲存數據集
    classification_df.to_csv('classification_dataset.csv', index=False, encoding='utf-8')
    regression_df.to_csv('regression_dataset.csv', index=False, encoding='utf-8')
    
    print(f"\n數據集已儲存:")
    print(f"- 分類數據集: classification_dataset.csv ({len(classification_df)} 筆資料)")
    print(f"- 回歸數據集: regression_dataset.csv ({len(regression_df)} 筆資料)")
    
else:
    print("找不到 Content 標籤")