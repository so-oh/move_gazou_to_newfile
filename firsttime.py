#フォルダのファイルを取得するライブラリ
import os
#ファイルの移動をするライブラリ
import shutil

#フォルダ内の画像ファイルを検索する関数
def find_image_files(source_folder):
    image_files = []
    for file_name in os.listdir(source_folder):
        # ファイルの絶対パスをjoinで結合する（ディレクトリパス、ファイル名）
        file_path = os.path.join(source_folder, file_name)
        #ファイルのパスを確認する
        if os.path.isfile(file_path):
            # ファイルの拡張子を取得し、画像ファイルであるか確認
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                #append()モジュールはリストの末尾に追加していく
                image_files.append(file_path)
    return image_files

#移動先のファイルを作成する関数
def create_destination_folder(destination_folder):
    if not os.path.exists(destination_folder):
        #パスがない場合にディレクトリを新規作成する
        os.makedirs(destination_folder)

#移動元フォルダから移動先フォルダにファイルを移す関数
def organize_images(source_folder, destination_folder):
    # 画像ファイルを見つける
    image_files = find_image_files(source_folder)
    
    # 宛先フォルダを作成する
    create_destination_folder(destination_folder)

    # 移す画像ファイルについての処理
    for image_file in image_files:
        #basenameモジュールでパス内のファイル名部分を取り出し、
        file_name = os.path.basename(image_file)
        #joinモジュールで新たに作ったディレクトリのパス名と結合
        destination_path = os.path.join(destination_folder, file_name)

        #ファイル・フォルダを別の場所に移動している
        shutil.move(image_file, destination_path) 
        print(f"{file_name} を {destination_folder} に移動しました。")

# 整理したい画像ファイルが含まれるフォルダのパスを指定
source_folder = '/Users/kataokaso/desktop/隼人'

# 整理後の画像ファイルを保存するフォルダのパスを指定
destination_folder = '/Users/kataokaso/desktop/隼人/画像お片付け'

# 画像ファイルの整理を実行
organize_images(source_folder, destination_folder)


