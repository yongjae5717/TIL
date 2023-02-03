# FAT32
## 구조
- Boot Record
- FAT Area (Cluster Chain)
- Data Area (Directory Entry)
- Main 함수 및 동작확인

### Boot Record
![](images/BootRecord.png)

- Boot Record 정보: 0x60 bytes
- Bytes Per Sector(11~12): 저장장치의 입출력 단위 섹터 Byte 크기 (일반적으로 0x200)
- Sector Per Cluster(13): FAT32의 입출력 단위인 클러스터 섹터 수
- Cluster Size: Bytes Per Sector(11 ~ 12) * Sector Per Cluster
- Reserved Sector Count(14): Reserved Area 섹터 수
  - 이를 통하여 FAT #1 Offset을 구할 수 있다.
  - FAT #1 Offset = Reserved Sector Count(14) * Bytes Per Sector(11~12)
- Num of FAT(16): FAT의 개수 (주로 0x02)
  - FAT Area의 크기 계산시 사용된다.
- num_of_sector_FAT_area(36~39) : 한 FAT 내의 섹터 수
  - Num of FAT와 조합하여 FAT Area 크기 계산
    - FAT Area Size = Num of FAT(16) * (num_of_sector_FAT_area(36~39) * Bytes Per Sector(11~12))
  - Data Area Offset = FAT #1 Offset(FAT영역의 시작 주소) + FAT Area Size

<details>
<summary>Boot Record, Endian Class</summary>
<div>

- Boot Record.py
```python
```

- endian.py
```python
```
</div>
</details>

### FAT Area
![](images/FatArea.png)

- Data Area의 각 클러스터의 사용여부를 확인하기 위함
- 데이터가 여러 클러스터로 분할되어 저장되면 클러스터 체인으로 표현된다.
- FAT Entry 하나의 크기는 4Bytes
- 파일 바이트 데이터가 나눠진 상태로 분포하기 때문에 FAT Table을 이용하여 용이하게 사용하기 위함.

|Value|Description|
|---|---|
|0x0000000|할당되지 않은 클러스터|
|0x0000002 ~ 0xFFFFFEF|사용중인 클러스터이며, 클러스터 체인의 다음 클러스터 번호|
|0xFFFFFF0 ~ 0xFFFFFF6|Reserved 클러스터|
|0xFFFFFF7|사용할수없는 Bad Cluster|
|0xFFFFFF8 ~ 0xFFFFFFF| EOF|


<details>
<summary>Fat Class, Cluster Rule Class, Cluster Chain Class</summary>
<div>

- fat.py
```python
```

- cluster_rule.py
```python
```

- cluster_chain.py
```python
```

</div>
</details>

### Data Area
![](images/DataArea.png)

- File의 실제 데이터 저장 위치
- Directory인 경우 내부 File의 메타 데이터를 저장하는 Directory Entry 저장
- Directory Entry Size: 32 bytes

- File name: 0 ~ 7
- Extension: 8 ~ 10
- Attribute: 11

|Value|Description|
|---|---|
|0x01|Read Only|
|0x02|Hidden|
|0x04|System|
|0x08|Volume Label|
|0x0F|LFN(Long File Name)|
|0x10|Directory|
|0x20|Archive|
|0x40|Device|
|0x80|Reserved|

  - First Cluster High: 20 ~ 21
  - First Cluster Low: 26 ~ 27
  - First_cluster: First Cluster Low + First Cluster High의 리틀엔디안
  - File Size: 28 ~ 31 (디렉토리의 경우 항상 0, 최대 크기는 4GB)

<details>
<summary>DirFileRead Class, DirPrepare Class, FileManage Class, Node Class</summary>
<div>

- DirFileRead Class
```python
```

- DirPrepare Class
```python
```

- FileManage Class
```python
```

- Node Class (Node, Node Manage)
```python
```
</div>
</details>

### Main 함수 및 동작 확인
- 메인화면 실행(특정 경로파일만 가져오기)
  - 입력
![](images/input1.png)
  - 출력
![](images/output1.png)
  
- 메인화면 실행(전체 파일 가져오기)
  - 입력
![](images/input2.png)
  - 출력
![](images/output2.png)