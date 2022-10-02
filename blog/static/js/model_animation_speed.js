const modelViewer = document.querySelector('#model-object');
  
  const play = () => {
    modelViewer.timeScale = 1.5;
  };
  modelViewer.addEventListener('load', play);
