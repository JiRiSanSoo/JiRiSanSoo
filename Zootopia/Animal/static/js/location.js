// 1. 기본위치를 --카카오로 -- 설정 (필수)
var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
  mapOption = { 
    center: new kakao.maps.LatLng(0, 0), // 지도의 중심좌표
    level: 5 ,// 지도의 확대 레벨
}; 
var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();
// HTML5의 geolocation으로 사용할 수 있는지 확인합니다 (내 위치를 받아오기 위함)
if (navigator.geolocation) {
// GeoLocation을 이용해서 접속 위치를 얻어옵니다
navigator.geolocation.getCurrentPosition(function(position) {
    
    var lat = position.coords.latitude, // 위도
        lon = position.coords.longitude; // 경도
    var locPosition = new kakao.maps.LatLng(lat, lon) 
    // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
    // 마커와 인포윈도우를 표시합니다
    displayMarker(locPosition);
  });
} 

// 지도에 마커를 표시하는 함수입니다
function displayMarker(locPosition) {
// 마커를 생성합니다.
var marker = new kakao.maps.Marker({  
    map: map, 
}); 
// 지도 중심좌표를 접속위치로 변경합니다
map.setCenter(locPosition);      
}    


// 지도에 클릭 이벤트를 등록합니다
// 지도를 클릭하면 마지막 파라미터로 넘어온 함수를 호출합니다.



var marker = new kakao.maps.Marker({ 
  // 지도 중심좌표에 마커를 생성합니다 
  position: map.getCenter() 
}); 
// 지도에 마커를 표시합니다
marker.setMap(map);

kakao.maps.event.addListener(map, 'click', function(mouseEvent) {        
  // 클릭한 위도, 경도 정보를 가져옵니다 
  var latlng = mouseEvent.latLng; 
  // 마커 위치를 클릭한 위치로 옮깁니다
  marker.setPosition(latlng);

});

// 주소 가져오는 api

// 마지막 위치 저장하는 변수
let lastAddress = "위치";
let stringAddress = "";
// 서버로 넘기기 위해 주소 저장하는 임시 div
const addressContainer = document.querySelector("#address");
const latitudeContainer = document.querySelector("#latitude");
const longitudeContainer = document.querySelector("#longitude");
// 주소-좌표 변환 객체를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();
 // 클릭한 위치를 표시할 마커입니다
    infowindow = new kakao.maps.InfoWindow({zindex:1}); // 클릭한 위치에 대한 주소를 표시할 인포윈도우입니다

// 지도를 클릭했을 때 클릭 위치 좌표에 대한 주소정보를 표시하도록 이벤트를 등록합니다
kakao.maps.event.addListener(map, 'click', function(mouseEvent) {
    searchDetailAddrFromCoords(mouseEvent.latLng, function(result, status) {
        if (status === kakao.maps.services.Status.OK) {
            var detailAddr = !!result[0].road_address;
            detailAddr =result[0].address.address_name;
            
            var content = detailAddr
            
            // 마커를 클릭한 위치에 표시합니다 
            marker.setPosition(mouseEvent.latLng);
            marker.setMap(map);

            // 번지수를 제외한 주소 추출
            extractCity(content);

            addressContainer.value = stringAddress;
            latitudeContainer.value = mouseEvent.latLng.Ma;
            longitudeContainer.value = mouseEvent.latLng.La;
            // 인포윈도우에 클릭한 위치에 대한 법정동 상세 주소정보를 표시합니다
            infowindow.setContent(content);
            infowindow.open(map, marker);
        }   
    });
});

// 번지수를 제외한 주소 추출 메서드
function extractCity(content){
    // 띄어 주소 쓰기로 분리
    lastAddress = content.split(" ");
    // 마지막 세부 주소 삭제
    lastAddress.pop();
    // 산일 경우 산 삭제
    if(lastAddress[lastAddress.length-1]=="산"){
        lastAddress.pop();
    }
    //  배열 to 문자열
    stringAddress = lastAddress.join(" ");
}

// 중심 좌표나 확대 수준이 변경됐을 때 지도 중심 좌표에 대한 주소 정보를 표시하도록 이벤트를 등록합니다
kakao.maps.event.addListener(map, 'idle', function() {
    searchAddrFromCoords(map.getCenter(), displayCenterInfo);
});

function searchAddrFromCoords(coords, callback) {
    // 좌표로 행정동 주소 정보를 요청합니다
    geocoder.coord2RegionCode(coords.getLng(), coords.getLat(), callback);         
}

function searchDetailAddrFromCoords(coords, callback) {
    // 좌표로 법정동 상세 주소 정보를 요청합니다
    geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
}

// 지도 좌측상단에 지도 중심좌표에 대한 주소정보를 표출하는 함수입니다
function displayCenterInfo(result, status) {
    if (status === kakao.maps.services.Status.OK) {
        var infoDiv = document.getElementById('centerAddr');

        for(var i = 0; i < result.length; i++) {
            // 행정동의 region_type 값은 'H' 이므로
            if (result[i].region_type === 'H') {
                // infoDiv.innerHTML = result[i].address_name;
                break;
            }
        }
    }    
}