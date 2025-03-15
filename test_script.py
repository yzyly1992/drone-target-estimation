from target_estimation import estimate_real_coords, TargetTracker
import math

if __name__ == "__main__":
    # Initialize target tracker
    tracker = TargetTracker()

    # # Pos-2 0836 39.73701311214281, -105.07958894136262
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73706794444445, -105.0800276388889
    # altitude = 80  # meters
    # heading = 90.2  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 2517, 1752  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-2 0839 39.736865571820985, -105.07967486297535
    # # 39.73686562023648, -105.07967475083579
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73706761111112, -105.0800261111111
    # altitude = 80  # meters
    # heading = 134.9  # degrees
    # gimbal_pitch = -60  # degrees
    # x_pixel, y_pixel = 1528, 1764  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-2 0847 39.73678022937951, -105.0797172265706
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73601733333334, -105.0793547222222
    # altitude = 80  # meters
    # heading = -44.9  # degrees
    # gimbal_pitch = -32  # degrees
    # x_pixel, y_pixel = 3420, 2020  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-2 0850 39.736945640212674, -105.07951830715356
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73601772222222, -105.0793538333333
    # altitude = 80  # meters
    # heading = 0  # degrees
    # gimbal_pitch = -32  # degrees
    # x_pixel, y_pixel = 1553,  1803  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-1 0891 39.73804088899502, -105.07757316593765
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73789672222222, -105.0775895555555
    # altitude = 80  # meters
    # heading = -179.9  # degrees
    # gimbal_pitch = -89.9  # degrees
    # x_pixel, y_pixel = 2282, 2123  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-1 0896 39.73791502862122, -105.07770015247475
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.7378975, -105.0775902777778
    # altitude = 80  # meters
    # heading = -89.9  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 2664, 2764  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-1 0899 39.73802502575232, -105.07773353431065
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73789705555556, -105.0775910555556
    # altitude = 80  # meters
    # heading = -44.9  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 2242, 2420  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-1 0903 39.73793989524488, -105.07755437246217
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73789808333333, -105.0775898333333
    # altitude = 80  # meters
    # heading = 45  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 1324, 2921  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-3 0021 34.040917579314474, -118.53552154609152
    # # Initialize drone parameters
    # drone_lat, drone_lon = 34.04031486111111, -118.5352650833333
    # altitude = 80  # meters
    # heading = -44.8  # degrees
    # gimbal_pitch = -32  # degrees
    # x_pixel, y_pixel = 3451, 2394  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-3 0022 34.04092585242436, -118.53551655380284
    # # Initialize drone parameters
    # drone_lat, drone_lon = 34.04031472222222, -118.5352650277778
    # altitude = 80  # meters
    # heading = -44.8  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 3485, 861  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-3 0023 34.04112077782075, -118.53538856995128
    # # Initialize drone parameters
    # drone_lat, drone_lon = 34.04031505555555, -118.5352648888889
    # altitude = 80  # meters
    # heading = -0.1  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 1588, 505  # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-3 0053 34.04117825256812, -118.5353483534665
    # # Initialize drone parameters
    # drone_lat, drone_lon = 34.04137161111111, -118.5345688333333
    # altitude = 80  # meters
    # heading = -89.7  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 1031, 788 # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-4 0824 39.736668031894666, -105.0803522963074
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73706677777778, -105.0800284444444
    # altitude = 80  # meters
    # heading = 179.7  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 3858, 1334 # Image size 1600x1200
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-4 0826 39.73659069761638, -105.08070185374521
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73706641666666, -105.0800280555556
    # altitude = 80  # meters
    # heading = -134.9  # degrees
    # gimbal_pitch = -32  # degrees
    # x_pixel, y_pixel = 2141, 2241
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-4 0828 39.73682027213527, -105.08064866652333
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73706722222222, -105.08002825
    # altitude = 80  # meters
    # heading = -89.8  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 424, 1136
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-4 0829 39.73681666426292, -105.0806315971058
    # # Initialize drone parameters
    # drone_lat, drone_lon = 39.73706769444445, -105.0800291111111
    # altitude = 80  # meters
    # heading = -89.8  # degrees
    # gimbal_pitch = -32  # degrees
    # x_pixel, y_pixel = 362, 2682
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-5 0635 28.076701719594567, -82.46638443277486
    # # Initialize drone parameters
    # drone_lat, drone_lon = 28.07650508333333, -82.46653719444444
    # altitude = 80  # meters
    # heading = 0  # degrees
    # gimbal_pitch = -60  # degrees
    # x_pixel, y_pixel = 3983, 2136
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-5 0637 28.076775174319057, -82.46606034295554
    # # Initialize drone parameters
    # drone_lat, drone_lon = 28.0765055, -82.46653669444444 
    # altitude = 80  # meters
    # heading = 45.3  # degrees
    # gimbal_pitch = -32  # degrees
    # x_pixel, y_pixel = 2697, 2763
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-5 0638 28.076782498558124, -82.46605152411313
    # # Initialize drone parameters
    # drone_lat, drone_lon = 28.07650552777778, -82.46653669444444
    # altitude = 80  # meters
    # heading = 45.1  # degrees
    # gimbal_pitch = -60  # degrees
    # x_pixel, y_pixel = 2696, 1210
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-5 0639 28.07661819721678, -82.46597009645227
    # # Initialize drone parameters
    # drone_lat, drone_lon = 28.07650558333333, -82.46653633333334
    # altitude = 80  # meters
    # heading = 90  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 1275, 1207
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-6 0643 28.07585096812442, -82.4653575709036
    # # Initialize drone parameters
    # drone_lat, drone_lon = 28.07621194444445, -82.46539161111112 
    # altitude = 80  # meters
    # heading = -179.9  # degrees
    # gimbal_pitch = -90  # degrees
    # x_pixel, y_pixel = 1720, 51
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-6 0644 28.075843343492018, -82.46536353269025
    # # Initialize drone parameters
    # drone_lat, drone_lon = 28.07621183333333, -82.46539141666668
    # altitude = 80  # meters
    # heading = -179.9  # degrees
    # gimbal_pitch = -60  # degrees
    # x_pixel, y_pixel = 1774, 1658
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # # Pos-6 0647 28.07600417894965, -82.46549801158157
    # # Initialize drone parameters
    # drone_lat, drone_lon = 28.07621186111111, -82.46539150000001 
    # altitude = 80  # meters
    # heading = -134.9  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 816,2183
    # hfov, vfov = 69.73, 55.17  # degrees
    # image_width, image_height = 4000, 3000

    # Pos-6 0656 28.076174339401913, -82.46530460214758
    # Initialize drone parameters
    drone_lat, drone_lon = 28.07621322222222, -82.46539088888889
    altitude = 80  # meters
    heading = 90  # degrees
    gimbal_pitch = -59.9  # degrees
    x_pixel, y_pixel = 3545, 2768
    hfov, vfov = 69.73, 55.17  # degrees
    image_width, image_height = 4000, 3000

    # Estimate target coordinates
    target_lat, target_lon = estimate_real_coords(
        drone_lat, drone_lon, altitude, heading, gimbal_pitch, x_pixel, y_pixel,
        image_width, image_height, hfov, vfov
    )

    # Add target to tracker
    target_id = tracker.add_target(target_lat, target_lon)
    print(f"Target ID: {target_id}, Latitude and Longitude: {target_lat}, {target_lon}")