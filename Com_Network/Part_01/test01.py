'''
1-03 - 电路交换， 报文交换， 分组交换的优缺点？
    电路交换：由于电路交换在通信之前要在通信双方之间建立一条被双方独占的物理通路
        优点：
            1. 通信线路为通信双方用户专用， 数据直达， 传输数据时延非常小。
            2. 通信双方物理通路一旦建立， 可随时通信， 实时性强。
            3. 按发送顺序传送数据， 不存哎失序问题。
            4. 适用于模拟信号， 也适用于传输数字信号。
            5. 交换设备及控制较为简单。
        缺点：
            1. 电路交换的平均连接建立时间对计算机通信来说较长。
            2. 信道利用率低。
            3. 不同类型， 不同规格， 不同速率的终端很难相互通信， 难以进行差错控制。
    报文交换：报文交换是以报文为数据交换的单位， 报文携带目标地址， 源地址等， 采用存储转发的方式
        优点：
            1. 不需要专用通信线路， 不存在建立时延， 可随时发送报文。
            2. 具有较高的传输可靠性。
            3. 便于不同类型， 规格， 速度的通信。
            4. 一个报文可同时发送到多个目的地址。
            5. 可建立传输优先级。
            6. 通信线路利用率高。
        缺点：
            1. 实时性差， 不适合传送实时数据。
            2. 只适用于数字信号。
            3. 由于要等待转发的报文存在磁盘上， 增加了传送时延。
    分组交换：采用存储转发传输方式， 但将一个长报文分割为若干个较短的分组， 然后逐个发送
        优点：
            1. 加速了数据的传输。
            2. 简化了存储管理。
            3. 减少了出错几率和重发数据量。
            4. 分组小， 适用于优先级策略。
        缺点：
            1. 仍存在存储转发延时。
            2. 降低了通信效率， 增加了处理的时间， 控制复杂， 时延增加。
            3. 可能出现失序， 丢失， 重复分组等问题。

1-12 - 互联网的两大组成部分（边缘与核心部分）的特点是什么？工作方式各有什么特点？
    边缘部分：处在互联网边缘的部分就是所有主机。 利用核心部分提供的服务， 使众多主机质检部能够互相通信并交换信息或共享信息。
    核心部分：由路由器和网络组成。 向网络边缘的主机提供连通性， 使边缘部分的任何一个主机都能向其他主机通信。

1-13 - C/S 和 P2P 通信方式的区别？ 有无相同的地方？
    C/S严格区别服务和被服务者， P2P无此区别。P2P是前者的双向应用， P2P的每一台主机既是客户同时又是服务器。

1-14 - 计网有哪些常用的性能指标？
    速率， 带宽， 吞吐量， 时延， 时延带宽积， 往返时间， 利用率。

1-22 - 网络协议的三个要素是什么？各有什么含义？
    1. 语法：数据与控制信息的结构或格式。
    2. 语义：需要发出何种控制信息， 完成何种动作以及做出何种响应。
    3. 同步：事件实现顺序的详细说明。

1-24 - 五层协议的网络体系结构的要点， 各层的主要功能？
    1. 物理层：透明的传送比特流， 还要确定连接电缆插头的定义及连接法。
    2. 数据链路层：在两个相邻结点间的线路上无差错的传送一帧为单位的数据， 每一帧包括数据和必要的控制信息。
    3. 网络层：选择合适的路由， 使发送站的运输层所传下来的分组能够正确无误地按照地址找到目的站， 并交付给目的站的运输层。
    4. 运输层：向上一层进行通信的两个进程之间提供一个可靠的端到端服务， 使他们看不见运输层以下的数据通信的细节。
    5. 应用层：直接为用户的应用进程提供服务。

1-27 - 解释everything over IP 和 IP over everything？
    everything over IP：在TCP/IP体系结构下， 各种网络应用均是建立在IP基础之上。
    IP over everything：在TCP/IP体系结构下， IP通过网络接口层运行在不同的物理网络之上。
    
'''