import "../styles/FaceImage.css";
import React from "react";
import { useState, useCallback } from "react";
import Cropper from 'react-easy-crop'
import * as faceapi from 'face-api.js';
import ReactModal from "react-modal";
import getCroppedImg from "./Crop";
await faceapi.loadFaceLandmarkModel('/models')
await faceapi.loadTinyFaceDetectorModel('/models')
// const addCSS = css => document.head.appendChild(document.createElement("style")).innerHTML=css;

const customStyles = {
    content: {
        position: 'relative',
        width: '1400px',
        height: '730px',
    },
};

const detect = async (val) => {
    if (val) {
        const input = document.getElementById('img1')
        const input2 = document.getElementById('img2')
        // const landmarks = await faceapi.detectFaceLandmarks(input, new faceapi.FaceLandmark68Net());
        const detections = await faceapi.detectSingleFace(input, new faceapi.TinyFaceDetectorOptions());
        const detections2 = await faceapi.detectSingleFace(input2, new faceapi.TinyFaceDetectorOptions());
        faceapi.draw.drawDetections(input, detections)
        faceapi.draw.drawDetections(input2, detections2)
        // faceapi.draw.drawFaceLandmarks(input, landmarks)
    }   
    else {
        alert("사진을 업로드해주세요.")
    }
}

const FaceImage = () => {
    const [file1, setFile1] = useState();
    const [file2, setFile2] = useState();
    const [isUploaded1, setIsUploaded1] = useState(false);
    const [isUploaded2, setIsUploaded2] = useState(false);
    const [isOpen, setIsOpen] = useState(false);
    const [modalImg, setModalImg] = useState();
    const [crop, setCrop] = useState({ x: 0, y: 0 })
    const [zoom, setZoom] = useState(1)
    const [croppedImage, setCroppedImage] = useState(null);
    const [croppedAreaPixels, setCroppedAreaPixels] = useState(null);
    const [canvasnum, setCanvasnum] = useState(1);

    const onCropComplete = useCallback((croppedArea, croppedAreaPixels) => {
        setCroppedAreaPixels(croppedAreaPixels);
      }, []);

    const handleChange1 = (e) => {
        setFile1(URL.createObjectURL(e.target.files[0]));
        setModalImg(URL.createObjectURL(e.target.files[0]));
        setCanvasnum(1);
        setIsOpen(true);
        setIsUploaded1(true);
    }
    const handleChange2 = (e) => {
        setFile2(URL.createObjectURL(e.target.files[0]));
        setModalImg(URL.createObjectURL(e.target.files[0]));
        setCanvasnum(2);
        setIsOpen(true);
        setIsUploaded2(true);
    }

    const showCroppedImage = useCallback(async () => {
    try {
        setIsOpen(false);
        const croppedImage = await getCroppedImg(
        {imageSrc: modalImg,
        pixelCrop: croppedAreaPixels,
        canvn: canvasnum}
        );
        console.log("done", { croppedImage });
        setCroppedImage(croppedImage);
    } catch (e) {
        console.error(e);
    }
    }, [croppedAreaPixels, modalImg, canvasnum]);

    return (  
        <div className="upload">
            
            <div className="explain">
                <h1 className="me">본인 사진 업로드</h1>
                <button className="btn" onClick={()=>(detect(isUploaded1&&isUploaded2))}>비교하기</button>
                <h1 className="me">다른 사람 사진 업로드</h1>
            </div>
            
            <div className="buttons">
                <input type="file" accept="image/*" id="ex1_file" onChange={handleChange1} /> 
                <label htmlFor="ex1_file">파일 선택</label>
                <input type="file" accept="image/*" id="ex2_file" onChange={handleChange2} />
                <label htmlFor="ex2_file">파일 선택</label>
                
                <ReactModal isOpen={isOpen} style={customStyles}>
                    <h1 className="modaltitle">이미지 크기 조정</h1>
                    <div className="cropper">
                        <Cropper
                            image={modalImg}
                            crop={crop}
                            zoom={zoom}
                            zoomSpeed={0.1}
                            minZoom={0.5}
                            maxZoom={3}
                            showGrid={true}
                            zoomWithScroll={true}
                            cropShape="rect"
                            cropSize={{ width: 461.6, height: 496.6 }}
                            onCropChange={setCrop}
                            onCropComplete={onCropComplete}
                            onZoomChange={setZoom}
                        />
                    </div>
                    <div className="but">
                        <button className="okbutton" onClick={showCroppedImage}>완료</button>
                    </div>
                </ReactModal>

            </div>
            <div className="face-image">

                <div className="user">
                    <canvas id="img1">
                    </canvas>
                    {/* <img src={file1} id='inp1'/> */}
                </div>

                <div className="ans">
                    <canvas id="ansimg">

                    </canvas>
                </div>
                
                <div className="other">
                    <canvas id="img2">
                    </canvas>
                    {/* <img src={file2} id='inp2'/> */}
                </div>
                
            </div>
        </div>
    );
}

export default FaceImage;