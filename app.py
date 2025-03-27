import streamlit as st
import pydicom
from PIL import Image
import numpy as np
import io

st.set_page_config(page_title="DICOM Viewer", layout="centered")
st.title("🩻 DICOMファイルビューア")

uploaded_file = st.file_uploader("DICOMファイルをアップロードしてください", type=["dcm"])

if uploaded_file is not None:
    try:
        # ファイルをpydicomで読み込む
        dicom_bytes = uploaded_file.read()
        dicom_data = pydicom.dcmread(io.BytesIO(dicom_bytes))

        # DICOM画像のピクセルデータを取得
        pixel_array = dicom_data.pixel_array

        # 正規化して8bit画像に変換（0-255）
        image_8bit = ((pixel_array - pixel_array.min()) / (np.ptp(pixel_array)) * 255).astype(np.uint8)

        # PILで画像を作成
        image = Image.fromarray(image_8bit)

        # 情報表示
        st.subheader("📋 メタデータ")
        st.write(f"患者ID: {dicom_data.get('PatientID', 'N/A')}")
        st.write(f"モダリティ: {dicom_data.get('Modality', 'N/A')}")
        st.write(f"スタディ日付: {dicom_data.get('StudyDate', 'N/A')}")

        st.subheader("🖼 画像")
        st.image(image, caption="DICOM Image", use_container_width=True)

    except Exception as e:
        st.error(f"読み込みエラー: {str(e)}")
