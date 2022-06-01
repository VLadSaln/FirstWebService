FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install -y python3 
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
WORKDIR /src 
RUN apt-get update && \
    apt-get install -y cmake
RUN apt-get update && \
    apt-get install -y libgstreamer1.0-0 gstreamer1.0-dev gstreamer1.0-tools gstreamer1.0-doc
RUN apt-get update && \
    apt-get install -y gstreamer1.0-plugins-base gstreamer1.0-plugins-good
RUN apt-get update && \
    apt-get install -y gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
RUN apt-get update && \
    apt-get install -y gstreamer1.0-libav
RUN apt-get update && \
    apt-get install -y gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
RUN git clone https://github.com/opencv/opencv.git
WORKDIR /src/opencv
RUN git checkout 4.1.0
RUN mkdir build
WORKDIR /src/opencv/build
RUN  cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D PYTHON_EXECUTABLE=$(which python3) \
-D BUILD_opencv_python2=OFF \
-D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") \
-D PYTHON3_EXECUTABLE=$(which python3) \
-D PYTHON3_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
-D PYTHON3_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
-D WITH_GSTREAMER=ON \
-D BUILD_EXAMPLES=ON ..
RUN make -j$(nproc)
RUN make install
RUN ldconfig
WORKDIR /Yolov5_DeepSort_Pytorch
COPY . /Yolov5_DeepSort_Pytorch
RUN set -xe \
    && apt-get update \
    && apt-get install -y python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt 
CMD [ "python3","track.py" ]