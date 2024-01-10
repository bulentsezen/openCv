#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;


/////////////////  Images  //////////////////////

void main() {

    string path = "Resources/kitap.jpg";
    Mat img = imread(path);
    imshow("Image", img);
    Mat matrix, imgWarp;
    float w = 400, h = 600;

    Point2f src[4] = { {260,422},{1098,338},{335,1788},{1290,1696} };
    Point2f dst[4] = { {0.0f,0.0f},{w,0.0f},{0.0f,h},{w,h} };

    matrix = getPerspectiveTransform(src, dst);
    warpPerspective(img, imgWarp, matrix, Point(w, h));

    for (int i = 0; i < 4; i++)
    {
        circle(img, src[i], 10, Scalar(0, 0, 255), FILLED);
    }

    imshow("Image", img);
    imshow("Image Warp", imgWarp);

    waitKey(0);

}