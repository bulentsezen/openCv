using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using OpenCvSharp;

public class yuzAlgilayici : MonoBehaviour
{
    // Start is called before the first frame update
    WebCamTexture _webCamTexture;
    CascadeClassifier cascade;
    OpenCvSharp.Rect MyFace;
    void Start()
    {
        WebCamDevice[] devices = WebCamTexture.devices;

        _webCamTexture = new WebCamTexture(devices[0].name);
        _webCamTexture.Play();
        
        cascade = new CascadeClassifier(Application.dataPath + "/haarcascade_frontalface_default.xml");
        // cascade = new CascadeClassifier(Application.dataPath + "/haarcascade_eye.xml");

    }

    // Update is called once per frame
    void Update()
    {
        GetComponent<Renderer>().material.mainTexture = _webCamTexture;
        Mat frame = OpenCvSharp.Unity.TextureToMat(_webCamTexture);

        findNewFace(frame);
        display(frame);
    }

    void findNewFace(Mat frame) 
    {
        var faces = cascade.DetectMultiScale(frame, 1.1, 2, HaarDetectionType.ScaleImage);

        if (faces.Length >= 1)
        {
            // Debug.Log(faces[0].Location);
            MyFace = faces[0];
        }
    }

    void display(Mat frame) 
    { 
        if (MyFace != null) 
        {
            frame.Rectangle(MyFace, new Scalar(250, 0, 0), 2);
        }

        Texture newtexture = OpenCvSharp.Unity.MatToTexture(frame);
        GetComponent<Renderer>().material.mainTexture = newtexture;

    }
}
