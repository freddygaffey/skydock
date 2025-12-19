## seq
ERROR: Could not find attribute 'seq'

## file
ERROR: Could not find attribute 'file'

## srcSystem
ERROR: Could not find attribute 'srcSystem'

## srcComponent
ERROR: Could not find attribute 'srcComponent'

## callback
ERROR: Could not find attribute 'callback'

## callback_args
ERROR: Could not find attribute 'callback_args'

## callback_kwargs
ERROR: Could not find attribute 'callback_kwargs'

## send_callback
ERROR: Could not find attribute 'send_callback'

## send_callback_args
ERROR: Could not find attribute 'send_callback_args'

## send_callback_kwargs
ERROR: Could not find attribute 'send_callback_kwargs'

## buf
ERROR: Could not find attribute 'buf'

## buf_index
ERROR: Could not find attribute 'buf_index'

## expected_length
ERROR: Could not find attribute 'expected_length'

## have_prefix_error
ERROR: Could not find attribute 'have_prefix_error'

## robust_parsing
ERROR: Could not find attribute 'robust_parsing'

## protocol_marker
ERROR: Could not find attribute 'protocol_marker'

## little_endian
ERROR: Could not find attribute 'little_endian'

## crc_extra
ERROR: Could not find attribute 'crc_extra'

## sort_fields
ERROR: Could not find attribute 'sort_fields'

## total_packets_sent
ERROR: Could not find attribute 'total_packets_sent'

## total_bytes_sent
ERROR: Could not find attribute 'total_bytes_sent'

## total_packets_received
ERROR: Could not find attribute 'total_packets_received'

## total_bytes_received
ERROR: Could not find attribute 'total_bytes_received'

## total_receive_errors
ERROR: Could not find attribute 'total_receive_errors'

## startup_time
ERROR: Could not find attribute 'startup_time'

## signing
ERROR: Could not find attribute 'signing'

## mav20_unpacker
ERROR: Could not find attribute 'mav20_unpacker'

## mav10_unpacker
ERROR: Could not find attribute 'mav10_unpacker'

## mav20_h3_unpacker
ERROR: Could not find attribute 'mav20_h3_unpacker'

## mav_csum_unpacker
ERROR: Could not find attribute 'mav_csum_unpacker'

## mav_sign_unpacker
ERROR: Could not find attribute 'mav_sign_unpacker'

## __module__
Attribute type: str

## __doc__
Attribute type: str

## __init__
    def __init__(self, file: Any, srcSystem: int = 0, srcComponent: int = 0, use_native: bool = False) -> None:
        self.seq = 0
        self.file = file
        self.srcSystem = srcSystem
        self.srcComponent = srcComponent
        self.callback: Optional[Callable[..., None]] = None
        self.callback_args: Optional[Iterable[Any]] = None
        self.callback_kwargs: Optional[Mapping[str, Any]] = None
        self.send_callback: Optional[Callable[..., None]] = None
        self.send_callback_args: Optional[Iterable[Any]] = None
        self.send_callback_kwargs: Optional[Mapping[str, Any]] = None
        self.buf = bytearray()
        self.buf_index = 0
        self.expected_length = HEADER_LEN_V1 + 2
        self.have_prefix_error = False
        self.robust_parsing = False
        self.protocol_marker = 253
        self.little_endian = True
        self.crc_extra = True
        self.sort_fields = True
        self.total_packets_sent = 0
        self.total_bytes_sent = 0
        self.total_packets_received = 0
        self.total_bytes_received = 0
        self.total_receive_errors = 0
        self.startup_time = time.time()
        self.signing = MAVLinkSigning()
        self.mav20_unpacker = struct.Struct("<cBBBBBBHB")
        self.mav10_unpacker = struct.Struct("<cBBBBB")
        self.mav20_h3_unpacker = struct.Struct("BBB")
        self.mav_csum_unpacker = struct.Struct("<H")
        self.mav_sign_unpacker = struct.Struct("<IH")

## set_callback
    def set_callback(self, callback: Callable[..., None], *args: Any, **kwargs: Any) -> None:
        self.callback = callback
        self.callback_args = args
        self.callback_kwargs = kwargs

## set_send_callback
    def set_send_callback(self, callback: Callable[..., None], *args: Any, **kwargs: Any) -> None:
        self.send_callback = callback
        self.send_callback_args = args
        self.send_callback_kwargs = kwargs

## send
    def send(self, mavmsg: MAVLink_message, force_mavlink1: bool = False) -> None:
        """send a MAVLink message"""
        buf = mavmsg.pack(self, force_mavlink1=force_mavlink1)
        self.file.write(buf)
        self.seq = (self.seq + 1) % 256
        self.total_packets_sent += 1
        self.total_bytes_sent += len(buf)
        if self.send_callback is not None and self.send_callback_args is not None and self.send_callback_kwargs is not None:
            self.send_callback(mavmsg, *self.send_callback_args, **self.send_callback_kwargs)

## buf_len
    def buf_len(self) -> int:
        return len(self.buf) - self.buf_index

## bytes_needed
    def bytes_needed(self) -> int:
        """return number of bytes needed for next parsing stage"""
        ret = self.expected_length - self.buf_len()

        if ret <= 0:
            return 1
        return ret

## _MAVLink__callbacks
    def __callbacks(self, msg: MAVLink_message) -> None:
        """this method exists only to make profiling results easier to read"""
        if self.callback is not None and self.callback_args is not None and self.callback_kwargs is not None:
            self.callback(msg, *self.callback_args, **self.callback_kwargs)

## parse_char
    def parse_char(self, c: Sequence[int]) -> Optional[MAVLink_message]:
        """input some data bytes, possibly returning a new message"""
        self.buf.extend(c)

        self.total_bytes_received += len(c)

        m = self.__parse_char_legacy()

        if m is not None:
            self.total_packets_received += 1
            self.__callbacks(m)
        else:
            # XXX The idea here is if we've read something and there's nothing left in
            # the buffer, reset it to 0 which frees the memory
            if self.buf_len() == 0 and self.buf_index != 0:
                self.buf = bytearray()
                self.buf_index = 0

        return m

## _MAVLink__parse_char_legacy
    def __parse_char_legacy(self) -> Optional[MAVLink_message]:
        """input some data bytes, possibly returning a new message"""
        header_len = HEADER_LEN_V1
        if self.buf_len() >= 1 and self.buf[self.buf_index] == PROTOCOL_MARKER_V2:
            header_len = HEADER_LEN_V2

        m: Optional[MAVLink_message] = None
        if self.buf_len() >= 1 and self.buf[self.buf_index] != PROTOCOL_MARKER_V1 and self.buf[self.buf_index] != PROTOCOL_MARKER_V2:
            magic = self.buf[self.buf_index]
            self.buf_index += 1
            if self.robust_parsing:
                invalid_prefix_start = self.buf_index - 1
                while self.buf_len() >= 1 and self.buf[self.buf_index] != PROTOCOL_MARKER_V1 and self.buf[self.buf_index] != PROTOCOL_MARKER_V2:
                    self.buf_index += 1
                m = MAVLink_bad_data(self.buf[invalid_prefix_start : self.buf_index], "Bad prefix")
                self.expected_length = header_len + 2
                self.total_receive_errors += 1
                return m
            if self.have_prefix_error:
                return None
            self.have_prefix_error = True
            self.total_receive_errors += 1
            raise MAVError("invalid MAVLink prefix '%s'" % magic)
        self.have_prefix_error = False
        if self.buf_len() >= 3:
            sbuf = self.buf[self.buf_index : 3 + self.buf_index]
            unpacked_h3: Tuple[int, int, int] = self.mav20_h3_unpacker.unpack(sbuf)
            magic, self.expected_length, incompat_flags = unpacked_h3
            if magic == PROTOCOL_MARKER_V2 and (incompat_flags & MAVLINK_IFLAG_SIGNED):
                self.expected_length += MAVLINK_SIGNATURE_BLOCK_LEN
            self.expected_length += header_len + 2
        if self.expected_length >= (header_len + 2) and self.buf_len() >= self.expected_length:
            mbuf = self.buf[self.buf_index : self.buf_index + self.expected_length]
            self.buf_index += self.expected_length
            self.expected_length = header_len + 2
            if self.robust_parsing:
                try:
                    if magic == PROTOCOL_MARKER_V2 and (incompat_flags & ~MAVLINK_IFLAG_SIGNED) != 0:
                        raise MAVError("invalid incompat_flags 0x%x 0x%x %u" % (incompat_flags, magic, self.expected_length))
                    m = self.decode(mbuf)
                except MAVError as reason:
                    m = MAVLink_bad_data(mbuf, reason.message)
                    self.total_receive_errors += 1
            else:
                if magic == PROTOCOL_MARKER_V2 and (incompat_flags & ~MAVLINK_IFLAG_SIGNED) != 0:
                    raise MAVError("invalid incompat_flags 0x%x 0x%x %u" % (incompat_flags, magic, self.expected_length))
                m = self.decode(mbuf)
            return m
        return None

## parse_buffer
    def parse_buffer(self, s: Sequence[int]) -> Optional[List[MAVLink_message]]:
        """input some data bytes, possibly returning a list of new messages"""
        m = self.parse_char(s)
        if m is None:
            return None
        ret = [m]
        while True:
            m = self.parse_char(b"")
            if m is None:
                return ret
            ret.append(m)

## check_signature
    def check_signature(self, msgbuf: bytearray, srcSystem: int, srcComponent: int) -> bool:
        """check signature on incoming message"""
        assert self.signing.secret_key is not None

        timestamp_buf = msgbuf[-12:-6]
        link_id = msgbuf[-13]
        tbytes: Tuple[int, int] = self.mav_sign_unpacker.unpack(timestamp_buf)
        tlow, thigh = tbytes
        timestamp = tlow + (thigh << 32)

        # see if the timestamp is acceptable
        stream_key = (link_id, srcSystem, srcComponent)
        if stream_key in self.signing.stream_timestamps:
            if timestamp <= self.signing.stream_timestamps[stream_key]:
                # reject old timestamp
                logger.info("old timestamp")
                return False
        else:
            # a new stream has appeared. Accept the timestamp if it is at most
            # one minute behind our current timestamp
            if timestamp + 6000 * 1000 < self.signing.timestamp:
                logger.info("bad new stream %s %s", timestamp / (100.0 * 1000 * 60 * 60 * 24 * 365), self.signing.timestamp / (100.0 * 1000 * 60 * 60 * 24 * 365))
                return False
            logger.info("new stream")

        # set the streams timestamp so we reject timestamps that go backwards
        self.signing.stream_timestamps[stream_key] = timestamp

        h = hashlib.new("sha256")
        h.update(self.signing.secret_key)
        h.update(msgbuf[:-6])
        sig1 = h.digest()[:6]
        sig2 = msgbuf[-6:]
        if sig1 != sig2:
            logger.info("sig mismatch")
            return False

        # the timestamp we next send with is the max of the received timestamp and
        # our current timestamp
        self.signing.timestamp = max(self.signing.timestamp, timestamp)
        return True

## decode
    def decode(self, msgbuf: bytearray) -> MAVLink_message:
        """decode a buffer as a MAVLink message"""
        # decode the header
        if msgbuf[0] != PROTOCOL_MARKER_V1:
            headerlen = 10
            try:
                header_v2: MAVLinkV2Header = self.mav20_unpacker.unpack(msgbuf[:headerlen])
            except struct.error as emsg:
                raise MAVError("Unable to unpack MAVLink header: %s" % emsg)
            magic, mlen, incompat_flags, compat_flags, seq, srcSystem, srcComponent, msgIdlow, msgIdhigh = header_v2
            msgId = msgIdlow | (msgIdhigh << 16)
        else:
            headerlen = 6
            try:
                header_v1: MAVLinkV1Header = self.mav10_unpacker.unpack(msgbuf[:headerlen])
            except struct.error as emsg:
                raise MAVError("Unable to unpack MAVLink header: %s" % emsg)
            magic, mlen, seq, srcSystem, srcComponent, msgId = header_v1
            incompat_flags = 0
            compat_flags = 0
        mapkey = msgId
        if (incompat_flags & MAVLINK_IFLAG_SIGNED) != 0:
            signature_len = MAVLINK_SIGNATURE_BLOCK_LEN
        else:
            signature_len = 0

        if ord(magic) != PROTOCOL_MARKER_V1 and ord(magic) != PROTOCOL_MARKER_V2:
            raise MAVError("invalid MAVLink prefix '{}'".format(hex(ord(magic))))
        if mlen != len(msgbuf) - (headerlen + 2 + signature_len):
            raise MAVError("invalid MAVLink message length. Got %u expected %u, msgId=%u headerlen=%u" % (len(msgbuf) - (headerlen + 2 + signature_len), mlen, msgId, headerlen))

        if mapkey not in mavlink_map:
            return MAVLink_unknown(msgId, msgbuf)

        # decode the payload
        msgtype = mavlink_map[mapkey]
        order_map = msgtype.orders
        len_map = msgtype.lengths
        crc_extra = msgtype.crc_extra

        # decode the checksum
        try:
            crc: int = self.mav_csum_unpacker.unpack(msgbuf[-(2 + signature_len) :][:2])[0]
        except struct.error as emsg:
            raise MAVError("Unable to unpack MAVLink CRC: %s" % emsg)
        crcbuf = msgbuf[1 : -(2 + signature_len)]
        if True:
            # using CRC extra
            crcbuf.append(crc_extra)
        crc2 = x25crc(crcbuf)
        if crc != crc2.crc and not MAVLINK_IGNORE_CRC:
            raise MAVError("invalid MAVLink CRC in msgID %u 0x%04x should be 0x%04x" % (msgId, crc, crc2.crc))

        sig_ok = False
        if signature_len == MAVLINK_SIGNATURE_BLOCK_LEN:
            self.signing.sig_count += 1
        if self.signing.secret_key is not None:
            accept_signature = False
            if signature_len == MAVLINK_SIGNATURE_BLOCK_LEN:
                sig_ok = self.check_signature(msgbuf, srcSystem, srcComponent)
                accept_signature = sig_ok
                if sig_ok:
                    self.signing.goodsig_count += 1
                else:
                    self.signing.badsig_count += 1
                if not accept_signature and self.signing.allow_unsigned_callback is not None:
                    accept_signature = self.signing.allow_unsigned_callback(self, msgId)
                    if accept_signature:
                        self.signing.unsigned_count += 1
                    else:
                        self.signing.reject_count += 1
            elif self.signing.allow_unsigned_callback is not None:
                accept_signature = self.signing.allow_unsigned_callback(self, msgId)
                if accept_signature:
                    self.signing.unsigned_count += 1
                else:
                    self.signing.reject_count += 1
            if not accept_signature:
                raise MAVError("Invalid signature")

        csize = msgtype.unpacker.size
        mbuf = msgbuf[headerlen : -(2 + signature_len)]
        if len(mbuf) < csize:
            # zero pad to give right size
            mbuf.extend([0] * (csize - len(mbuf)))
        if len(mbuf) < csize:
            raise MAVError("Bad message of type %s length %u needs %s" % (msgtype, len(mbuf), csize))
        mbuf = mbuf[:csize]
        try:
            t: Tuple[Union[bytes, int, float], ...] = msgtype.unpacker.unpack(mbuf)
        except struct.error as emsg:
            raise MAVError("Unable to unpack MAVLink payload type=%s payloadLength=%u: %s" % (msgtype, len(mbuf), emsg))

        tlist: List[Union[bytes, float, int, Sequence[Union[bytes, float, int]]]] = list(t)
        # handle sorted fields
        if True:
            if sum(len_map) == len(len_map):
                # message has no arrays in it
                for i in range(0, len(tlist)):
                    tlist[i] = t[order_map[i]]
            else:
                # message has some arrays
                tlist = []
                for i in range(0, len(order_map)):
                    order = order_map[i]
                    L = len_map[order]
                    tip = sum(len_map[:order])
                    field = t[tip]
                    if L == 1 or isinstance(field, bytes):
                        tlist.append(field)
                    else:
                        tlist.append(list(t[tip : (tip + L)]))

        # terminate any strings
        for i, elem in enumerate(tlist):
            if isinstance(elem, bytes):
                tlist[i] = elem.rstrip(b"\x00")

        # construct the message object
        try:
            # Note that initializers don't follow the Liskov Substitution Principle
            # therefore it can't be typechecked
            m = msgtype(*tlist)  # type: ignore
        except Exception as emsg:
            raise MAVError("Unable to instantiate MAVLink message of type %s : %s" % (msgtype, emsg))
        m._signed = sig_ok
        if m._signed:
            m._link_id = msgbuf[-13]
        m._msgbuf = msgbuf
        m._payload = msgbuf[6 : -(2 + signature_len)]
        m._crc = crc
        m._header = MAVLink_header(msgId, incompat_flags, compat_flags, mlen, seq, srcSystem, srcComponent)
        return m

## sensor_offsets_encode
    def sensor_offsets_encode(self, mag_ofs_x: int, mag_ofs_y: int, mag_ofs_z: int, mag_declination: float, raw_press: int, raw_temp: int, gyro_cal_x: float, gyro_cal_y: float, gyro_cal_z: float, accel_cal_x: float, accel_cal_y: float, accel_cal_z: float) -> MAVLink_sensor_offsets_message:
        """
        Offsets and calibrations values for hardware sensors. This makes it
        easier to debug the calibration process.

        mag_ofs_x                 : Magnetometer X offset. (type:int16_t)
        mag_ofs_y                 : Magnetometer Y offset. (type:int16_t)
        mag_ofs_z                 : Magnetometer Z offset. (type:int16_t)
        mag_declination           : Magnetic declination. [rad] (type:float)
        raw_press                 : Raw pressure from barometer. (type:int32_t)
        raw_temp                  : Raw temperature from barometer. (type:int32_t)
        gyro_cal_x                : Gyro X calibration. (type:float)
        gyro_cal_y                : Gyro Y calibration. (type:float)
        gyro_cal_z                : Gyro Z calibration. (type:float)
        accel_cal_x               : Accel X calibration. (type:float)
        accel_cal_y               : Accel Y calibration. (type:float)
        accel_cal_z               : Accel Z calibration. (type:float)

        """
        return MAVLink_sensor_offsets_message(mag_ofs_x, mag_ofs_y, mag_ofs_z, mag_declination, raw_press, raw_temp, gyro_cal_x, gyro_cal_y, gyro_cal_z, accel_cal_x, accel_cal_y, accel_cal_z)

## sensor_offsets_send
    def sensor_offsets_send(self, mag_ofs_x: int, mag_ofs_y: int, mag_ofs_z: int, mag_declination: float, raw_press: int, raw_temp: int, gyro_cal_x: float, gyro_cal_y: float, gyro_cal_z: float, accel_cal_x: float, accel_cal_y: float, accel_cal_z: float, force_mavlink1: bool = False) -> None:
        """
        Offsets and calibrations values for hardware sensors. This makes it
        easier to debug the calibration process.

        mag_ofs_x                 : Magnetometer X offset. (type:int16_t)
        mag_ofs_y                 : Magnetometer Y offset. (type:int16_t)
        mag_ofs_z                 : Magnetometer Z offset. (type:int16_t)
        mag_declination           : Magnetic declination. [rad] (type:float)
        raw_press                 : Raw pressure from barometer. (type:int32_t)
        raw_temp                  : Raw temperature from barometer. (type:int32_t)
        gyro_cal_x                : Gyro X calibration. (type:float)
        gyro_cal_y                : Gyro Y calibration. (type:float)
        gyro_cal_z                : Gyro Z calibration. (type:float)
        accel_cal_x               : Accel X calibration. (type:float)
        accel_cal_y               : Accel Y calibration. (type:float)
        accel_cal_z               : Accel Z calibration. (type:float)

        """
        self.send(self.sensor_offsets_encode(mag_ofs_x, mag_ofs_y, mag_ofs_z, mag_declination, raw_press, raw_temp, gyro_cal_x, gyro_cal_y, gyro_cal_z, accel_cal_x, accel_cal_y, accel_cal_z), force_mavlink1=force_mavlink1)

## set_mag_offsets_encode
    def set_mag_offsets_encode(self, target_system: int, target_component: int, mag_ofs_x: int, mag_ofs_y: int, mag_ofs_z: int) -> MAVLink_set_mag_offsets_message:
        """
        Set the magnetometer offsets

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        mag_ofs_x                 : Magnetometer X offset. (type:int16_t)
        mag_ofs_y                 : Magnetometer Y offset. (type:int16_t)
        mag_ofs_z                 : Magnetometer Z offset. (type:int16_t)

        """
        return MAVLink_set_mag_offsets_message(target_system, target_component, mag_ofs_x, mag_ofs_y, mag_ofs_z)

## set_mag_offsets_send
    def set_mag_offsets_send(self, target_system: int, target_component: int, mag_ofs_x: int, mag_ofs_y: int, mag_ofs_z: int, force_mavlink1: bool = False) -> None:
        """
        Set the magnetometer offsets

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        mag_ofs_x                 : Magnetometer X offset. (type:int16_t)
        mag_ofs_y                 : Magnetometer Y offset. (type:int16_t)
        mag_ofs_z                 : Magnetometer Z offset. (type:int16_t)

        """
        self.send(self.set_mag_offsets_encode(target_system, target_component, mag_ofs_x, mag_ofs_y, mag_ofs_z), force_mavlink1=force_mavlink1)

## meminfo_encode
    def meminfo_encode(self, brkval: int, freemem: int, freemem32: int = 0) -> MAVLink_meminfo_message:
        """
        State of autopilot RAM.

        brkval                    : Heap top. (type:uint16_t)
        freemem                   : Free memory. [bytes] (type:uint16_t)
        freemem32                 : Free memory (32 bit). [bytes] (type:uint32_t)

        """
        return MAVLink_meminfo_message(brkval, freemem, freemem32)

## meminfo_send
    def meminfo_send(self, brkval: int, freemem: int, freemem32: int = 0, force_mavlink1: bool = False) -> None:
        """
        State of autopilot RAM.

        brkval                    : Heap top. (type:uint16_t)
        freemem                   : Free memory. [bytes] (type:uint16_t)
        freemem32                 : Free memory (32 bit). [bytes] (type:uint32_t)

        """
        self.send(self.meminfo_encode(brkval, freemem, freemem32), force_mavlink1=force_mavlink1)

## ap_adc_encode
    def ap_adc_encode(self, adc1: int, adc2: int, adc3: int, adc4: int, adc5: int, adc6: int) -> MAVLink_ap_adc_message:
        """
        Raw ADC output.

        adc1                      : ADC output 1. (type:uint16_t)
        adc2                      : ADC output 2. (type:uint16_t)
        adc3                      : ADC output 3. (type:uint16_t)
        adc4                      : ADC output 4. (type:uint16_t)
        adc5                      : ADC output 5. (type:uint16_t)
        adc6                      : ADC output 6. (type:uint16_t)

        """
        return MAVLink_ap_adc_message(adc1, adc2, adc3, adc4, adc5, adc6)

## ap_adc_send
    def ap_adc_send(self, adc1: int, adc2: int, adc3: int, adc4: int, adc5: int, adc6: int, force_mavlink1: bool = False) -> None:
        """
        Raw ADC output.

        adc1                      : ADC output 1. (type:uint16_t)
        adc2                      : ADC output 2. (type:uint16_t)
        adc3                      : ADC output 3. (type:uint16_t)
        adc4                      : ADC output 4. (type:uint16_t)
        adc5                      : ADC output 5. (type:uint16_t)
        adc6                      : ADC output 6. (type:uint16_t)

        """
        self.send(self.ap_adc_encode(adc1, adc2, adc3, adc4, adc5, adc6), force_mavlink1=force_mavlink1)

## digicam_configure_encode
    def digicam_configure_encode(self, target_system: int, target_component: int, mode: int, shutter_speed: int, aperture: int, iso: int, exposure_type: int, command_id: int, engine_cut_off: int, extra_param: int, extra_value: float) -> MAVLink_digicam_configure_message:
        """
        Configure on-board Camera Control System.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        mode                      : Mode enumeration from 1 to N //P, TV, AV, M, etc. (0 means ignore). (type:uint8_t)
        shutter_speed             : Divisor number //e.g. 1000 means 1/1000 (0 means ignore). (type:uint16_t)
        aperture                  : F stop number x 10 //e.g. 28 means 2.8 (0 means ignore). (type:uint8_t)
        iso                       : ISO enumeration from 1 to N //e.g. 80, 100, 200, Etc (0 means ignore). (type:uint8_t)
        exposure_type             : Exposure type enumeration from 1 to N (0 means ignore). (type:uint8_t)
        command_id                : Command Identity (incremental loop: 0 to 255). //A command sent multiple times will be executed or pooled just once. (type:uint8_t)
        engine_cut_off            : Main engine cut-off time before camera trigger (0 means no cut-off). [ds] (type:uint8_t)
        extra_param               : Extra parameters enumeration (0 means ignore). (type:uint8_t)
        extra_value               : Correspondent value to given extra_param. (type:float)

        """
        return MAVLink_digicam_configure_message(target_system, target_component, mode, shutter_speed, aperture, iso, exposure_type, command_id, engine_cut_off, extra_param, extra_value)

## digicam_configure_send
    def digicam_configure_send(self, target_system: int, target_component: int, mode: int, shutter_speed: int, aperture: int, iso: int, exposure_type: int, command_id: int, engine_cut_off: int, extra_param: int, extra_value: float, force_mavlink1: bool = False) -> None:
        """
        Configure on-board Camera Control System.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        mode                      : Mode enumeration from 1 to N //P, TV, AV, M, etc. (0 means ignore). (type:uint8_t)
        shutter_speed             : Divisor number //e.g. 1000 means 1/1000 (0 means ignore). (type:uint16_t)
        aperture                  : F stop number x 10 //e.g. 28 means 2.8 (0 means ignore). (type:uint8_t)
        iso                       : ISO enumeration from 1 to N //e.g. 80, 100, 200, Etc (0 means ignore). (type:uint8_t)
        exposure_type             : Exposure type enumeration from 1 to N (0 means ignore). (type:uint8_t)
        command_id                : Command Identity (incremental loop: 0 to 255). //A command sent multiple times will be executed or pooled just once. (type:uint8_t)
        engine_cut_off            : Main engine cut-off time before camera trigger (0 means no cut-off). [ds] (type:uint8_t)
        extra_param               : Extra parameters enumeration (0 means ignore). (type:uint8_t)
        extra_value               : Correspondent value to given extra_param. (type:float)

        """
        self.send(self.digicam_configure_encode(target_system, target_component, mode, shutter_speed, aperture, iso, exposure_type, command_id, engine_cut_off, extra_param, extra_value), force_mavlink1=force_mavlink1)

## digicam_control_encode
    def digicam_control_encode(self, target_system: int, target_component: int, session: int, zoom_pos: int, zoom_step: int, focus_lock: int, shot: int, command_id: int, extra_param: int, extra_value: float) -> MAVLink_digicam_control_message:
        """
        Control on-board Camera Control System to take shots.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        session                   : 0: stop, 1: start or keep it up //Session control e.g. show/hide lens. (type:uint8_t)
        zoom_pos                  : 1 to N //Zoom's absolute position (0 means ignore). (type:uint8_t)
        zoom_step                 : -100 to 100 //Zooming step value to offset zoom from the current position. (type:int8_t)
        focus_lock                : 0: unlock focus or keep unlocked, 1: lock focus or keep locked, 3: re-lock focus. (type:uint8_t)
        shot                      : 0: ignore, 1: shot or start filming. (type:uint8_t)
        command_id                : Command Identity (incremental loop: 0 to 255)//A command sent multiple times will be executed or pooled just once. (type:uint8_t)
        extra_param               : Extra parameters enumeration (0 means ignore). (type:uint8_t)
        extra_value               : Correspondent value to given extra_param. (type:float)

        """
        return MAVLink_digicam_control_message(target_system, target_component, session, zoom_pos, zoom_step, focus_lock, shot, command_id, extra_param, extra_value)

## digicam_control_send
    def digicam_control_send(self, target_system: int, target_component: int, session: int, zoom_pos: int, zoom_step: int, focus_lock: int, shot: int, command_id: int, extra_param: int, extra_value: float, force_mavlink1: bool = False) -> None:
        """
        Control on-board Camera Control System to take shots.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        session                   : 0: stop, 1: start or keep it up //Session control e.g. show/hide lens. (type:uint8_t)
        zoom_pos                  : 1 to N //Zoom's absolute position (0 means ignore). (type:uint8_t)
        zoom_step                 : -100 to 100 //Zooming step value to offset zoom from the current position. (type:int8_t)
        focus_lock                : 0: unlock focus or keep unlocked, 1: lock focus or keep locked, 3: re-lock focus. (type:uint8_t)
        shot                      : 0: ignore, 1: shot or start filming. (type:uint8_t)
        command_id                : Command Identity (incremental loop: 0 to 255)//A command sent multiple times will be executed or pooled just once. (type:uint8_t)
        extra_param               : Extra parameters enumeration (0 means ignore). (type:uint8_t)
        extra_value               : Correspondent value to given extra_param. (type:float)

        """
        self.send(self.digicam_control_encode(target_system, target_component, session, zoom_pos, zoom_step, focus_lock, shot, command_id, extra_param, extra_value), force_mavlink1=force_mavlink1)

## mount_configure_encode
    def mount_configure_encode(self, target_system: int, target_component: int, mount_mode: int, stab_roll: int, stab_pitch: int, stab_yaw: int) -> MAVLink_mount_configure_message:
        """
        Message to configure a camera mount, directional antenna, etc.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        mount_mode                : Mount operating mode. (type:uint8_t, values:MAV_MOUNT_MODE)
        stab_roll                 : (1 = yes, 0 = no). (type:uint8_t)
        stab_pitch                : (1 = yes, 0 = no). (type:uint8_t)
        stab_yaw                  : (1 = yes, 0 = no). (type:uint8_t)

        """
        return MAVLink_mount_configure_message(target_system, target_component, mount_mode, stab_roll, stab_pitch, stab_yaw)

## mount_configure_send
    def mount_configure_send(self, target_system: int, target_component: int, mount_mode: int, stab_roll: int, stab_pitch: int, stab_yaw: int, force_mavlink1: bool = False) -> None:
        """
        Message to configure a camera mount, directional antenna, etc.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        mount_mode                : Mount operating mode. (type:uint8_t, values:MAV_MOUNT_MODE)
        stab_roll                 : (1 = yes, 0 = no). (type:uint8_t)
        stab_pitch                : (1 = yes, 0 = no). (type:uint8_t)
        stab_yaw                  : (1 = yes, 0 = no). (type:uint8_t)

        """
        self.send(self.mount_configure_encode(target_system, target_component, mount_mode, stab_roll, stab_pitch, stab_yaw), force_mavlink1=force_mavlink1)

## mount_control_encode
    def mount_control_encode(self, target_system: int, target_component: int, input_a: int, input_b: int, input_c: int, save_position: int) -> MAVLink_mount_control_message:
        """
        Message to control a camera mount, directional antenna, etc.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        input_a                   : Pitch (centi-degrees) or lat (degE7), depending on mount mode. (type:int32_t)
        input_b                   : Roll (centi-degrees) or lon (degE7) depending on mount mode. (type:int32_t)
        input_c                   : Yaw (centi-degrees) or alt (cm) depending on mount mode. (type:int32_t)
        save_position             : If "1" it will save current trimmed position on EEPROM (just valid for NEUTRAL and LANDING). (type:uint8_t)

        """
        return MAVLink_mount_control_message(target_system, target_component, input_a, input_b, input_c, save_position)

## mount_control_send
    def mount_control_send(self, target_system: int, target_component: int, input_a: int, input_b: int, input_c: int, save_position: int, force_mavlink1: bool = False) -> None:
        """
        Message to control a camera mount, directional antenna, etc.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        input_a                   : Pitch (centi-degrees) or lat (degE7), depending on mount mode. (type:int32_t)
        input_b                   : Roll (centi-degrees) or lon (degE7) depending on mount mode. (type:int32_t)
        input_c                   : Yaw (centi-degrees) or alt (cm) depending on mount mode. (type:int32_t)
        save_position             : If "1" it will save current trimmed position on EEPROM (just valid for NEUTRAL and LANDING). (type:uint8_t)

        """
        self.send(self.mount_control_encode(target_system, target_component, input_a, input_b, input_c, save_position), force_mavlink1=force_mavlink1)

## mount_status_encode
    def mount_status_encode(self, target_system: int, target_component: int, pointing_a: int, pointing_b: int, pointing_c: int, mount_mode: int = 0) -> MAVLink_mount_status_message:
        """
        Message with some status from autopilot to GCS about camera or antenna
        mount.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        pointing_a                : Pitch. [cdeg] (type:int32_t)
        pointing_b                : Roll. [cdeg] (type:int32_t)
        pointing_c                : Yaw. [cdeg] (type:int32_t)
        mount_mode                : Mount operating mode. (type:uint8_t, values:MAV_MOUNT_MODE)

        """
        return MAVLink_mount_status_message(target_system, target_component, pointing_a, pointing_b, pointing_c, mount_mode)

## mount_status_send
    def mount_status_send(self, target_system: int, target_component: int, pointing_a: int, pointing_b: int, pointing_c: int, mount_mode: int = 0, force_mavlink1: bool = False) -> None:
        """
        Message with some status from autopilot to GCS about camera or antenna
        mount.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        pointing_a                : Pitch. [cdeg] (type:int32_t)
        pointing_b                : Roll. [cdeg] (type:int32_t)
        pointing_c                : Yaw. [cdeg] (type:int32_t)
        mount_mode                : Mount operating mode. (type:uint8_t, values:MAV_MOUNT_MODE)

        """
        self.send(self.mount_status_encode(target_system, target_component, pointing_a, pointing_b, pointing_c, mount_mode), force_mavlink1=force_mavlink1)

## fence_point_encode
    def fence_point_encode(self, target_system: int, target_component: int, idx: int, count: int, lat: float, lng: float) -> MAVLink_fence_point_message:
        """
        A fence point. Used to set a point when from GCS -> MAV. Also used to
        return a point from MAV -> GCS.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        idx                       : Point index (first point is 1, 0 is for return point). (type:uint8_t)
        count                     : Total number of points (for sanity checking). (type:uint8_t)
        lat                       : Latitude of point. [deg] (type:float)
        lng                       : Longitude of point. [deg] (type:float)

        """
        return MAVLink_fence_point_message(target_system, target_component, idx, count, lat, lng)

## fence_point_send
    def fence_point_send(self, target_system: int, target_component: int, idx: int, count: int, lat: float, lng: float, force_mavlink1: bool = False) -> None:
        """
        A fence point. Used to set a point when from GCS -> MAV. Also used to
        return a point from MAV -> GCS.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        idx                       : Point index (first point is 1, 0 is for return point). (type:uint8_t)
        count                     : Total number of points (for sanity checking). (type:uint8_t)
        lat                       : Latitude of point. [deg] (type:float)
        lng                       : Longitude of point. [deg] (type:float)

        """
        self.send(self.fence_point_encode(target_system, target_component, idx, count, lat, lng), force_mavlink1=force_mavlink1)

## fence_fetch_point_encode
    def fence_fetch_point_encode(self, target_system: int, target_component: int, idx: int) -> MAVLink_fence_fetch_point_message:
        """
        Request a current fence point from MAV.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        idx                       : Point index (first point is 1, 0 is for return point). (type:uint8_t)

        """
        return MAVLink_fence_fetch_point_message(target_system, target_component, idx)

## fence_fetch_point_send
    def fence_fetch_point_send(self, target_system: int, target_component: int, idx: int, force_mavlink1: bool = False) -> None:
        """
        Request a current fence point from MAV.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        idx                       : Point index (first point is 1, 0 is for return point). (type:uint8_t)

        """
        self.send(self.fence_fetch_point_encode(target_system, target_component, idx), force_mavlink1=force_mavlink1)

## ahrs_encode
    def ahrs_encode(self, omegaIx: float, omegaIy: float, omegaIz: float, accel_weight: float, renorm_val: float, error_rp: float, error_yaw: float) -> MAVLink_ahrs_message:
        """
        Status of DCM attitude estimator.

        omegaIx                   : X gyro drift estimate. [rad/s] (type:float)
        omegaIy                   : Y gyro drift estimate. [rad/s] (type:float)
        omegaIz                   : Z gyro drift estimate. [rad/s] (type:float)
        accel_weight              : Average accel_weight. (type:float)
        renorm_val                : Average renormalisation value. (type:float)
        error_rp                  : Average error_roll_pitch value. (type:float)
        error_yaw                 : Average error_yaw value. (type:float)

        """
        return MAVLink_ahrs_message(omegaIx, omegaIy, omegaIz, accel_weight, renorm_val, error_rp, error_yaw)

## ahrs_send
    def ahrs_send(self, omegaIx: float, omegaIy: float, omegaIz: float, accel_weight: float, renorm_val: float, error_rp: float, error_yaw: float, force_mavlink1: bool = False) -> None:
        """
        Status of DCM attitude estimator.

        omegaIx                   : X gyro drift estimate. [rad/s] (type:float)
        omegaIy                   : Y gyro drift estimate. [rad/s] (type:float)
        omegaIz                   : Z gyro drift estimate. [rad/s] (type:float)
        accel_weight              : Average accel_weight. (type:float)
        renorm_val                : Average renormalisation value. (type:float)
        error_rp                  : Average error_roll_pitch value. (type:float)
        error_yaw                 : Average error_yaw value. (type:float)

        """
        self.send(self.ahrs_encode(omegaIx, omegaIy, omegaIz, accel_weight, renorm_val, error_rp, error_yaw), force_mavlink1=force_mavlink1)

## simstate_encode
    def simstate_encode(self, roll: float, pitch: float, yaw: float, xacc: float, yacc: float, zacc: float, xgyro: float, ygyro: float, zgyro: float, lat: int, lng: int) -> MAVLink_simstate_message:
        """
        Status of simulation environment, if used.

        roll                      : Roll angle. [rad] (type:float)
        pitch                     : Pitch angle. [rad] (type:float)
        yaw                       : Yaw angle. [rad] (type:float)
        xacc                      : X acceleration. [m/s/s] (type:float)
        yacc                      : Y acceleration. [m/s/s] (type:float)
        zacc                      : Z acceleration. [m/s/s] (type:float)
        xgyro                     : Angular speed around X axis. [rad/s] (type:float)
        ygyro                     : Angular speed around Y axis. [rad/s] (type:float)
        zgyro                     : Angular speed around Z axis. [rad/s] (type:float)
        lat                       : Latitude. [degE7] (type:int32_t)
        lng                       : Longitude. [degE7] (type:int32_t)

        """
        return MAVLink_simstate_message(roll, pitch, yaw, xacc, yacc, zacc, xgyro, ygyro, zgyro, lat, lng)

## simstate_send
    def simstate_send(self, roll: float, pitch: float, yaw: float, xacc: float, yacc: float, zacc: float, xgyro: float, ygyro: float, zgyro: float, lat: int, lng: int, force_mavlink1: bool = False) -> None:
        """
        Status of simulation environment, if used.

        roll                      : Roll angle. [rad] (type:float)
        pitch                     : Pitch angle. [rad] (type:float)
        yaw                       : Yaw angle. [rad] (type:float)
        xacc                      : X acceleration. [m/s/s] (type:float)
        yacc                      : Y acceleration. [m/s/s] (type:float)
        zacc                      : Z acceleration. [m/s/s] (type:float)
        xgyro                     : Angular speed around X axis. [rad/s] (type:float)
        ygyro                     : Angular speed around Y axis. [rad/s] (type:float)
        zgyro                     : Angular speed around Z axis. [rad/s] (type:float)
        lat                       : Latitude. [degE7] (type:int32_t)
        lng                       : Longitude. [degE7] (type:int32_t)

        """
        self.send(self.simstate_encode(roll, pitch, yaw, xacc, yacc, zacc, xgyro, ygyro, zgyro, lat, lng), force_mavlink1=force_mavlink1)

## hwstatus_encode
    def hwstatus_encode(self, Vcc: int, I2Cerr: int) -> MAVLink_hwstatus_message:
        """
        Status of key hardware.

        Vcc                       : Board voltage. [mV] (type:uint16_t)
        I2Cerr                    : I2C error count. (type:uint8_t)

        """
        return MAVLink_hwstatus_message(Vcc, I2Cerr)

## hwstatus_send
    def hwstatus_send(self, Vcc: int, I2Cerr: int, force_mavlink1: bool = False) -> None:
        """
        Status of key hardware.

        Vcc                       : Board voltage. [mV] (type:uint16_t)
        I2Cerr                    : I2C error count. (type:uint8_t)

        """
        self.send(self.hwstatus_encode(Vcc, I2Cerr), force_mavlink1=force_mavlink1)

## radio_encode
    def radio_encode(self, rssi: int, remrssi: int, txbuf: int, noise: int, remnoise: int, rxerrors: int, fixed: int) -> MAVLink_radio_message:
        """
        Status generated by radio.

        rssi                      : Local signal strength. (type:uint8_t)
        remrssi                   : Remote signal strength. (type:uint8_t)
        txbuf                     : How full the tx buffer is. [%] (type:uint8_t)
        noise                     : Background noise level. (type:uint8_t)
        remnoise                  : Remote background noise level. (type:uint8_t)
        rxerrors                  : Receive errors. (type:uint16_t)
        fixed                     : Count of error corrected packets. (type:uint16_t)

        """
        return MAVLink_radio_message(rssi, remrssi, txbuf, noise, remnoise, rxerrors, fixed)

## radio_send
    def radio_send(self, rssi: int, remrssi: int, txbuf: int, noise: int, remnoise: int, rxerrors: int, fixed: int, force_mavlink1: bool = False) -> None:
        """
        Status generated by radio.

        rssi                      : Local signal strength. (type:uint8_t)
        remrssi                   : Remote signal strength. (type:uint8_t)
        txbuf                     : How full the tx buffer is. [%] (type:uint8_t)
        noise                     : Background noise level. (type:uint8_t)
        remnoise                  : Remote background noise level. (type:uint8_t)
        rxerrors                  : Receive errors. (type:uint16_t)
        fixed                     : Count of error corrected packets. (type:uint16_t)

        """
        self.send(self.radio_encode(rssi, remrssi, txbuf, noise, remnoise, rxerrors, fixed), force_mavlink1=force_mavlink1)

## limits_status_encode
    def limits_status_encode(self, limits_state: int, last_trigger: int, last_action: int, last_recovery: int, last_clear: int, breach_count: int, mods_enabled: int, mods_required: int, mods_triggered: int) -> MAVLink_limits_status_message:
        """
        Status of AP_Limits. Sent in extended status stream when AP_Limits is
        enabled.

        limits_state              : State of AP_Limits. (type:uint8_t, values:LIMITS_STATE)
        last_trigger              : Time (since boot) of last breach. [ms] (type:uint32_t)
        last_action               : Time (since boot) of last recovery action. [ms] (type:uint32_t)
        last_recovery             : Time (since boot) of last successful recovery. [ms] (type:uint32_t)
        last_clear                : Time (since boot) of last all-clear. [ms] (type:uint32_t)
        breach_count              : Number of fence breaches. (type:uint16_t)
        mods_enabled              : AP_Limit_Module bitfield of enabled modules. (type:uint8_t, values:LIMIT_MODULE)
        mods_required             : AP_Limit_Module bitfield of required modules. (type:uint8_t, values:LIMIT_MODULE)
        mods_triggered            : AP_Limit_Module bitfield of triggered modules. (type:uint8_t, values:LIMIT_MODULE)

        """
        return MAVLink_limits_status_message(limits_state, last_trigger, last_action, last_recovery, last_clear, breach_count, mods_enabled, mods_required, mods_triggered)

## limits_status_send
    def limits_status_send(self, limits_state: int, last_trigger: int, last_action: int, last_recovery: int, last_clear: int, breach_count: int, mods_enabled: int, mods_required: int, mods_triggered: int, force_mavlink1: bool = False) -> None:
        """
        Status of AP_Limits. Sent in extended status stream when AP_Limits is
        enabled.

        limits_state              : State of AP_Limits. (type:uint8_t, values:LIMITS_STATE)
        last_trigger              : Time (since boot) of last breach. [ms] (type:uint32_t)
        last_action               : Time (since boot) of last recovery action. [ms] (type:uint32_t)
        last_recovery             : Time (since boot) of last successful recovery. [ms] (type:uint32_t)
        last_clear                : Time (since boot) of last all-clear. [ms] (type:uint32_t)
        breach_count              : Number of fence breaches. (type:uint16_t)
        mods_enabled              : AP_Limit_Module bitfield of enabled modules. (type:uint8_t, values:LIMIT_MODULE)
        mods_required             : AP_Limit_Module bitfield of required modules. (type:uint8_t, values:LIMIT_MODULE)
        mods_triggered            : AP_Limit_Module bitfield of triggered modules. (type:uint8_t, values:LIMIT_MODULE)

        """
        self.send(self.limits_status_encode(limits_state, last_trigger, last_action, last_recovery, last_clear, breach_count, mods_enabled, mods_required, mods_triggered), force_mavlink1=force_mavlink1)

## wind_encode
    def wind_encode(self, direction: float, speed: float, speed_z: float) -> MAVLink_wind_message:
        """
        Wind estimation.

        direction                 : Wind direction (that wind is coming from). [deg] (type:float)
        speed                     : Wind speed in ground plane. [m/s] (type:float)
        speed_z                   : Vertical wind speed. [m/s] (type:float)

        """
        return MAVLink_wind_message(direction, speed, speed_z)

## wind_send
    def wind_send(self, direction: float, speed: float, speed_z: float, force_mavlink1: bool = False) -> None:
        """
        Wind estimation.

        direction                 : Wind direction (that wind is coming from). [deg] (type:float)
        speed                     : Wind speed in ground plane. [m/s] (type:float)
        speed_z                   : Vertical wind speed. [m/s] (type:float)

        """
        self.send(self.wind_encode(direction, speed, speed_z), force_mavlink1=force_mavlink1)

## data16_encode
    def data16_encode(self, type: int, len: int, data: Sequence[int]) -> MAVLink_data16_message:
        """
        Data packet, size 16.

        type                      : Data type. (type:uint8_t)
        len                       : Data length. [bytes] (type:uint8_t)
        data                      : Raw data. (type:uint8_t)

        """
        return MAVLink_data16_message(type, len, data)

## data16_send
    def data16_send(self, type: int, len: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Data packet, size 16.

        type                      : Data type. (type:uint8_t)
        len                       : Data length. [bytes] (type:uint8_t)
        data                      : Raw data. (type:uint8_t)

        """
        self.send(self.data16_encode(type, len, data), force_mavlink1=force_mavlink1)

## data32_encode
    def data32_encode(self, type: int, len: int, data: Sequence[int]) -> MAVLink_data32_message:
        """
        Data packet, size 32.

        type                      : Data type. (type:uint8_t)
        len                       : Data length. [bytes] (type:uint8_t)
        data                      : Raw data. (type:uint8_t)

        """
        return MAVLink_data32_message(type, len, data)

## data32_send
    def data32_send(self, type: int, len: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Data packet, size 32.

        type                      : Data type. (type:uint8_t)
        len                       : Data length. [bytes] (type:uint8_t)
        data                      : Raw data. (type:uint8_t)

        """
        self.send(self.data32_encode(type, len, data), force_mavlink1=force_mavlink1)

## data64_encode
    def data64_encode(self, type: int, len: int, data: Sequence[int]) -> MAVLink_data64_message:
        """
        Data packet, size 64.

        type                      : Data type. (type:uint8_t)
        len                       : Data length. [bytes] (type:uint8_t)
        data                      : Raw data. (type:uint8_t)

        """
        return MAVLink_data64_message(type, len, data)

## data64_send
    def data64_send(self, type: int, len: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Data packet, size 64.

        type                      : Data type. (type:uint8_t)
        len                       : Data length. [bytes] (type:uint8_t)
        data                      : Raw data. (type:uint8_t)

        """
        self.send(self.data64_encode(type, len, data), force_mavlink1=force_mavlink1)

## data96_encode
    def data96_encode(self, type: int, len: int, data: Sequence[int]) -> MAVLink_data96_message:
        """
        Data packet, size 96.

        type                      : Data type. (type:uint8_t)
        len                       : Data length. [bytes] (type:uint8_t)
        data                      : Raw data. (type:uint8_t)

        """
        return MAVLink_data96_message(type, len, data)

## data96_send
    def data96_send(self, type: int, len: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Data packet, size 96.

        type                      : Data type. (type:uint8_t)
        len                       : Data length. [bytes] (type:uint8_t)
        data                      : Raw data. (type:uint8_t)

        """
        self.send(self.data96_encode(type, len, data), force_mavlink1=force_mavlink1)

## rangefinder_encode
    def rangefinder_encode(self, distance: float, voltage: float) -> MAVLink_rangefinder_message:
        """
        Rangefinder reporting.

        distance                  : Distance. [m] (type:float)
        voltage                   : Raw voltage if available, zero otherwise. [V] (type:float)

        """
        return MAVLink_rangefinder_message(distance, voltage)

## rangefinder_send
    def rangefinder_send(self, distance: float, voltage: float, force_mavlink1: bool = False) -> None:
        """
        Rangefinder reporting.

        distance                  : Distance. [m] (type:float)
        voltage                   : Raw voltage if available, zero otherwise. [V] (type:float)

        """
        self.send(self.rangefinder_encode(distance, voltage), force_mavlink1=force_mavlink1)

## airspeed_autocal_encode
    def airspeed_autocal_encode(self, vx: float, vy: float, vz: float, diff_pressure: float, EAS2TAS: float, ratio: float, state_x: float, state_y: float, state_z: float, Pax: float, Pby: float, Pcz: float) -> MAVLink_airspeed_autocal_message:
        """
        Airspeed auto-calibration.

        vx                        : GPS velocity north. [m/s] (type:float)
        vy                        : GPS velocity east. [m/s] (type:float)
        vz                        : GPS velocity down. [m/s] (type:float)
        diff_pressure             : Differential pressure. [Pa] (type:float)
        EAS2TAS                   : Estimated to true airspeed ratio. (type:float)
        ratio                     : Airspeed ratio. (type:float)
        state_x                   : EKF state x. (type:float)
        state_y                   : EKF state y. (type:float)
        state_z                   : EKF state z. (type:float)
        Pax                       : EKF Pax. (type:float)
        Pby                       : EKF Pby. (type:float)
        Pcz                       : EKF Pcz. (type:float)

        """
        return MAVLink_airspeed_autocal_message(vx, vy, vz, diff_pressure, EAS2TAS, ratio, state_x, state_y, state_z, Pax, Pby, Pcz)

## airspeed_autocal_send
    def airspeed_autocal_send(self, vx: float, vy: float, vz: float, diff_pressure: float, EAS2TAS: float, ratio: float, state_x: float, state_y: float, state_z: float, Pax: float, Pby: float, Pcz: float, force_mavlink1: bool = False) -> None:
        """
        Airspeed auto-calibration.

        vx                        : GPS velocity north. [m/s] (type:float)
        vy                        : GPS velocity east. [m/s] (type:float)
        vz                        : GPS velocity down. [m/s] (type:float)
        diff_pressure             : Differential pressure. [Pa] (type:float)
        EAS2TAS                   : Estimated to true airspeed ratio. (type:float)
        ratio                     : Airspeed ratio. (type:float)
        state_x                   : EKF state x. (type:float)
        state_y                   : EKF state y. (type:float)
        state_z                   : EKF state z. (type:float)
        Pax                       : EKF Pax. (type:float)
        Pby                       : EKF Pby. (type:float)
        Pcz                       : EKF Pcz. (type:float)

        """
        self.send(self.airspeed_autocal_encode(vx, vy, vz, diff_pressure, EAS2TAS, ratio, state_x, state_y, state_z, Pax, Pby, Pcz), force_mavlink1=force_mavlink1)

## rally_point_encode
    def rally_point_encode(self, target_system: int, target_component: int, idx: int, count: int, lat: int, lng: int, alt: int, break_alt: int, land_dir: int, flags: int) -> MAVLink_rally_point_message:
        """
        A rally point. Used to set a point when from GCS -> MAV. Also used to
        return a point from MAV -> GCS.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        idx                       : Point index (first point is 0). (type:uint8_t)
        count                     : Total number of points (for sanity checking). (type:uint8_t)
        lat                       : Latitude of point. [degE7] (type:int32_t)
        lng                       : Longitude of point. [degE7] (type:int32_t)
        alt                       : Transit / loiter altitude relative to home. [m] (type:int16_t)
        break_alt                 : Break altitude relative to home. [m] (type:int16_t)
        land_dir                  : Heading to aim for when landing. [cdeg] (type:uint16_t)
        flags                     : Configuration flags. (type:uint8_t, values:RALLY_FLAGS)

        """
        return MAVLink_rally_point_message(target_system, target_component, idx, count, lat, lng, alt, break_alt, land_dir, flags)

## rally_point_send
    def rally_point_send(self, target_system: int, target_component: int, idx: int, count: int, lat: int, lng: int, alt: int, break_alt: int, land_dir: int, flags: int, force_mavlink1: bool = False) -> None:
        """
        A rally point. Used to set a point when from GCS -> MAV. Also used to
        return a point from MAV -> GCS.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        idx                       : Point index (first point is 0). (type:uint8_t)
        count                     : Total number of points (for sanity checking). (type:uint8_t)
        lat                       : Latitude of point. [degE7] (type:int32_t)
        lng                       : Longitude of point. [degE7] (type:int32_t)
        alt                       : Transit / loiter altitude relative to home. [m] (type:int16_t)
        break_alt                 : Break altitude relative to home. [m] (type:int16_t)
        land_dir                  : Heading to aim for when landing. [cdeg] (type:uint16_t)
        flags                     : Configuration flags. (type:uint8_t, values:RALLY_FLAGS)

        """
        self.send(self.rally_point_encode(target_system, target_component, idx, count, lat, lng, alt, break_alt, land_dir, flags), force_mavlink1=force_mavlink1)

## rally_fetch_point_encode
    def rally_fetch_point_encode(self, target_system: int, target_component: int, idx: int) -> MAVLink_rally_fetch_point_message:
        """
        Request a current rally point from MAV. MAV should respond with a
        RALLY_POINT message. MAV should not respond if the request is
        invalid.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        idx                       : Point index (first point is 0). (type:uint8_t)

        """
        return MAVLink_rally_fetch_point_message(target_system, target_component, idx)

## rally_fetch_point_send
    def rally_fetch_point_send(self, target_system: int, target_component: int, idx: int, force_mavlink1: bool = False) -> None:
        """
        Request a current rally point from MAV. MAV should respond with a
        RALLY_POINT message. MAV should not respond if the request is
        invalid.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        idx                       : Point index (first point is 0). (type:uint8_t)

        """
        self.send(self.rally_fetch_point_encode(target_system, target_component, idx), force_mavlink1=force_mavlink1)

## compassmot_status_encode
    def compassmot_status_encode(self, throttle: int, current: float, interference: int, CompensationX: float, CompensationY: float, CompensationZ: float) -> MAVLink_compassmot_status_message:
        """
        Status of compassmot calibration.

        throttle                  : Throttle. [d%] (type:uint16_t)
        current                   : Current. [A] (type:float)
        interference              : Interference. [%] (type:uint16_t)
        CompensationX             : Motor Compensation X. (type:float)
        CompensationY             : Motor Compensation Y. (type:float)
        CompensationZ             : Motor Compensation Z. (type:float)

        """
        return MAVLink_compassmot_status_message(throttle, current, interference, CompensationX, CompensationY, CompensationZ)

## compassmot_status_send
    def compassmot_status_send(self, throttle: int, current: float, interference: int, CompensationX: float, CompensationY: float, CompensationZ: float, force_mavlink1: bool = False) -> None:
        """
        Status of compassmot calibration.

        throttle                  : Throttle. [d%] (type:uint16_t)
        current                   : Current. [A] (type:float)
        interference              : Interference. [%] (type:uint16_t)
        CompensationX             : Motor Compensation X. (type:float)
        CompensationY             : Motor Compensation Y. (type:float)
        CompensationZ             : Motor Compensation Z. (type:float)

        """
        self.send(self.compassmot_status_encode(throttle, current, interference, CompensationX, CompensationY, CompensationZ), force_mavlink1=force_mavlink1)

## ahrs2_encode
    def ahrs2_encode(self, roll: float, pitch: float, yaw: float, altitude: float, lat: int, lng: int) -> MAVLink_ahrs2_message:
        """
        Status of secondary AHRS filter if available.

        roll                      : Roll angle. [rad] (type:float)
        pitch                     : Pitch angle. [rad] (type:float)
        yaw                       : Yaw angle. [rad] (type:float)
        altitude                  : Altitude (MSL). [m] (type:float)
        lat                       : Latitude. [degE7] (type:int32_t)
        lng                       : Longitude. [degE7] (type:int32_t)

        """
        return MAVLink_ahrs2_message(roll, pitch, yaw, altitude, lat, lng)

## ahrs2_send
    def ahrs2_send(self, roll: float, pitch: float, yaw: float, altitude: float, lat: int, lng: int, force_mavlink1: bool = False) -> None:
        """
        Status of secondary AHRS filter if available.

        roll                      : Roll angle. [rad] (type:float)
        pitch                     : Pitch angle. [rad] (type:float)
        yaw                       : Yaw angle. [rad] (type:float)
        altitude                  : Altitude (MSL). [m] (type:float)
        lat                       : Latitude. [degE7] (type:int32_t)
        lng                       : Longitude. [degE7] (type:int32_t)

        """
        self.send(self.ahrs2_encode(roll, pitch, yaw, altitude, lat, lng), force_mavlink1=force_mavlink1)

## camera_status_encode
    def camera_status_encode(self, time_usec: int, target_system: int, cam_idx: int, img_idx: int, event_id: int, p1: float, p2: float, p3: float, p4: float) -> MAVLink_camera_status_message:
        """
        Camera Event.

        time_usec                 : Image timestamp (since UNIX epoch, according to camera clock). [us] (type:uint64_t)
        target_system             : System ID. (type:uint8_t)
        cam_idx                   : Camera ID. (type:uint8_t)
        img_idx                   : Image index. (type:uint16_t)
        event_id                  : Event type. (type:uint8_t, values:CAMERA_STATUS_TYPES)
        p1                        : Parameter 1 (meaning depends on event_id, see CAMERA_STATUS_TYPES enum). (type:float)
        p2                        : Parameter 2 (meaning depends on event_id, see CAMERA_STATUS_TYPES enum). (type:float)
        p3                        : Parameter 3 (meaning depends on event_id, see CAMERA_STATUS_TYPES enum). (type:float)
        p4                        : Parameter 4 (meaning depends on event_id, see CAMERA_STATUS_TYPES enum). (type:float)

        """
        return MAVLink_camera_status_message(time_usec, target_system, cam_idx, img_idx, event_id, p1, p2, p3, p4)

## camera_status_send
    def camera_status_send(self, time_usec: int, target_system: int, cam_idx: int, img_idx: int, event_id: int, p1: float, p2: float, p3: float, p4: float, force_mavlink1: bool = False) -> None:
        """
        Camera Event.

        time_usec                 : Image timestamp (since UNIX epoch, according to camera clock). [us] (type:uint64_t)
        target_system             : System ID. (type:uint8_t)
        cam_idx                   : Camera ID. (type:uint8_t)
        img_idx                   : Image index. (type:uint16_t)
        event_id                  : Event type. (type:uint8_t, values:CAMERA_STATUS_TYPES)
        p1                        : Parameter 1 (meaning depends on event_id, see CAMERA_STATUS_TYPES enum). (type:float)
        p2                        : Parameter 2 (meaning depends on event_id, see CAMERA_STATUS_TYPES enum). (type:float)
        p3                        : Parameter 3 (meaning depends on event_id, see CAMERA_STATUS_TYPES enum). (type:float)
        p4                        : Parameter 4 (meaning depends on event_id, see CAMERA_STATUS_TYPES enum). (type:float)

        """
        self.send(self.camera_status_encode(time_usec, target_system, cam_idx, img_idx, event_id, p1, p2, p3, p4), force_mavlink1=force_mavlink1)

## camera_feedback_encode
    def camera_feedback_encode(self, time_usec: int, target_system: int, cam_idx: int, img_idx: int, lat: int, lng: int, alt_msl: float, alt_rel: float, roll: float, pitch: float, yaw: float, foc_len: float, flags: int, completed_captures: int = 0) -> MAVLink_camera_feedback_message:
        """
        Camera Capture Feedback.

        time_usec                 : Image timestamp (since UNIX epoch), as passed in by CAMERA_STATUS message (or autopilot if no CCB). [us] (type:uint64_t)
        target_system             : System ID. (type:uint8_t)
        cam_idx                   : Camera ID. (type:uint8_t)
        img_idx                   : Image index. (type:uint16_t)
        lat                       : Latitude. [degE7] (type:int32_t)
        lng                       : Longitude. [degE7] (type:int32_t)
        alt_msl                   : Altitude (MSL). [m] (type:float)
        alt_rel                   : Altitude (Relative to HOME location). [m] (type:float)
        roll                      : Camera Roll angle (earth frame, +-180). [deg] (type:float)
        pitch                     : Camera Pitch angle (earth frame, +-180). [deg] (type:float)
        yaw                       : Camera Yaw (earth frame, 0-360, true). [deg] (type:float)
        foc_len                   : Focal Length. [mm] (type:float)
        flags                     : Feedback flags. (type:uint8_t, values:CAMERA_FEEDBACK_FLAGS)
        completed_captures        : Completed image captures. (type:uint16_t)

        """
        return MAVLink_camera_feedback_message(time_usec, target_system, cam_idx, img_idx, lat, lng, alt_msl, alt_rel, roll, pitch, yaw, foc_len, flags, completed_captures)

## camera_feedback_send
    def camera_feedback_send(self, time_usec: int, target_system: int, cam_idx: int, img_idx: int, lat: int, lng: int, alt_msl: float, alt_rel: float, roll: float, pitch: float, yaw: float, foc_len: float, flags: int, completed_captures: int = 0, force_mavlink1: bool = False) -> None:
        """
        Camera Capture Feedback.

        time_usec                 : Image timestamp (since UNIX epoch), as passed in by CAMERA_STATUS message (or autopilot if no CCB). [us] (type:uint64_t)
        target_system             : System ID. (type:uint8_t)
        cam_idx                   : Camera ID. (type:uint8_t)
        img_idx                   : Image index. (type:uint16_t)
        lat                       : Latitude. [degE7] (type:int32_t)
        lng                       : Longitude. [degE7] (type:int32_t)
        alt_msl                   : Altitude (MSL). [m] (type:float)
        alt_rel                   : Altitude (Relative to HOME location). [m] (type:float)
        roll                      : Camera Roll angle (earth frame, +-180). [deg] (type:float)
        pitch                     : Camera Pitch angle (earth frame, +-180). [deg] (type:float)
        yaw                       : Camera Yaw (earth frame, 0-360, true). [deg] (type:float)
        foc_len                   : Focal Length. [mm] (type:float)
        flags                     : Feedback flags. (type:uint8_t, values:CAMERA_FEEDBACK_FLAGS)
        completed_captures        : Completed image captures. (type:uint16_t)

        """
        self.send(self.camera_feedback_encode(time_usec, target_system, cam_idx, img_idx, lat, lng, alt_msl, alt_rel, roll, pitch, yaw, foc_len, flags, completed_captures), force_mavlink1=force_mavlink1)

## battery2_encode
    def battery2_encode(self, voltage: int, current_battery: int) -> MAVLink_battery2_message:
        """
        2nd Battery status

        voltage                   : Voltage. [mV] (type:uint16_t)
        current_battery           : Battery current, -1: autopilot does not measure the current. [cA] (type:int16_t)

        """
        return MAVLink_battery2_message(voltage, current_battery)

## battery2_send
    def battery2_send(self, voltage: int, current_battery: int, force_mavlink1: bool = False) -> None:
        """
        2nd Battery status

        voltage                   : Voltage. [mV] (type:uint16_t)
        current_battery           : Battery current, -1: autopilot does not measure the current. [cA] (type:int16_t)

        """
        self.send(self.battery2_encode(voltage, current_battery), force_mavlink1=force_mavlink1)

## ahrs3_encode
    def ahrs3_encode(self, roll: float, pitch: float, yaw: float, altitude: float, lat: int, lng: int, v1: float, v2: float, v3: float, v4: float) -> MAVLink_ahrs3_message:
        """
        Status of third AHRS filter if available. This is for ANU research
        group (Ali and Sean).

        roll                      : Roll angle. [rad] (type:float)
        pitch                     : Pitch angle. [rad] (type:float)
        yaw                       : Yaw angle. [rad] (type:float)
        altitude                  : Altitude (MSL). [m] (type:float)
        lat                       : Latitude. [degE7] (type:int32_t)
        lng                       : Longitude. [degE7] (type:int32_t)
        v1                        : Test variable1. (type:float)
        v2                        : Test variable2. (type:float)
        v3                        : Test variable3. (type:float)
        v4                        : Test variable4. (type:float)

        """
        return MAVLink_ahrs3_message(roll, pitch, yaw, altitude, lat, lng, v1, v2, v3, v4)

## ahrs3_send
    def ahrs3_send(self, roll: float, pitch: float, yaw: float, altitude: float, lat: int, lng: int, v1: float, v2: float, v3: float, v4: float, force_mavlink1: bool = False) -> None:
        """
        Status of third AHRS filter if available. This is for ANU research
        group (Ali and Sean).

        roll                      : Roll angle. [rad] (type:float)
        pitch                     : Pitch angle. [rad] (type:float)
        yaw                       : Yaw angle. [rad] (type:float)
        altitude                  : Altitude (MSL). [m] (type:float)
        lat                       : Latitude. [degE7] (type:int32_t)
        lng                       : Longitude. [degE7] (type:int32_t)
        v1                        : Test variable1. (type:float)
        v2                        : Test variable2. (type:float)
        v3                        : Test variable3. (type:float)
        v4                        : Test variable4. (type:float)

        """
        self.send(self.ahrs3_encode(roll, pitch, yaw, altitude, lat, lng, v1, v2, v3, v4), force_mavlink1=force_mavlink1)

## autopilot_version_request_encode
    def autopilot_version_request_encode(self, target_system: int, target_component: int) -> MAVLink_autopilot_version_request_message:
        """
        Request the autopilot version from the system/component.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)

        """
        return MAVLink_autopilot_version_request_message(target_system, target_component)

## autopilot_version_request_send
    def autopilot_version_request_send(self, target_system: int, target_component: int, force_mavlink1: bool = False) -> None:
        """
        Request the autopilot version from the system/component.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)

        """
        self.send(self.autopilot_version_request_encode(target_system, target_component), force_mavlink1=force_mavlink1)

## remote_log_data_block_encode
    def remote_log_data_block_encode(self, target_system: int, target_component: int, seqno: int, data: Sequence[int]) -> MAVLink_remote_log_data_block_message:
        """
        Send a block of log data to remote location.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        seqno                     : Log data block sequence number. (type:uint32_t, values:MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS)
        data                      : Log data block. (type:uint8_t)

        """
        return MAVLink_remote_log_data_block_message(target_system, target_component, seqno, data)

## remote_log_data_block_send
    def remote_log_data_block_send(self, target_system: int, target_component: int, seqno: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Send a block of log data to remote location.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        seqno                     : Log data block sequence number. (type:uint32_t, values:MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS)
        data                      : Log data block. (type:uint8_t)

        """
        self.send(self.remote_log_data_block_encode(target_system, target_component, seqno, data), force_mavlink1=force_mavlink1)

## remote_log_block_status_encode
    def remote_log_block_status_encode(self, target_system: int, target_component: int, seqno: int, status: int) -> MAVLink_remote_log_block_status_message:
        """
        Send Status of each log block that autopilot board might have sent.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        seqno                     : Log data block sequence number. (type:uint32_t)
        status                    : Log data block status. (type:uint8_t, values:MAV_REMOTE_LOG_DATA_BLOCK_STATUSES)

        """
        return MAVLink_remote_log_block_status_message(target_system, target_component, seqno, status)

## remote_log_block_status_send
    def remote_log_block_status_send(self, target_system: int, target_component: int, seqno: int, status: int, force_mavlink1: bool = False) -> None:
        """
        Send Status of each log block that autopilot board might have sent.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        seqno                     : Log data block sequence number. (type:uint32_t)
        status                    : Log data block status. (type:uint8_t, values:MAV_REMOTE_LOG_DATA_BLOCK_STATUSES)

        """
        self.send(self.remote_log_block_status_encode(target_system, target_component, seqno, status), force_mavlink1=force_mavlink1)

## led_control_encode
    def led_control_encode(self, target_system: int, target_component: int, instance: int, pattern: int, custom_len: int, custom_bytes: Sequence[int]) -> MAVLink_led_control_message:
        """
        Control vehicle LEDs.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        instance                  : Instance (LED instance to control or 255 for all LEDs). (type:uint8_t)
        pattern                   : Pattern (see LED_PATTERN_ENUM). (type:uint8_t)
        custom_len                : Custom Byte Length. (type:uint8_t)
        custom_bytes              : Custom Bytes. (type:uint8_t)

        """
        return MAVLink_led_control_message(target_system, target_component, instance, pattern, custom_len, custom_bytes)

## led_control_send
    def led_control_send(self, target_system: int, target_component: int, instance: int, pattern: int, custom_len: int, custom_bytes: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Control vehicle LEDs.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        instance                  : Instance (LED instance to control or 255 for all LEDs). (type:uint8_t)
        pattern                   : Pattern (see LED_PATTERN_ENUM). (type:uint8_t)
        custom_len                : Custom Byte Length. (type:uint8_t)
        custom_bytes              : Custom Bytes. (type:uint8_t)

        """
        self.send(self.led_control_encode(target_system, target_component, instance, pattern, custom_len, custom_bytes), force_mavlink1=force_mavlink1)

## mag_cal_progress_encode
    def mag_cal_progress_encode(self, compass_id: int, cal_mask: int, cal_status: int, attempt: int, completion_pct: int, completion_mask: Sequence[int], direction_x: float, direction_y: float, direction_z: float) -> MAVLink_mag_cal_progress_message:
        """
        Reports progress of compass calibration.

        compass_id                : Compass being calibrated. (type:uint8_t)
        cal_mask                  : Bitmask of compasses being calibrated. (type:uint8_t)
        cal_status                : Calibration Status. (type:uint8_t, values:MAG_CAL_STATUS)
        attempt                   : Attempt number. (type:uint8_t)
        completion_pct            : Completion percentage. [%] (type:uint8_t)
        completion_mask           : Bitmask of sphere sections (see http://en.wikipedia.org/wiki/Geodesic_grid). (type:uint8_t)
        direction_x               : Body frame direction vector for display. (type:float)
        direction_y               : Body frame direction vector for display. (type:float)
        direction_z               : Body frame direction vector for display. (type:float)

        """
        return MAVLink_mag_cal_progress_message(compass_id, cal_mask, cal_status, attempt, completion_pct, completion_mask, direction_x, direction_y, direction_z)

## mag_cal_progress_send
    def mag_cal_progress_send(self, compass_id: int, cal_mask: int, cal_status: int, attempt: int, completion_pct: int, completion_mask: Sequence[int], direction_x: float, direction_y: float, direction_z: float, force_mavlink1: bool = False) -> None:
        """
        Reports progress of compass calibration.

        compass_id                : Compass being calibrated. (type:uint8_t)
        cal_mask                  : Bitmask of compasses being calibrated. (type:uint8_t)
        cal_status                : Calibration Status. (type:uint8_t, values:MAG_CAL_STATUS)
        attempt                   : Attempt number. (type:uint8_t)
        completion_pct            : Completion percentage. [%] (type:uint8_t)
        completion_mask           : Bitmask of sphere sections (see http://en.wikipedia.org/wiki/Geodesic_grid). (type:uint8_t)
        direction_x               : Body frame direction vector for display. (type:float)
        direction_y               : Body frame direction vector for display. (type:float)
        direction_z               : Body frame direction vector for display. (type:float)

        """
        self.send(self.mag_cal_progress_encode(compass_id, cal_mask, cal_status, attempt, completion_pct, completion_mask, direction_x, direction_y, direction_z), force_mavlink1=force_mavlink1)

## ekf_status_report_encode
    def ekf_status_report_encode(self, flags: int, velocity_variance: float, pos_horiz_variance: float, pos_vert_variance: float, compass_variance: float, terrain_alt_variance: float, airspeed_variance: float = 0) -> MAVLink_ekf_status_report_message:
        """
        EKF Status message including flags and variances.

        flags                     : Flags. (type:uint16_t, values:EKF_STATUS_FLAGS)
        velocity_variance         : Velocity variance. (type:float)
        pos_horiz_variance        : Horizontal Position variance. (type:float)
        pos_vert_variance         : Vertical Position variance. (type:float)
        compass_variance          : Compass variance. (type:float)
        terrain_alt_variance        : Terrain Altitude variance. (type:float)
        airspeed_variance         : Airspeed variance. (type:float)

        """
        return MAVLink_ekf_status_report_message(flags, velocity_variance, pos_horiz_variance, pos_vert_variance, compass_variance, terrain_alt_variance, airspeed_variance)

## ekf_status_report_send
    def ekf_status_report_send(self, flags: int, velocity_variance: float, pos_horiz_variance: float, pos_vert_variance: float, compass_variance: float, terrain_alt_variance: float, airspeed_variance: float = 0, force_mavlink1: bool = False) -> None:
        """
        EKF Status message including flags and variances.

        flags                     : Flags. (type:uint16_t, values:EKF_STATUS_FLAGS)
        velocity_variance         : Velocity variance. (type:float)
        pos_horiz_variance        : Horizontal Position variance. (type:float)
        pos_vert_variance         : Vertical Position variance. (type:float)
        compass_variance          : Compass variance. (type:float)
        terrain_alt_variance        : Terrain Altitude variance. (type:float)
        airspeed_variance         : Airspeed variance. (type:float)

        """
        self.send(self.ekf_status_report_encode(flags, velocity_variance, pos_horiz_variance, pos_vert_variance, compass_variance, terrain_alt_variance, airspeed_variance), force_mavlink1=force_mavlink1)

## pid_tuning_encode
    def pid_tuning_encode(self, axis: int, desired: float, achieved: float, FF: float, P: float, I: float, D: float, SRate: float = 0, PDmod: float = 0) -> MAVLink_pid_tuning_message:
        """
        PID tuning information.

        axis                      : Axis. (type:uint8_t, values:PID_TUNING_AXIS)
        desired                   : Desired rate. (type:float)
        achieved                  : Achieved rate. (type:float)
        FF                        : FF component. (type:float)
        P                         : P component. (type:float)
        I                         : I component. (type:float)
        D                         : D component. (type:float)
        SRate                     : Slew rate. (type:float)
        PDmod                     : P/D oscillation modifier. (type:float)

        """
        return MAVLink_pid_tuning_message(axis, desired, achieved, FF, P, I, D, SRate, PDmod)

## pid_tuning_send
    def pid_tuning_send(self, axis: int, desired: float, achieved: float, FF: float, P: float, I: float, D: float, SRate: float = 0, PDmod: float = 0, force_mavlink1: bool = False) -> None:
        """
        PID tuning information.

        axis                      : Axis. (type:uint8_t, values:PID_TUNING_AXIS)
        desired                   : Desired rate. (type:float)
        achieved                  : Achieved rate. (type:float)
        FF                        : FF component. (type:float)
        P                         : P component. (type:float)
        I                         : I component. (type:float)
        D                         : D component. (type:float)
        SRate                     : Slew rate. (type:float)
        PDmod                     : P/D oscillation modifier. (type:float)

        """
        self.send(self.pid_tuning_encode(axis, desired, achieved, FF, P, I, D, SRate, PDmod), force_mavlink1=force_mavlink1)

## deepstall_encode
    def deepstall_encode(self, landing_lat: int, landing_lon: int, path_lat: int, path_lon: int, arc_entry_lat: int, arc_entry_lon: int, altitude: float, expected_travel_distance: float, cross_track_error: float, stage: int) -> MAVLink_deepstall_message:
        """
        Deepstall path planning.

        landing_lat               : Landing latitude. [degE7] (type:int32_t)
        landing_lon               : Landing longitude. [degE7] (type:int32_t)
        path_lat                  : Final heading start point, latitude. [degE7] (type:int32_t)
        path_lon                  : Final heading start point, longitude. [degE7] (type:int32_t)
        arc_entry_lat             : Arc entry point, latitude. [degE7] (type:int32_t)
        arc_entry_lon             : Arc entry point, longitude. [degE7] (type:int32_t)
        altitude                  : Altitude. [m] (type:float)
        expected_travel_distance        : Distance the aircraft expects to travel during the deepstall. [m] (type:float)
        cross_track_error         : Deepstall cross track error (only valid when in DEEPSTALL_STAGE_LAND). [m] (type:float)
        stage                     : Deepstall stage. (type:uint8_t, values:DEEPSTALL_STAGE)

        """
        return MAVLink_deepstall_message(landing_lat, landing_lon, path_lat, path_lon, arc_entry_lat, arc_entry_lon, altitude, expected_travel_distance, cross_track_error, stage)

## deepstall_send
    def deepstall_send(self, landing_lat: int, landing_lon: int, path_lat: int, path_lon: int, arc_entry_lat: int, arc_entry_lon: int, altitude: float, expected_travel_distance: float, cross_track_error: float, stage: int, force_mavlink1: bool = False) -> None:
        """
        Deepstall path planning.

        landing_lat               : Landing latitude. [degE7] (type:int32_t)
        landing_lon               : Landing longitude. [degE7] (type:int32_t)
        path_lat                  : Final heading start point, latitude. [degE7] (type:int32_t)
        path_lon                  : Final heading start point, longitude. [degE7] (type:int32_t)
        arc_entry_lat             : Arc entry point, latitude. [degE7] (type:int32_t)
        arc_entry_lon             : Arc entry point, longitude. [degE7] (type:int32_t)
        altitude                  : Altitude. [m] (type:float)
        expected_travel_distance        : Distance the aircraft expects to travel during the deepstall. [m] (type:float)
        cross_track_error         : Deepstall cross track error (only valid when in DEEPSTALL_STAGE_LAND). [m] (type:float)
        stage                     : Deepstall stage. (type:uint8_t, values:DEEPSTALL_STAGE)

        """
        self.send(self.deepstall_encode(landing_lat, landing_lon, path_lat, path_lon, arc_entry_lat, arc_entry_lon, altitude, expected_travel_distance, cross_track_error, stage), force_mavlink1=force_mavlink1)

## gimbal_report_encode
    def gimbal_report_encode(self, target_system: int, target_component: int, delta_time: float, delta_angle_x: float, delta_angle_y: float, delta_angle_z: float, delta_velocity_x: float, delta_velocity_y: float, delta_velocity_z: float, joint_roll: float, joint_el: float, joint_az: float) -> MAVLink_gimbal_report_message:
        """
        3 axis gimbal measurements.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        delta_time                : Time since last update. [s] (type:float)
        delta_angle_x             : Delta angle X. [rad] (type:float)
        delta_angle_y             : Delta angle Y. [rad] (type:float)
        delta_angle_z             : Delta angle X. [rad] (type:float)
        delta_velocity_x          : Delta velocity X. [m/s] (type:float)
        delta_velocity_y          : Delta velocity Y. [m/s] (type:float)
        delta_velocity_z          : Delta velocity Z. [m/s] (type:float)
        joint_roll                : Joint ROLL. [rad] (type:float)
        joint_el                  : Joint EL. [rad] (type:float)
        joint_az                  : Joint AZ. [rad] (type:float)

        """
        return MAVLink_gimbal_report_message(target_system, target_component, delta_time, delta_angle_x, delta_angle_y, delta_angle_z, delta_velocity_x, delta_velocity_y, delta_velocity_z, joint_roll, joint_el, joint_az)

## gimbal_report_send
    def gimbal_report_send(self, target_system: int, target_component: int, delta_time: float, delta_angle_x: float, delta_angle_y: float, delta_angle_z: float, delta_velocity_x: float, delta_velocity_y: float, delta_velocity_z: float, joint_roll: float, joint_el: float, joint_az: float, force_mavlink1: bool = False) -> None:
        """
        3 axis gimbal measurements.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        delta_time                : Time since last update. [s] (type:float)
        delta_angle_x             : Delta angle X. [rad] (type:float)
        delta_angle_y             : Delta angle Y. [rad] (type:float)
        delta_angle_z             : Delta angle X. [rad] (type:float)
        delta_velocity_x          : Delta velocity X. [m/s] (type:float)
        delta_velocity_y          : Delta velocity Y. [m/s] (type:float)
        delta_velocity_z          : Delta velocity Z. [m/s] (type:float)
        joint_roll                : Joint ROLL. [rad] (type:float)
        joint_el                  : Joint EL. [rad] (type:float)
        joint_az                  : Joint AZ. [rad] (type:float)

        """
        self.send(self.gimbal_report_encode(target_system, target_component, delta_time, delta_angle_x, delta_angle_y, delta_angle_z, delta_velocity_x, delta_velocity_y, delta_velocity_z, joint_roll, joint_el, joint_az), force_mavlink1=force_mavlink1)

## gimbal_control_encode
    def gimbal_control_encode(self, target_system: int, target_component: int, demanded_rate_x: float, demanded_rate_y: float, demanded_rate_z: float) -> MAVLink_gimbal_control_message:
        """
        Control message for rate gimbal.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        demanded_rate_x           : Demanded angular rate X. [rad/s] (type:float)
        demanded_rate_y           : Demanded angular rate Y. [rad/s] (type:float)
        demanded_rate_z           : Demanded angular rate Z. [rad/s] (type:float)

        """
        return MAVLink_gimbal_control_message(target_system, target_component, demanded_rate_x, demanded_rate_y, demanded_rate_z)

## gimbal_control_send
    def gimbal_control_send(self, target_system: int, target_component: int, demanded_rate_x: float, demanded_rate_y: float, demanded_rate_z: float, force_mavlink1: bool = False) -> None:
        """
        Control message for rate gimbal.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        demanded_rate_x           : Demanded angular rate X. [rad/s] (type:float)
        demanded_rate_y           : Demanded angular rate Y. [rad/s] (type:float)
        demanded_rate_z           : Demanded angular rate Z. [rad/s] (type:float)

        """
        self.send(self.gimbal_control_encode(target_system, target_component, demanded_rate_x, demanded_rate_y, demanded_rate_z), force_mavlink1=force_mavlink1)

## gimbal_torque_cmd_report_encode
    def gimbal_torque_cmd_report_encode(self, target_system: int, target_component: int, rl_torque_cmd: int, el_torque_cmd: int, az_torque_cmd: int) -> MAVLink_gimbal_torque_cmd_report_message:
        """
        100 Hz gimbal torque command telemetry.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        rl_torque_cmd             : Roll Torque Command. (type:int16_t)
        el_torque_cmd             : Elevation Torque Command. (type:int16_t)
        az_torque_cmd             : Azimuth Torque Command. (type:int16_t)

        """
        return MAVLink_gimbal_torque_cmd_report_message(target_system, target_component, rl_torque_cmd, el_torque_cmd, az_torque_cmd)

## gimbal_torque_cmd_report_send
    def gimbal_torque_cmd_report_send(self, target_system: int, target_component: int, rl_torque_cmd: int, el_torque_cmd: int, az_torque_cmd: int, force_mavlink1: bool = False) -> None:
        """
        100 Hz gimbal torque command telemetry.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        rl_torque_cmd             : Roll Torque Command. (type:int16_t)
        el_torque_cmd             : Elevation Torque Command. (type:int16_t)
        az_torque_cmd             : Azimuth Torque Command. (type:int16_t)

        """
        self.send(self.gimbal_torque_cmd_report_encode(target_system, target_component, rl_torque_cmd, el_torque_cmd, az_torque_cmd), force_mavlink1=force_mavlink1)

## gopro_heartbeat_encode
    def gopro_heartbeat_encode(self, status: int, capture_mode: int, flags: int) -> MAVLink_gopro_heartbeat_message:
        """
        Heartbeat from a HeroBus attached GoPro.

        status                    : Status. (type:uint8_t, values:GOPRO_HEARTBEAT_STATUS)
        capture_mode              : Current capture mode. (type:uint8_t, values:GOPRO_CAPTURE_MODE)
        flags                     : Additional status bits. (type:uint8_t, values:GOPRO_HEARTBEAT_FLAGS)

        """
        return MAVLink_gopro_heartbeat_message(status, capture_mode, flags)

## gopro_heartbeat_send
    def gopro_heartbeat_send(self, status: int, capture_mode: int, flags: int, force_mavlink1: bool = False) -> None:
        """
        Heartbeat from a HeroBus attached GoPro.

        status                    : Status. (type:uint8_t, values:GOPRO_HEARTBEAT_STATUS)
        capture_mode              : Current capture mode. (type:uint8_t, values:GOPRO_CAPTURE_MODE)
        flags                     : Additional status bits. (type:uint8_t, values:GOPRO_HEARTBEAT_FLAGS)

        """
        self.send(self.gopro_heartbeat_encode(status, capture_mode, flags), force_mavlink1=force_mavlink1)

## gopro_get_request_encode
    def gopro_get_request_encode(self, target_system: int, target_component: int, cmd_id: int) -> MAVLink_gopro_get_request_message:
        """
        Request a GOPRO_COMMAND response from the GoPro.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        cmd_id                    : Command ID. (type:uint8_t, values:GOPRO_COMMAND)

        """
        return MAVLink_gopro_get_request_message(target_system, target_component, cmd_id)

## gopro_get_request_send
    def gopro_get_request_send(self, target_system: int, target_component: int, cmd_id: int, force_mavlink1: bool = False) -> None:
        """
        Request a GOPRO_COMMAND response from the GoPro.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        cmd_id                    : Command ID. (type:uint8_t, values:GOPRO_COMMAND)

        """
        self.send(self.gopro_get_request_encode(target_system, target_component, cmd_id), force_mavlink1=force_mavlink1)

## gopro_get_response_encode
    def gopro_get_response_encode(self, cmd_id: int, status: int, value: Sequence[int]) -> MAVLink_gopro_get_response_message:
        """
        Response from a GOPRO_COMMAND get request.

        cmd_id                    : Command ID. (type:uint8_t, values:GOPRO_COMMAND)
        status                    : Status. (type:uint8_t, values:GOPRO_REQUEST_STATUS)
        value                     : Value. (type:uint8_t)

        """
        return MAVLink_gopro_get_response_message(cmd_id, status, value)

## gopro_get_response_send
    def gopro_get_response_send(self, cmd_id: int, status: int, value: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Response from a GOPRO_COMMAND get request.

        cmd_id                    : Command ID. (type:uint8_t, values:GOPRO_COMMAND)
        status                    : Status. (type:uint8_t, values:GOPRO_REQUEST_STATUS)
        value                     : Value. (type:uint8_t)

        """
        self.send(self.gopro_get_response_encode(cmd_id, status, value), force_mavlink1=force_mavlink1)

## gopro_set_request_encode
    def gopro_set_request_encode(self, target_system: int, target_component: int, cmd_id: int, value: Sequence[int]) -> MAVLink_gopro_set_request_message:
        """
        Request to set a GOPRO_COMMAND with a desired.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        cmd_id                    : Command ID. (type:uint8_t, values:GOPRO_COMMAND)
        value                     : Value. (type:uint8_t)

        """
        return MAVLink_gopro_set_request_message(target_system, target_component, cmd_id, value)

## gopro_set_request_send
    def gopro_set_request_send(self, target_system: int, target_component: int, cmd_id: int, value: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Request to set a GOPRO_COMMAND with a desired.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        cmd_id                    : Command ID. (type:uint8_t, values:GOPRO_COMMAND)
        value                     : Value. (type:uint8_t)

        """
        self.send(self.gopro_set_request_encode(target_system, target_component, cmd_id, value), force_mavlink1=force_mavlink1)

## gopro_set_response_encode
    def gopro_set_response_encode(self, cmd_id: int, status: int) -> MAVLink_gopro_set_response_message:
        """
        Response from a GOPRO_COMMAND set request.

        cmd_id                    : Command ID. (type:uint8_t, values:GOPRO_COMMAND)
        status                    : Status. (type:uint8_t, values:GOPRO_REQUEST_STATUS)

        """
        return MAVLink_gopro_set_response_message(cmd_id, status)

## gopro_set_response_send
    def gopro_set_response_send(self, cmd_id: int, status: int, force_mavlink1: bool = False) -> None:
        """
        Response from a GOPRO_COMMAND set request.

        cmd_id                    : Command ID. (type:uint8_t, values:GOPRO_COMMAND)
        status                    : Status. (type:uint8_t, values:GOPRO_REQUEST_STATUS)

        """
        self.send(self.gopro_set_response_encode(cmd_id, status), force_mavlink1=force_mavlink1)

## rpm_encode
    def rpm_encode(self, rpm1: float, rpm2: float) -> MAVLink_rpm_message:
        """
        RPM sensor output.

        rpm1                      : RPM Sensor1. (type:float)
        rpm2                      : RPM Sensor2. (type:float)

        """
        return MAVLink_rpm_message(rpm1, rpm2)

## rpm_send
    def rpm_send(self, rpm1: float, rpm2: float, force_mavlink1: bool = False) -> None:
        """
        RPM sensor output.

        rpm1                      : RPM Sensor1. (type:float)
        rpm2                      : RPM Sensor2. (type:float)

        """
        self.send(self.rpm_encode(rpm1, rpm2), force_mavlink1=force_mavlink1)

## device_op_read_encode
    def device_op_read_encode(self, target_system: int, target_component: int, request_id: int, bustype: int, bus: int, address: int, busname: bytes, regstart: int, count: int, bank: int = 0) -> MAVLink_device_op_read_message:
        """
        Read registers for a device.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        request_id                : Request ID - copied to reply. (type:uint32_t)
        bustype                   : The bus type. (type:uint8_t, values:DEVICE_OP_BUSTYPE)
        bus                       : Bus number. (type:uint8_t)
        address                   : Bus address. (type:uint8_t)
        busname                   : Name of device on bus (for SPI). (type:char)
        regstart                  : First register to read. (type:uint8_t)
        count                     : Count of registers to read. (type:uint8_t)
        bank                      : Bank number. (type:uint8_t)

        """
        return MAVLink_device_op_read_message(target_system, target_component, request_id, bustype, bus, address, busname, regstart, count, bank)

## device_op_read_send
    def device_op_read_send(self, target_system: int, target_component: int, request_id: int, bustype: int, bus: int, address: int, busname: bytes, regstart: int, count: int, bank: int = 0, force_mavlink1: bool = False) -> None:
        """
        Read registers for a device.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        request_id                : Request ID - copied to reply. (type:uint32_t)
        bustype                   : The bus type. (type:uint8_t, values:DEVICE_OP_BUSTYPE)
        bus                       : Bus number. (type:uint8_t)
        address                   : Bus address. (type:uint8_t)
        busname                   : Name of device on bus (for SPI). (type:char)
        regstart                  : First register to read. (type:uint8_t)
        count                     : Count of registers to read. (type:uint8_t)
        bank                      : Bank number. (type:uint8_t)

        """
        self.send(self.device_op_read_encode(target_system, target_component, request_id, bustype, bus, address, busname, regstart, count, bank), force_mavlink1=force_mavlink1)

## device_op_read_reply_encode
    def device_op_read_reply_encode(self, request_id: int, result: int, regstart: int, count: int, data: Sequence[int], bank: int = 0) -> MAVLink_device_op_read_reply_message:
        """
        Read registers reply.

        request_id                : Request ID - copied from request. (type:uint32_t)
        result                    : 0 for success, anything else is failure code. (type:uint8_t)
        regstart                  : Starting register. (type:uint8_t)
        count                     : Count of bytes read. (type:uint8_t)
        data                      : Reply data. (type:uint8_t)
        bank                      : Bank number. (type:uint8_t)

        """
        return MAVLink_device_op_read_reply_message(request_id, result, regstart, count, data, bank)

## device_op_read_reply_send
    def device_op_read_reply_send(self, request_id: int, result: int, regstart: int, count: int, data: Sequence[int], bank: int = 0, force_mavlink1: bool = False) -> None:
        """
        Read registers reply.

        request_id                : Request ID - copied from request. (type:uint32_t)
        result                    : 0 for success, anything else is failure code. (type:uint8_t)
        regstart                  : Starting register. (type:uint8_t)
        count                     : Count of bytes read. (type:uint8_t)
        data                      : Reply data. (type:uint8_t)
        bank                      : Bank number. (type:uint8_t)

        """
        self.send(self.device_op_read_reply_encode(request_id, result, regstart, count, data, bank), force_mavlink1=force_mavlink1)

## device_op_write_encode
    def device_op_write_encode(self, target_system: int, target_component: int, request_id: int, bustype: int, bus: int, address: int, busname: bytes, regstart: int, count: int, data: Sequence[int], bank: int = 0) -> MAVLink_device_op_write_message:
        """
        Write registers for a device.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        request_id                : Request ID - copied to reply. (type:uint32_t)
        bustype                   : The bus type. (type:uint8_t, values:DEVICE_OP_BUSTYPE)
        bus                       : Bus number. (type:uint8_t)
        address                   : Bus address. (type:uint8_t)
        busname                   : Name of device on bus (for SPI). (type:char)
        regstart                  : First register to write. (type:uint8_t)
        count                     : Count of registers to write. (type:uint8_t)
        data                      : Write data. (type:uint8_t)
        bank                      : Bank number. (type:uint8_t)

        """
        return MAVLink_device_op_write_message(target_system, target_component, request_id, bustype, bus, address, busname, regstart, count, data, bank)

## device_op_write_send
    def device_op_write_send(self, target_system: int, target_component: int, request_id: int, bustype: int, bus: int, address: int, busname: bytes, regstart: int, count: int, data: Sequence[int], bank: int = 0, force_mavlink1: bool = False) -> None:
        """
        Write registers for a device.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        request_id                : Request ID - copied to reply. (type:uint32_t)
        bustype                   : The bus type. (type:uint8_t, values:DEVICE_OP_BUSTYPE)
        bus                       : Bus number. (type:uint8_t)
        address                   : Bus address. (type:uint8_t)
        busname                   : Name of device on bus (for SPI). (type:char)
        regstart                  : First register to write. (type:uint8_t)
        count                     : Count of registers to write. (type:uint8_t)
        data                      : Write data. (type:uint8_t)
        bank                      : Bank number. (type:uint8_t)

        """
        self.send(self.device_op_write_encode(target_system, target_component, request_id, bustype, bus, address, busname, regstart, count, data, bank), force_mavlink1=force_mavlink1)

## device_op_write_reply_encode
    def device_op_write_reply_encode(self, request_id: int, result: int) -> MAVLink_device_op_write_reply_message:
        """
        Write registers reply.

        request_id                : Request ID - copied from request. (type:uint32_t)
        result                    : 0 for success, anything else is failure code. (type:uint8_t)

        """
        return MAVLink_device_op_write_reply_message(request_id, result)

## device_op_write_reply_send
    def device_op_write_reply_send(self, request_id: int, result: int, force_mavlink1: bool = False) -> None:
        """
        Write registers reply.

        request_id                : Request ID - copied from request. (type:uint32_t)
        result                    : 0 for success, anything else is failure code. (type:uint8_t)

        """
        self.send(self.device_op_write_reply_encode(request_id, result), force_mavlink1=force_mavlink1)

## secure_command_encode
    def secure_command_encode(self, target_system: int, target_component: int, sequence: int, operation: int, data_length: int, sig_length: int, data: Sequence[int]) -> MAVLink_secure_command_message:
        """
        Send a secure command. Data should be signed with a private key
        corresponding with a public key known to the recipient.
        Signature should be over the concatenation of the sequence
        number (little-endian format), the operation (little-endian
        format) the data and the session key. For
        SECURE_COMMAND_GET_SESSION_KEY the session key should be zero
        length. The data array consists of the data followed by the
        signature. The sum of the data_length and the sig_length
        cannot be more than 220. The format of the data is command
        specific.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        sequence                  : Sequence ID for tagging reply. (type:uint32_t)
        operation                 : Operation being requested. (type:uint32_t, values:SECURE_COMMAND_OP)
        data_length               : Data length. (type:uint8_t)
        sig_length                : Signature length. (type:uint8_t)
        data                      : Signed data. (type:uint8_t)

        """
        return MAVLink_secure_command_message(target_system, target_component, sequence, operation, data_length, sig_length, data)

## secure_command_send
    def secure_command_send(self, target_system: int, target_component: int, sequence: int, operation: int, data_length: int, sig_length: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Send a secure command. Data should be signed with a private key
        corresponding with a public key known to the recipient.
        Signature should be over the concatenation of the sequence
        number (little-endian format), the operation (little-endian
        format) the data and the session key. For
        SECURE_COMMAND_GET_SESSION_KEY the session key should be zero
        length. The data array consists of the data followed by the
        signature. The sum of the data_length and the sig_length
        cannot be more than 220. The format of the data is command
        specific.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        sequence                  : Sequence ID for tagging reply. (type:uint32_t)
        operation                 : Operation being requested. (type:uint32_t, values:SECURE_COMMAND_OP)
        data_length               : Data length. (type:uint8_t)
        sig_length                : Signature length. (type:uint8_t)
        data                      : Signed data. (type:uint8_t)

        """
        self.send(self.secure_command_encode(target_system, target_component, sequence, operation, data_length, sig_length, data), force_mavlink1=force_mavlink1)

## secure_command_reply_encode
    def secure_command_reply_encode(self, sequence: int, operation: int, result: int, data_length: int, data: Sequence[int]) -> MAVLink_secure_command_reply_message:
        """
        Reply from secure command.

        sequence                  : Sequence ID from request. (type:uint32_t)
        operation                 : Operation that was requested. (type:uint32_t, values:SECURE_COMMAND_OP)
        result                    : Result of command. (type:uint8_t, values:MAV_RESULT)
        data_length               : Data length. (type:uint8_t)
        data                      : Reply data. (type:uint8_t)

        """
        return MAVLink_secure_command_reply_message(sequence, operation, result, data_length, data)

## secure_command_reply_send
    def secure_command_reply_send(self, sequence: int, operation: int, result: int, data_length: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Reply from secure command.

        sequence                  : Sequence ID from request. (type:uint32_t)
        operation                 : Operation that was requested. (type:uint32_t, values:SECURE_COMMAND_OP)
        result                    : Result of command. (type:uint8_t, values:MAV_RESULT)
        data_length               : Data length. (type:uint8_t)
        data                      : Reply data. (type:uint8_t)

        """
        self.send(self.secure_command_reply_encode(sequence, operation, result, data_length, data), force_mavlink1=force_mavlink1)

## adap_tuning_encode
    def adap_tuning_encode(self, axis: int, desired: float, achieved: float, error: float, theta: float, omega: float, sigma: float, theta_dot: float, omega_dot: float, sigma_dot: float, f: float, f_dot: float, u: float) -> MAVLink_adap_tuning_message:
        """
        Adaptive Controller tuning information.

        axis                      : Axis. (type:uint8_t, values:PID_TUNING_AXIS)
        desired                   : Desired rate. [deg/s] (type:float)
        achieved                  : Achieved rate. [deg/s] (type:float)
        error                     : Error between model and vehicle. (type:float)
        theta                     : Theta estimated state predictor. (type:float)
        omega                     : Omega estimated state predictor. (type:float)
        sigma                     : Sigma estimated state predictor. (type:float)
        theta_dot                 : Theta derivative. (type:float)
        omega_dot                 : Omega derivative. (type:float)
        sigma_dot                 : Sigma derivative. (type:float)
        f                         : Projection operator value. (type:float)
        f_dot                     : Projection operator derivative. (type:float)
        u                         : u adaptive controlled output command. (type:float)

        """
        return MAVLink_adap_tuning_message(axis, desired, achieved, error, theta, omega, sigma, theta_dot, omega_dot, sigma_dot, f, f_dot, u)

## adap_tuning_send
    def adap_tuning_send(self, axis: int, desired: float, achieved: float, error: float, theta: float, omega: float, sigma: float, theta_dot: float, omega_dot: float, sigma_dot: float, f: float, f_dot: float, u: float, force_mavlink1: bool = False) -> None:
        """
        Adaptive Controller tuning information.

        axis                      : Axis. (type:uint8_t, values:PID_TUNING_AXIS)
        desired                   : Desired rate. [deg/s] (type:float)
        achieved                  : Achieved rate. [deg/s] (type:float)
        error                     : Error between model and vehicle. (type:float)
        theta                     : Theta estimated state predictor. (type:float)
        omega                     : Omega estimated state predictor. (type:float)
        sigma                     : Sigma estimated state predictor. (type:float)
        theta_dot                 : Theta derivative. (type:float)
        omega_dot                 : Omega derivative. (type:float)
        sigma_dot                 : Sigma derivative. (type:float)
        f                         : Projection operator value. (type:float)
        f_dot                     : Projection operator derivative. (type:float)
        u                         : u adaptive controlled output command. (type:float)

        """
        self.send(self.adap_tuning_encode(axis, desired, achieved, error, theta, omega, sigma, theta_dot, omega_dot, sigma_dot, f, f_dot, u), force_mavlink1=force_mavlink1)

## vision_position_delta_encode
    def vision_position_delta_encode(self, time_usec: int, time_delta_usec: int, angle_delta: Sequence[float], position_delta: Sequence[float], confidence: float) -> MAVLink_vision_position_delta_message:
        """
        Camera vision based attitude and position deltas.

        time_usec                 : Timestamp (synced to UNIX time or since system boot). [us] (type:uint64_t)
        time_delta_usec           : Time since the last reported camera frame. [us] (type:uint64_t)
        angle_delta               : Defines a rotation vector [roll, pitch, yaw] to the current MAV_FRAME_BODY_FRD from the previous MAV_FRAME_BODY_FRD. [rad] (type:float)
        position_delta            : Change in position to the current MAV_FRAME_BODY_FRD from the previous FRAME_BODY_FRD rotated to the current MAV_FRAME_BODY_FRD. [m] (type:float)
        confidence                : Normalised confidence value from 0 to 100. [%] (type:float)

        """
        return MAVLink_vision_position_delta_message(time_usec, time_delta_usec, angle_delta, position_delta, confidence)

## vision_position_delta_send
    def vision_position_delta_send(self, time_usec: int, time_delta_usec: int, angle_delta: Sequence[float], position_delta: Sequence[float], confidence: float, force_mavlink1: bool = False) -> None:
        """
        Camera vision based attitude and position deltas.

        time_usec                 : Timestamp (synced to UNIX time or since system boot). [us] (type:uint64_t)
        time_delta_usec           : Time since the last reported camera frame. [us] (type:uint64_t)
        angle_delta               : Defines a rotation vector [roll, pitch, yaw] to the current MAV_FRAME_BODY_FRD from the previous MAV_FRAME_BODY_FRD. [rad] (type:float)
        position_delta            : Change in position to the current MAV_FRAME_BODY_FRD from the previous FRAME_BODY_FRD rotated to the current MAV_FRAME_BODY_FRD. [m] (type:float)
        confidence                : Normalised confidence value from 0 to 100. [%] (type:float)

        """
        self.send(self.vision_position_delta_encode(time_usec, time_delta_usec, angle_delta, position_delta, confidence), force_mavlink1=force_mavlink1)

## aoa_ssa_encode
    def aoa_ssa_encode(self, time_usec: int, AOA: float, SSA: float) -> MAVLink_aoa_ssa_message:
        """
        Angle of Attack and Side Slip Angle.

        time_usec                 : Timestamp (since boot or Unix epoch). [us] (type:uint64_t)
        AOA                       : Angle of Attack. [deg] (type:float)
        SSA                       : Side Slip Angle. [deg] (type:float)

        """
        return MAVLink_aoa_ssa_message(time_usec, AOA, SSA)

## aoa_ssa_send
    def aoa_ssa_send(self, time_usec: int, AOA: float, SSA: float, force_mavlink1: bool = False) -> None:
        """
        Angle of Attack and Side Slip Angle.

        time_usec                 : Timestamp (since boot or Unix epoch). [us] (type:uint64_t)
        AOA                       : Angle of Attack. [deg] (type:float)
        SSA                       : Side Slip Angle. [deg] (type:float)

        """
        self.send(self.aoa_ssa_encode(time_usec, AOA, SSA), force_mavlink1=force_mavlink1)

## esc_telemetry_1_to_4_encode
    def esc_telemetry_1_to_4_encode(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int]) -> MAVLink_esc_telemetry_1_to_4_message:
        """
        ESC Telemetry Data for ESCs 1 to 4, matching data sent by BLHeli ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        return MAVLink_esc_telemetry_1_to_4_message(temperature, voltage, current, totalcurrent, rpm, count)

## esc_telemetry_1_to_4_send
    def esc_telemetry_1_to_4_send(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        ESC Telemetry Data for ESCs 1 to 4, matching data sent by BLHeli ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        self.send(self.esc_telemetry_1_to_4_encode(temperature, voltage, current, totalcurrent, rpm, count), force_mavlink1=force_mavlink1)

## esc_telemetry_5_to_8_encode
    def esc_telemetry_5_to_8_encode(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int]) -> MAVLink_esc_telemetry_5_to_8_message:
        """
        ESC Telemetry Data for ESCs 5 to 8, matching data sent by BLHeli ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        return MAVLink_esc_telemetry_5_to_8_message(temperature, voltage, current, totalcurrent, rpm, count)

## esc_telemetry_5_to_8_send
    def esc_telemetry_5_to_8_send(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        ESC Telemetry Data for ESCs 5 to 8, matching data sent by BLHeli ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        self.send(self.esc_telemetry_5_to_8_encode(temperature, voltage, current, totalcurrent, rpm, count), force_mavlink1=force_mavlink1)

## esc_telemetry_9_to_12_encode
    def esc_telemetry_9_to_12_encode(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int]) -> MAVLink_esc_telemetry_9_to_12_message:
        """
        ESC Telemetry Data for ESCs 9 to 12, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        return MAVLink_esc_telemetry_9_to_12_message(temperature, voltage, current, totalcurrent, rpm, count)

## esc_telemetry_9_to_12_send
    def esc_telemetry_9_to_12_send(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        ESC Telemetry Data for ESCs 9 to 12, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        self.send(self.esc_telemetry_9_to_12_encode(temperature, voltage, current, totalcurrent, rpm, count), force_mavlink1=force_mavlink1)

## osd_param_config_encode
    def osd_param_config_encode(self, target_system: int, target_component: int, request_id: int, osd_screen: int, osd_index: int, param_id: bytes, config_type: int, min_value: float, max_value: float, increment: float) -> MAVLink_osd_param_config_message:
        """
        Configure an OSD parameter slot.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        request_id                : Request ID - copied to reply. (type:uint32_t)
        osd_screen                : OSD parameter screen index. (type:uint8_t)
        osd_index                 : OSD parameter display index. (type:uint8_t)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        config_type               : Config type. (type:uint8_t, values:OSD_PARAM_CONFIG_TYPE)
        min_value                 : OSD parameter minimum value. (type:float)
        max_value                 : OSD parameter maximum value. (type:float)
        increment                 : OSD parameter increment. (type:float)

        """
        return MAVLink_osd_param_config_message(target_system, target_component, request_id, osd_screen, osd_index, param_id, config_type, min_value, max_value, increment)

## osd_param_config_send
    def osd_param_config_send(self, target_system: int, target_component: int, request_id: int, osd_screen: int, osd_index: int, param_id: bytes, config_type: int, min_value: float, max_value: float, increment: float, force_mavlink1: bool = False) -> None:
        """
        Configure an OSD parameter slot.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        request_id                : Request ID - copied to reply. (type:uint32_t)
        osd_screen                : OSD parameter screen index. (type:uint8_t)
        osd_index                 : OSD parameter display index. (type:uint8_t)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        config_type               : Config type. (type:uint8_t, values:OSD_PARAM_CONFIG_TYPE)
        min_value                 : OSD parameter minimum value. (type:float)
        max_value                 : OSD parameter maximum value. (type:float)
        increment                 : OSD parameter increment. (type:float)

        """
        self.send(self.osd_param_config_encode(target_system, target_component, request_id, osd_screen, osd_index, param_id, config_type, min_value, max_value, increment), force_mavlink1=force_mavlink1)

## osd_param_config_reply_encode
    def osd_param_config_reply_encode(self, request_id: int, result: int) -> MAVLink_osd_param_config_reply_message:
        """
        Configure OSD parameter reply.

        request_id                : Request ID - copied from request. (type:uint32_t)
        result                    : Config error type. (type:uint8_t, values:OSD_PARAM_CONFIG_ERROR)

        """
        return MAVLink_osd_param_config_reply_message(request_id, result)

## osd_param_config_reply_send
    def osd_param_config_reply_send(self, request_id: int, result: int, force_mavlink1: bool = False) -> None:
        """
        Configure OSD parameter reply.

        request_id                : Request ID - copied from request. (type:uint32_t)
        result                    : Config error type. (type:uint8_t, values:OSD_PARAM_CONFIG_ERROR)

        """
        self.send(self.osd_param_config_reply_encode(request_id, result), force_mavlink1=force_mavlink1)

## osd_param_show_config_encode
    def osd_param_show_config_encode(self, target_system: int, target_component: int, request_id: int, osd_screen: int, osd_index: int) -> MAVLink_osd_param_show_config_message:
        """
        Read a configured an OSD parameter slot.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        request_id                : Request ID - copied to reply. (type:uint32_t)
        osd_screen                : OSD parameter screen index. (type:uint8_t)
        osd_index                 : OSD parameter display index. (type:uint8_t)

        """
        return MAVLink_osd_param_show_config_message(target_system, target_component, request_id, osd_screen, osd_index)

## osd_param_show_config_send
    def osd_param_show_config_send(self, target_system: int, target_component: int, request_id: int, osd_screen: int, osd_index: int, force_mavlink1: bool = False) -> None:
        """
        Read a configured an OSD parameter slot.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        request_id                : Request ID - copied to reply. (type:uint32_t)
        osd_screen                : OSD parameter screen index. (type:uint8_t)
        osd_index                 : OSD parameter display index. (type:uint8_t)

        """
        self.send(self.osd_param_show_config_encode(target_system, target_component, request_id, osd_screen, osd_index), force_mavlink1=force_mavlink1)

## osd_param_show_config_reply_encode
    def osd_param_show_config_reply_encode(self, request_id: int, result: int, param_id: bytes, config_type: int, min_value: float, max_value: float, increment: float) -> MAVLink_osd_param_show_config_reply_message:
        """
        Read configured OSD parameter reply.

        request_id                : Request ID - copied from request. (type:uint32_t)
        result                    : Config error type. (type:uint8_t, values:OSD_PARAM_CONFIG_ERROR)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        config_type               : Config type. (type:uint8_t, values:OSD_PARAM_CONFIG_TYPE)
        min_value                 : OSD parameter minimum value. (type:float)
        max_value                 : OSD parameter maximum value. (type:float)
        increment                 : OSD parameter increment. (type:float)

        """
        return MAVLink_osd_param_show_config_reply_message(request_id, result, param_id, config_type, min_value, max_value, increment)

## osd_param_show_config_reply_send
    def osd_param_show_config_reply_send(self, request_id: int, result: int, param_id: bytes, config_type: int, min_value: float, max_value: float, increment: float, force_mavlink1: bool = False) -> None:
        """
        Read configured OSD parameter reply.

        request_id                : Request ID - copied from request. (type:uint32_t)
        result                    : Config error type. (type:uint8_t, values:OSD_PARAM_CONFIG_ERROR)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        config_type               : Config type. (type:uint8_t, values:OSD_PARAM_CONFIG_TYPE)
        min_value                 : OSD parameter minimum value. (type:float)
        max_value                 : OSD parameter maximum value. (type:float)
        increment                 : OSD parameter increment. (type:float)

        """
        self.send(self.osd_param_show_config_reply_encode(request_id, result, param_id, config_type, min_value, max_value, increment), force_mavlink1=force_mavlink1)

## obstacle_distance_3d_encode
    def obstacle_distance_3d_encode(self, time_boot_ms: int, sensor_type: int, frame: int, obstacle_id: int, x: float, y: float, z: float, min_distance: float, max_distance: float) -> MAVLink_obstacle_distance_3d_message:
        """
        Obstacle located as a 3D vector.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        sensor_type               : Class id of the distance sensor type. (type:uint8_t, values:MAV_DISTANCE_SENSOR)
        frame                     : Coordinate frame of reference. (type:uint8_t, values:MAV_FRAME)
        obstacle_id               : Unique ID given to each obstacle so that its movement can be tracked. Use UINT16_MAX if object ID is unknown or cannot be determined. (type:uint16_t)
        x                         : X position of the obstacle. [m] (type:float)
        y                         : Y position of the obstacle. [m] (type:float)
        z                         : Z position of the obstacle. [m] (type:float)
        min_distance              : Minimum distance the sensor can measure. [m] (type:float)
        max_distance              : Maximum distance the sensor can measure. [m] (type:float)

        """
        return MAVLink_obstacle_distance_3d_message(time_boot_ms, sensor_type, frame, obstacle_id, x, y, z, min_distance, max_distance)

## obstacle_distance_3d_send
    def obstacle_distance_3d_send(self, time_boot_ms: int, sensor_type: int, frame: int, obstacle_id: int, x: float, y: float, z: float, min_distance: float, max_distance: float, force_mavlink1: bool = False) -> None:
        """
        Obstacle located as a 3D vector.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        sensor_type               : Class id of the distance sensor type. (type:uint8_t, values:MAV_DISTANCE_SENSOR)
        frame                     : Coordinate frame of reference. (type:uint8_t, values:MAV_FRAME)
        obstacle_id               : Unique ID given to each obstacle so that its movement can be tracked. Use UINT16_MAX if object ID is unknown or cannot be determined. (type:uint16_t)
        x                         : X position of the obstacle. [m] (type:float)
        y                         : Y position of the obstacle. [m] (type:float)
        z                         : Z position of the obstacle. [m] (type:float)
        min_distance              : Minimum distance the sensor can measure. [m] (type:float)
        max_distance              : Maximum distance the sensor can measure. [m] (type:float)

        """
        self.send(self.obstacle_distance_3d_encode(time_boot_ms, sensor_type, frame, obstacle_id, x, y, z, min_distance, max_distance), force_mavlink1=force_mavlink1)

## water_depth_encode
    def water_depth_encode(self, time_boot_ms: int, id: int, healthy: int, lat: int, lng: int, alt: float, roll: float, pitch: float, yaw: float, distance: float, temperature: float) -> MAVLink_water_depth_message:
        """
        Water depth

        time_boot_ms              : Timestamp (time since system boot) [ms] (type:uint32_t)
        id                        : Onboard ID of the sensor (type:uint8_t)
        healthy                   : Sensor data healthy (0=unhealthy, 1=healthy) (type:uint8_t)
        lat                       : Latitude [degE7] (type:int32_t)
        lng                       : Longitude [degE7] (type:int32_t)
        alt                       : Altitude (MSL) of vehicle [m] (type:float)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        distance                  : Distance (uncorrected) [m] (type:float)
        temperature               : Water temperature [degC] (type:float)

        """
        return MAVLink_water_depth_message(time_boot_ms, id, healthy, lat, lng, alt, roll, pitch, yaw, distance, temperature)

## water_depth_send
    def water_depth_send(self, time_boot_ms: int, id: int, healthy: int, lat: int, lng: int, alt: float, roll: float, pitch: float, yaw: float, distance: float, temperature: float, force_mavlink1: bool = False) -> None:
        """
        Water depth

        time_boot_ms              : Timestamp (time since system boot) [ms] (type:uint32_t)
        id                        : Onboard ID of the sensor (type:uint8_t)
        healthy                   : Sensor data healthy (0=unhealthy, 1=healthy) (type:uint8_t)
        lat                       : Latitude [degE7] (type:int32_t)
        lng                       : Longitude [degE7] (type:int32_t)
        alt                       : Altitude (MSL) of vehicle [m] (type:float)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        distance                  : Distance (uncorrected) [m] (type:float)
        temperature               : Water temperature [degC] (type:float)

        """
        self.send(self.water_depth_encode(time_boot_ms, id, healthy, lat, lng, alt, roll, pitch, yaw, distance, temperature), force_mavlink1=force_mavlink1)

## mcu_status_encode
    def mcu_status_encode(self, id: int, MCU_temperature: int, MCU_voltage: int, MCU_voltage_min: int, MCU_voltage_max: int) -> MAVLink_mcu_status_message:
        """
        The MCU status, giving MCU temperature and voltage. The min and max
        voltages are to allow for detecting power supply instability.

        id                        : MCU instance (type:uint8_t)
        MCU_temperature           : MCU Internal temperature [cdegC] (type:int16_t)
        MCU_voltage               : MCU voltage [mV] (type:uint16_t)
        MCU_voltage_min           : MCU voltage minimum [mV] (type:uint16_t)
        MCU_voltage_max           : MCU voltage maximum [mV] (type:uint16_t)

        """
        return MAVLink_mcu_status_message(id, MCU_temperature, MCU_voltage, MCU_voltage_min, MCU_voltage_max)

## mcu_status_send
    def mcu_status_send(self, id: int, MCU_temperature: int, MCU_voltage: int, MCU_voltage_min: int, MCU_voltage_max: int, force_mavlink1: bool = False) -> None:
        """
        The MCU status, giving MCU temperature and voltage. The min and max
        voltages are to allow for detecting power supply instability.

        id                        : MCU instance (type:uint8_t)
        MCU_temperature           : MCU Internal temperature [cdegC] (type:int16_t)
        MCU_voltage               : MCU voltage [mV] (type:uint16_t)
        MCU_voltage_min           : MCU voltage minimum [mV] (type:uint16_t)
        MCU_voltage_max           : MCU voltage maximum [mV] (type:uint16_t)

        """
        self.send(self.mcu_status_encode(id, MCU_temperature, MCU_voltage, MCU_voltage_min, MCU_voltage_max), force_mavlink1=force_mavlink1)

## esc_telemetry_13_to_16_encode
    def esc_telemetry_13_to_16_encode(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int]) -> MAVLink_esc_telemetry_13_to_16_message:
        """
        ESC Telemetry Data for ESCs 13 to 16, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        return MAVLink_esc_telemetry_13_to_16_message(temperature, voltage, current, totalcurrent, rpm, count)

## esc_telemetry_13_to_16_send
    def esc_telemetry_13_to_16_send(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        ESC Telemetry Data for ESCs 13 to 16, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        self.send(self.esc_telemetry_13_to_16_encode(temperature, voltage, current, totalcurrent, rpm, count), force_mavlink1=force_mavlink1)

## esc_telemetry_17_to_20_encode
    def esc_telemetry_17_to_20_encode(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int]) -> MAVLink_esc_telemetry_17_to_20_message:
        """
        ESC Telemetry Data for ESCs 17 to 20, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        return MAVLink_esc_telemetry_17_to_20_message(temperature, voltage, current, totalcurrent, rpm, count)

## esc_telemetry_17_to_20_send
    def esc_telemetry_17_to_20_send(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        ESC Telemetry Data for ESCs 17 to 20, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        self.send(self.esc_telemetry_17_to_20_encode(temperature, voltage, current, totalcurrent, rpm, count), force_mavlink1=force_mavlink1)

## esc_telemetry_21_to_24_encode
    def esc_telemetry_21_to_24_encode(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int]) -> MAVLink_esc_telemetry_21_to_24_message:
        """
        ESC Telemetry Data for ESCs 21 to 24, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        return MAVLink_esc_telemetry_21_to_24_message(temperature, voltage, current, totalcurrent, rpm, count)

## esc_telemetry_21_to_24_send
    def esc_telemetry_21_to_24_send(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        ESC Telemetry Data for ESCs 21 to 24, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        self.send(self.esc_telemetry_21_to_24_encode(temperature, voltage, current, totalcurrent, rpm, count), force_mavlink1=force_mavlink1)

## esc_telemetry_25_to_28_encode
    def esc_telemetry_25_to_28_encode(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int]) -> MAVLink_esc_telemetry_25_to_28_message:
        """
        ESC Telemetry Data for ESCs 25 to 28, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        return MAVLink_esc_telemetry_25_to_28_message(temperature, voltage, current, totalcurrent, rpm, count)

## esc_telemetry_25_to_28_send
    def esc_telemetry_25_to_28_send(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        ESC Telemetry Data for ESCs 25 to 28, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        self.send(self.esc_telemetry_25_to_28_encode(temperature, voltage, current, totalcurrent, rpm, count), force_mavlink1=force_mavlink1)

## esc_telemetry_29_to_32_encode
    def esc_telemetry_29_to_32_encode(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int]) -> MAVLink_esc_telemetry_29_to_32_message:
        """
        ESC Telemetry Data for ESCs 29 to 32, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        return MAVLink_esc_telemetry_29_to_32_message(temperature, voltage, current, totalcurrent, rpm, count)

## esc_telemetry_29_to_32_send
    def esc_telemetry_29_to_32_send(self, temperature: Sequence[int], voltage: Sequence[int], current: Sequence[int], totalcurrent: Sequence[int], rpm: Sequence[int], count: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        ESC Telemetry Data for ESCs 29 to 32, matching data sent by BLHeli
        ESCs.

        temperature               : Temperature. [degC] (type:uint8_t)
        voltage                   : Voltage. [cV] (type:uint16_t)
        current                   : Current. [cA] (type:uint16_t)
        totalcurrent              : Total current. [mAh] (type:uint16_t)
        rpm                       : RPM (eRPM). [rpm] (type:uint16_t)
        count                     : count of telemetry packets received (wraps at 65535). (type:uint16_t)

        """
        self.send(self.esc_telemetry_29_to_32_encode(temperature, voltage, current, totalcurrent, rpm, count), force_mavlink1=force_mavlink1)

## sys_status_encode
    def sys_status_encode(self, onboard_control_sensors_present: int, onboard_control_sensors_enabled: int, onboard_control_sensors_health: int, load: int, voltage_battery: int, current_battery: int, battery_remaining: int, drop_rate_comm: int, errors_comm: int, errors_count1: int, errors_count2: int, errors_count3: int, errors_count4: int) -> MAVLink_sys_status_message:
        """
        The general system state. If the system is following the MAVLink
        standard, the system state is mainly defined by three
        orthogonal states/modes: The system mode, which is either
        LOCKED (motors shut down and locked), MANUAL (system under RC
        control), GUIDED (system with autonomous position control,
        position setpoint controlled manually) or AUTO (system guided
        by path/waypoint planner). The NAV_MODE defined the current
        flight state: LIFTOFF (often an open-loop maneuver), LANDING,
        WAYPOINTS or VECTOR. This represents the internal navigation
        state machine. The system status shows whether the system is
        currently active or not and if an emergency occurred. During
        the CRITICAL and EMERGENCY states the MAV is still considered
        to be active, but should start emergency procedures
        autonomously. After a failure occurred it should first move
        from active to critical to allow manual intervention and then
        move to emergency after a certain timeout.

        onboard_control_sensors_present        : Bitmap showing which onboard controllers and sensors are present. Value of 0: not present. Value of 1: present. (type:uint32_t, values:MAV_SYS_STATUS_SENSOR)
        onboard_control_sensors_enabled        : Bitmap showing which onboard controllers and sensors are enabled:  Value of 0: not enabled. Value of 1: enabled. (type:uint32_t, values:MAV_SYS_STATUS_SENSOR)
        onboard_control_sensors_health        : Bitmap showing which onboard controllers and sensors have an error (or are operational). Value of 0: error. Value of 1: healthy. (type:uint32_t, values:MAV_SYS_STATUS_SENSOR)
        load                      : Maximum usage in percent of the mainloop time. Values: [0-1000] - should always be below 1000 [d%] (type:uint16_t)
        voltage_battery           : Battery voltage, UINT16_MAX: Voltage not sent by autopilot [mV] (type:uint16_t)
        current_battery           : Battery current, -1: Current not sent by autopilot [cA] (type:int16_t)
        battery_remaining         : Battery energy remaining, -1: Battery remaining energy not sent by autopilot [%] (type:int8_t)
        drop_rate_comm            : Communication drop rate, (UART, I2C, SPI, CAN), dropped packets on all links (packets that were corrupted on reception on the MAV) [c%] (type:uint16_t)
        errors_comm               : Communication errors (UART, I2C, SPI, CAN), dropped packets on all links (packets that were corrupted on reception on the MAV) (type:uint16_t)
        errors_count1             : Autopilot-specific errors (type:uint16_t)
        errors_count2             : Autopilot-specific errors (type:uint16_t)
        errors_count3             : Autopilot-specific errors (type:uint16_t)
        errors_count4             : Autopilot-specific errors (type:uint16_t)

        """
        return MAVLink_sys_status_message(onboard_control_sensors_present, onboard_control_sensors_enabled, onboard_control_sensors_health, load, voltage_battery, current_battery, battery_remaining, drop_rate_comm, errors_comm, errors_count1, errors_count2, errors_count3, errors_count4)

## sys_status_send
    def sys_status_send(self, onboard_control_sensors_present: int, onboard_control_sensors_enabled: int, onboard_control_sensors_health: int, load: int, voltage_battery: int, current_battery: int, battery_remaining: int, drop_rate_comm: int, errors_comm: int, errors_count1: int, errors_count2: int, errors_count3: int, errors_count4: int, force_mavlink1: bool = False) -> None:
        """
        The general system state. If the system is following the MAVLink
        standard, the system state is mainly defined by three
        orthogonal states/modes: The system mode, which is either
        LOCKED (motors shut down and locked), MANUAL (system under RC
        control), GUIDED (system with autonomous position control,
        position setpoint controlled manually) or AUTO (system guided
        by path/waypoint planner). The NAV_MODE defined the current
        flight state: LIFTOFF (often an open-loop maneuver), LANDING,
        WAYPOINTS or VECTOR. This represents the internal navigation
        state machine. The system status shows whether the system is
        currently active or not and if an emergency occurred. During
        the CRITICAL and EMERGENCY states the MAV is still considered
        to be active, but should start emergency procedures
        autonomously. After a failure occurred it should first move
        from active to critical to allow manual intervention and then
        move to emergency after a certain timeout.

        onboard_control_sensors_present        : Bitmap showing which onboard controllers and sensors are present. Value of 0: not present. Value of 1: present. (type:uint32_t, values:MAV_SYS_STATUS_SENSOR)
        onboard_control_sensors_enabled        : Bitmap showing which onboard controllers and sensors are enabled:  Value of 0: not enabled. Value of 1: enabled. (type:uint32_t, values:MAV_SYS_STATUS_SENSOR)
        onboard_control_sensors_health        : Bitmap showing which onboard controllers and sensors have an error (or are operational). Value of 0: error. Value of 1: healthy. (type:uint32_t, values:MAV_SYS_STATUS_SENSOR)
        load                      : Maximum usage in percent of the mainloop time. Values: [0-1000] - should always be below 1000 [d%] (type:uint16_t)
        voltage_battery           : Battery voltage, UINT16_MAX: Voltage not sent by autopilot [mV] (type:uint16_t)
        current_battery           : Battery current, -1: Current not sent by autopilot [cA] (type:int16_t)
        battery_remaining         : Battery energy remaining, -1: Battery remaining energy not sent by autopilot [%] (type:int8_t)
        drop_rate_comm            : Communication drop rate, (UART, I2C, SPI, CAN), dropped packets on all links (packets that were corrupted on reception on the MAV) [c%] (type:uint16_t)
        errors_comm               : Communication errors (UART, I2C, SPI, CAN), dropped packets on all links (packets that were corrupted on reception on the MAV) (type:uint16_t)
        errors_count1             : Autopilot-specific errors (type:uint16_t)
        errors_count2             : Autopilot-specific errors (type:uint16_t)
        errors_count3             : Autopilot-specific errors (type:uint16_t)
        errors_count4             : Autopilot-specific errors (type:uint16_t)

        """
        self.send(self.sys_status_encode(onboard_control_sensors_present, onboard_control_sensors_enabled, onboard_control_sensors_health, load, voltage_battery, current_battery, battery_remaining, drop_rate_comm, errors_comm, errors_count1, errors_count2, errors_count3, errors_count4), force_mavlink1=force_mavlink1)

## system_time_encode
    def system_time_encode(self, time_unix_usec: int, time_boot_ms: int) -> MAVLink_system_time_message:
        """
        The system time is the time of the master clock, typically the
        computer clock of the main onboard computer.

        time_unix_usec            : Timestamp (UNIX epoch time). [us] (type:uint64_t)
        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)

        """
        return MAVLink_system_time_message(time_unix_usec, time_boot_ms)

## system_time_send
    def system_time_send(self, time_unix_usec: int, time_boot_ms: int, force_mavlink1: bool = False) -> None:
        """
        The system time is the time of the master clock, typically the
        computer clock of the main onboard computer.

        time_unix_usec            : Timestamp (UNIX epoch time). [us] (type:uint64_t)
        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)

        """
        self.send(self.system_time_encode(time_unix_usec, time_boot_ms), force_mavlink1=force_mavlink1)

## ping_encode
    def ping_encode(self, time_usec: int, seq: int, target_system: int, target_component: int) -> MAVLink_ping_message:
        """
        A ping message either requesting or responding to a ping. This allows
        to measure the system latencies, including serial port, radio
        modem and UDP connections. The ping microservice is documented
        at https://mavlink.io/en/services/ping.html

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        seq                       : PING sequence (type:uint32_t)
        target_system             : 0: request ping from all receiving systems. If greater than 0: message is a ping response and number is the system id of the requesting system (type:uint8_t)
        target_component          : 0: request ping from all receiving components. If greater than 0: message is a ping response and number is the component id of the requesting component. (type:uint8_t)

        """
        return MAVLink_ping_message(time_usec, seq, target_system, target_component)

## ping_send
    def ping_send(self, time_usec: int, seq: int, target_system: int, target_component: int, force_mavlink1: bool = False) -> None:
        """
        A ping message either requesting or responding to a ping. This allows
        to measure the system latencies, including serial port, radio
        modem and UDP connections. The ping microservice is documented
        at https://mavlink.io/en/services/ping.html

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        seq                       : PING sequence (type:uint32_t)
        target_system             : 0: request ping from all receiving systems. If greater than 0: message is a ping response and number is the system id of the requesting system (type:uint8_t)
        target_component          : 0: request ping from all receiving components. If greater than 0: message is a ping response and number is the component id of the requesting component. (type:uint8_t)

        """
        self.send(self.ping_encode(time_usec, seq, target_system, target_component), force_mavlink1=force_mavlink1)

## change_operator_control_encode
    def change_operator_control_encode(self, target_system: int, control_request: int, version: int, passkey: bytes) -> MAVLink_change_operator_control_message:
        """
        Request to control this MAV

        target_system             : System the GCS requests control for (type:uint8_t)
        control_request           : 0: request control of this MAV, 1: Release control of this MAV (type:uint8_t)
        version                   : 0: key as plaintext, 1-255: future, different hashing/encryption variants. The GCS should in general use the safest mode possible initially and then gradually move down the encryption level if it gets a NACK message indicating an encryption mismatch. [rad] (type:uint8_t)
        passkey                   : Password / Key, depending on version plaintext or encrypted. 25 or less characters, NULL terminated. The characters may involve A-Z, a-z, 0-9, and "!?,.-" (type:char)

        """
        return MAVLink_change_operator_control_message(target_system, control_request, version, passkey)

## change_operator_control_send
    def change_operator_control_send(self, target_system: int, control_request: int, version: int, passkey: bytes, force_mavlink1: bool = False) -> None:
        """
        Request to control this MAV

        target_system             : System the GCS requests control for (type:uint8_t)
        control_request           : 0: request control of this MAV, 1: Release control of this MAV (type:uint8_t)
        version                   : 0: key as plaintext, 1-255: future, different hashing/encryption variants. The GCS should in general use the safest mode possible initially and then gradually move down the encryption level if it gets a NACK message indicating an encryption mismatch. [rad] (type:uint8_t)
        passkey                   : Password / Key, depending on version plaintext or encrypted. 25 or less characters, NULL terminated. The characters may involve A-Z, a-z, 0-9, and "!?,.-" (type:char)

        """
        self.send(self.change_operator_control_encode(target_system, control_request, version, passkey), force_mavlink1=force_mavlink1)

## change_operator_control_ack_encode
    def change_operator_control_ack_encode(self, gcs_system_id: int, control_request: int, ack: int) -> MAVLink_change_operator_control_ack_message:
        """
        Accept / deny control of this MAV

        gcs_system_id             : ID of the GCS this message (type:uint8_t)
        control_request           : 0: request control of this MAV, 1: Release control of this MAV (type:uint8_t)
        ack                       : 0: ACK, 1: NACK: Wrong passkey, 2: NACK: Unsupported passkey encryption method, 3: NACK: Already under control (type:uint8_t)

        """
        return MAVLink_change_operator_control_ack_message(gcs_system_id, control_request, ack)

## change_operator_control_ack_send
    def change_operator_control_ack_send(self, gcs_system_id: int, control_request: int, ack: int, force_mavlink1: bool = False) -> None:
        """
        Accept / deny control of this MAV

        gcs_system_id             : ID of the GCS this message (type:uint8_t)
        control_request           : 0: request control of this MAV, 1: Release control of this MAV (type:uint8_t)
        ack                       : 0: ACK, 1: NACK: Wrong passkey, 2: NACK: Unsupported passkey encryption method, 3: NACK: Already under control (type:uint8_t)

        """
        self.send(self.change_operator_control_ack_encode(gcs_system_id, control_request, ack), force_mavlink1=force_mavlink1)

## auth_key_encode
    def auth_key_encode(self, key: bytes) -> MAVLink_auth_key_message:
        """
        Emit an encrypted signature / key identifying this system. PLEASE
        NOTE: This protocol has been kept simple, so transmitting the
        key requires an encrypted channel for true safety.

        key                       : key (type:char)

        """
        return MAVLink_auth_key_message(key)

## auth_key_send
    def auth_key_send(self, key: bytes, force_mavlink1: bool = False) -> None:
        """
        Emit an encrypted signature / key identifying this system. PLEASE
        NOTE: This protocol has been kept simple, so transmitting the
        key requires an encrypted channel for true safety.

        key                       : key (type:char)

        """
        self.send(self.auth_key_encode(key), force_mavlink1=force_mavlink1)

## set_mode_encode
    def set_mode_encode(self, target_system: int, base_mode: int, custom_mode: int) -> MAVLink_set_mode_message:
        """
        Set the system mode, as defined by enum MAV_MODE. There is no target
        component id as the mode is by definition for the overall
        aircraft, not only for one component.

        target_system             : The system setting the mode (type:uint8_t)
        base_mode                 : The new base mode. (type:uint8_t, values:MAV_MODE)
        custom_mode               : The new autopilot-specific mode. This field can be ignored by an autopilot. (type:uint32_t)

        """
        return MAVLink_set_mode_message(target_system, base_mode, custom_mode)

## set_mode_send
    def set_mode_send(self, target_system: int, base_mode: int, custom_mode: int, force_mavlink1: bool = False) -> None:
        """
        Set the system mode, as defined by enum MAV_MODE. There is no target
        component id as the mode is by definition for the overall
        aircraft, not only for one component.

        target_system             : The system setting the mode (type:uint8_t)
        base_mode                 : The new base mode. (type:uint8_t, values:MAV_MODE)
        custom_mode               : The new autopilot-specific mode. This field can be ignored by an autopilot. (type:uint32_t)

        """
        self.send(self.set_mode_encode(target_system, base_mode, custom_mode), force_mavlink1=force_mavlink1)

## param_request_read_encode
    def param_request_read_encode(self, target_system: int, target_component: int, param_id: bytes, param_index: int) -> MAVLink_param_request_read_message:
        """
        Request to read the onboard parameter with the param_id string id.
        Onboard parameters are stored as key[const char*] ->
        value[float]. This allows to send a parameter to any other
        component (such as the GCS) without the need of previous
        knowledge of possible parameter names. Thus the same GCS can
        store different parameters for different autopilots. See also
        https://mavlink.io/en/services/parameter.html for a full
        documentation of QGroundControl and IMU code.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_index               : Parameter index. Send -1 to use the param ID field as identifier (else the param id will be ignored) (type:int16_t)

        """
        return MAVLink_param_request_read_message(target_system, target_component, param_id, param_index)

## param_request_read_send
    def param_request_read_send(self, target_system: int, target_component: int, param_id: bytes, param_index: int, force_mavlink1: bool = False) -> None:
        """
        Request to read the onboard parameter with the param_id string id.
        Onboard parameters are stored as key[const char*] ->
        value[float]. This allows to send a parameter to any other
        component (such as the GCS) without the need of previous
        knowledge of possible parameter names. Thus the same GCS can
        store different parameters for different autopilots. See also
        https://mavlink.io/en/services/parameter.html for a full
        documentation of QGroundControl and IMU code.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_index               : Parameter index. Send -1 to use the param ID field as identifier (else the param id will be ignored) (type:int16_t)

        """
        self.send(self.param_request_read_encode(target_system, target_component, param_id, param_index), force_mavlink1=force_mavlink1)

## param_request_list_encode
    def param_request_list_encode(self, target_system: int, target_component: int) -> MAVLink_param_request_list_message:
        """
        Request all parameters of this component. After this request, all
        parameters are emitted. The parameter microservice is
        documented at https://mavlink.io/en/services/parameter.html

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)

        """
        return MAVLink_param_request_list_message(target_system, target_component)

## param_request_list_send
    def param_request_list_send(self, target_system: int, target_component: int, force_mavlink1: bool = False) -> None:
        """
        Request all parameters of this component. After this request, all
        parameters are emitted. The parameter microservice is
        documented at https://mavlink.io/en/services/parameter.html

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)

        """
        self.send(self.param_request_list_encode(target_system, target_component), force_mavlink1=force_mavlink1)

## param_value_encode
    def param_value_encode(self, param_id: bytes, param_value: float, param_type: int, param_count: int, param_index: int) -> MAVLink_param_value_message:
        """
        Emit the value of a onboard parameter. The inclusion of param_count
        and param_index in the message allows the recipient to keep
        track of received parameters and allows him to re-request
        missing parameters after a loss or timeout. The parameter
        microservice is documented at
        https://mavlink.io/en/services/parameter.html

        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Onboard parameter value (type:float)
        param_type                : Onboard parameter type. (type:uint8_t, values:MAV_PARAM_TYPE)
        param_count               : Total number of onboard parameters (type:uint16_t)
        param_index               : Index of this onboard parameter (type:uint16_t)

        """
        return MAVLink_param_value_message(param_id, param_value, param_type, param_count, param_index)

## param_value_send
    def param_value_send(self, param_id: bytes, param_value: float, param_type: int, param_count: int, param_index: int, force_mavlink1: bool = False) -> None:
        """
        Emit the value of a onboard parameter. The inclusion of param_count
        and param_index in the message allows the recipient to keep
        track of received parameters and allows him to re-request
        missing parameters after a loss or timeout. The parameter
        microservice is documented at
        https://mavlink.io/en/services/parameter.html

        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Onboard parameter value (type:float)
        param_type                : Onboard parameter type. (type:uint8_t, values:MAV_PARAM_TYPE)
        param_count               : Total number of onboard parameters (type:uint16_t)
        param_index               : Index of this onboard parameter (type:uint16_t)

        """
        self.send(self.param_value_encode(param_id, param_value, param_type, param_count, param_index), force_mavlink1=force_mavlink1)

## param_set_encode
    def param_set_encode(self, target_system: int, target_component: int, param_id: bytes, param_value: float, param_type: int) -> MAVLink_param_set_message:
        """
        Set a parameter value (write new value to permanent storage).
        The receiving component should acknowledge the new parameter
        value by broadcasting a PARAM_VALUE message (broadcasting
        ensures that multiple GCS all have an up-to-date list of all
        parameters). If the sending GCS did not receive a PARAM_VALUE
        within its timeout time, it should re-send the PARAM_SET
        message. The parameter microservice is documented at
        https://mavlink.io/en/services/parameter.html.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Onboard parameter value (type:float)
        param_type                : Onboard parameter type. (type:uint8_t, values:MAV_PARAM_TYPE)

        """
        return MAVLink_param_set_message(target_system, target_component, param_id, param_value, param_type)

## param_set_send
    def param_set_send(self, target_system: int, target_component: int, param_id: bytes, param_value: float, param_type: int, force_mavlink1: bool = False) -> None:
        """
        Set a parameter value (write new value to permanent storage).
        The receiving component should acknowledge the new parameter
        value by broadcasting a PARAM_VALUE message (broadcasting
        ensures that multiple GCS all have an up-to-date list of all
        parameters). If the sending GCS did not receive a PARAM_VALUE
        within its timeout time, it should re-send the PARAM_SET
        message. The parameter microservice is documented at
        https://mavlink.io/en/services/parameter.html.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Onboard parameter value (type:float)
        param_type                : Onboard parameter type. (type:uint8_t, values:MAV_PARAM_TYPE)

        """
        self.send(self.param_set_encode(target_system, target_component, param_id, param_value, param_type), force_mavlink1=force_mavlink1)

## gps_raw_int_encode
    def gps_raw_int_encode(self, time_usec: int, fix_type: int, lat: int, lon: int, alt: int, eph: int, epv: int, vel: int, cog: int, satellites_visible: int, alt_ellipsoid: int = 0, h_acc: int = 0, v_acc: int = 0, vel_acc: int = 0, hdg_acc: int = 0, yaw: int = 0) -> MAVLink_gps_raw_int_message:
        """
        The global position, as returned by the Global Positioning System
        (GPS). This is                 NOT the global position
        estimate of the system, but rather a RAW sensor value. See
        message GLOBAL_POSITION_INT for the global position estimate.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        fix_type                  : GPS fix type. (type:uint8_t, values:GPS_FIX_TYPE)
        lat                       : Latitude (WGS84, EGM96 ellipsoid) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84, EGM96 ellipsoid) [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Positive for up. Note that virtually all GPS modules provide the MSL altitude in addition to the WGS84 altitude. [mm] (type:int32_t)
        eph                       : GPS HDOP horizontal dilution of position (unitless * 100). If unknown, set to: UINT16_MAX (type:uint16_t)
        epv                       : GPS VDOP vertical dilution of position (unitless * 100). If unknown, set to: UINT16_MAX (type:uint16_t)
        vel                       : GPS ground speed. If unknown, set to: UINT16_MAX [cm/s] (type:uint16_t)
        cog                       : Course over ground (NOT heading, but direction of movement) in degrees * 100, 0.0..359.99 degrees. If unknown, set to: UINT16_MAX [cdeg] (type:uint16_t)
        satellites_visible        : Number of satellites visible. If unknown, set to UINT8_MAX (type:uint8_t)
        alt_ellipsoid             : Altitude (above WGS84, EGM96 ellipsoid). Positive for up. [mm] (type:int32_t)
        h_acc                     : Position uncertainty. [mm] (type:uint32_t)
        v_acc                     : Altitude uncertainty. [mm] (type:uint32_t)
        vel_acc                   : Speed uncertainty. [mm/s] (type:uint32_t)
        hdg_acc                   : Heading / track uncertainty [degE5] (type:uint32_t)
        yaw                       : Yaw in earth frame from north. Use 0 if this GPS does not provide yaw. Use UINT16_MAX if this GPS is configured to provide yaw and is currently unable to provide it. Use 36000 for north. [cdeg] (type:uint16_t)

        """
        return MAVLink_gps_raw_int_message(time_usec, fix_type, lat, lon, alt, eph, epv, vel, cog, satellites_visible, alt_ellipsoid, h_acc, v_acc, vel_acc, hdg_acc, yaw)

## gps_raw_int_send
    def gps_raw_int_send(self, time_usec: int, fix_type: int, lat: int, lon: int, alt: int, eph: int, epv: int, vel: int, cog: int, satellites_visible: int, alt_ellipsoid: int = 0, h_acc: int = 0, v_acc: int = 0, vel_acc: int = 0, hdg_acc: int = 0, yaw: int = 0, force_mavlink1: bool = False) -> None:
        """
        The global position, as returned by the Global Positioning System
        (GPS). This is                 NOT the global position
        estimate of the system, but rather a RAW sensor value. See
        message GLOBAL_POSITION_INT for the global position estimate.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        fix_type                  : GPS fix type. (type:uint8_t, values:GPS_FIX_TYPE)
        lat                       : Latitude (WGS84, EGM96 ellipsoid) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84, EGM96 ellipsoid) [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Positive for up. Note that virtually all GPS modules provide the MSL altitude in addition to the WGS84 altitude. [mm] (type:int32_t)
        eph                       : GPS HDOP horizontal dilution of position (unitless * 100). If unknown, set to: UINT16_MAX (type:uint16_t)
        epv                       : GPS VDOP vertical dilution of position (unitless * 100). If unknown, set to: UINT16_MAX (type:uint16_t)
        vel                       : GPS ground speed. If unknown, set to: UINT16_MAX [cm/s] (type:uint16_t)
        cog                       : Course over ground (NOT heading, but direction of movement) in degrees * 100, 0.0..359.99 degrees. If unknown, set to: UINT16_MAX [cdeg] (type:uint16_t)
        satellites_visible        : Number of satellites visible. If unknown, set to UINT8_MAX (type:uint8_t)
        alt_ellipsoid             : Altitude (above WGS84, EGM96 ellipsoid). Positive for up. [mm] (type:int32_t)
        h_acc                     : Position uncertainty. [mm] (type:uint32_t)
        v_acc                     : Altitude uncertainty. [mm] (type:uint32_t)
        vel_acc                   : Speed uncertainty. [mm/s] (type:uint32_t)
        hdg_acc                   : Heading / track uncertainty [degE5] (type:uint32_t)
        yaw                       : Yaw in earth frame from north. Use 0 if this GPS does not provide yaw. Use UINT16_MAX if this GPS is configured to provide yaw and is currently unable to provide it. Use 36000 for north. [cdeg] (type:uint16_t)

        """
        self.send(self.gps_raw_int_encode(time_usec, fix_type, lat, lon, alt, eph, epv, vel, cog, satellites_visible, alt_ellipsoid, h_acc, v_acc, vel_acc, hdg_acc, yaw), force_mavlink1=force_mavlink1)

## gps_status_encode
    def gps_status_encode(self, satellites_visible: int, satellite_prn: Sequence[int], satellite_used: Sequence[int], satellite_elevation: Sequence[int], satellite_azimuth: Sequence[int], satellite_snr: Sequence[int]) -> MAVLink_gps_status_message:
        """
        The positioning status, as reported by GPS. This message is intended
        to display status information about each satellite visible to
        the receiver. See message GLOBAL_POSITION_INT for the global
        position estimate. This message can contain information for up
        to 20 satellites.

        satellites_visible        : Number of satellites visible (type:uint8_t)
        satellite_prn             : Global satellite ID (type:uint8_t)
        satellite_used            : 0: Satellite not used, 1: used for localization (type:uint8_t)
        satellite_elevation        : Elevation (0: right on top of receiver, 90: on the horizon) of satellite [deg] (type:uint8_t)
        satellite_azimuth         : Direction of satellite, 0: 0 deg, 255: 360 deg. [deg] (type:uint8_t)
        satellite_snr             : Signal to noise ratio of satellite [dB] (type:uint8_t)

        """
        return MAVLink_gps_status_message(satellites_visible, satellite_prn, satellite_used, satellite_elevation, satellite_azimuth, satellite_snr)

## gps_status_send
    def gps_status_send(self, satellites_visible: int, satellite_prn: Sequence[int], satellite_used: Sequence[int], satellite_elevation: Sequence[int], satellite_azimuth: Sequence[int], satellite_snr: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        The positioning status, as reported by GPS. This message is intended
        to display status information about each satellite visible to
        the receiver. See message GLOBAL_POSITION_INT for the global
        position estimate. This message can contain information for up
        to 20 satellites.

        satellites_visible        : Number of satellites visible (type:uint8_t)
        satellite_prn             : Global satellite ID (type:uint8_t)
        satellite_used            : 0: Satellite not used, 1: used for localization (type:uint8_t)
        satellite_elevation        : Elevation (0: right on top of receiver, 90: on the horizon) of satellite [deg] (type:uint8_t)
        satellite_azimuth         : Direction of satellite, 0: 0 deg, 255: 360 deg. [deg] (type:uint8_t)
        satellite_snr             : Signal to noise ratio of satellite [dB] (type:uint8_t)

        """
        self.send(self.gps_status_encode(satellites_visible, satellite_prn, satellite_used, satellite_elevation, satellite_azimuth, satellite_snr), force_mavlink1=force_mavlink1)

## scaled_imu_encode
    def scaled_imu_encode(self, time_boot_ms: int, xacc: int, yacc: int, zacc: int, xgyro: int, ygyro: int, zgyro: int, xmag: int, ymag: int, zmag: int, temperature: int = 0) -> MAVLink_scaled_imu_message:
        """
        The RAW IMU readings for the usual 9DOF sensor setup. This message
        should contain the scaled values to the described units

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)
        xgyro                     : Angular speed around X axis [mrad/s] (type:int16_t)
        ygyro                     : Angular speed around Y axis [mrad/s] (type:int16_t)
        zgyro                     : Angular speed around Z axis [mrad/s] (type:int16_t)
        xmag                      : X Magnetic field [mgauss] (type:int16_t)
        ymag                      : Y Magnetic field [mgauss] (type:int16_t)
        zmag                      : Z Magnetic field [mgauss] (type:int16_t)
        temperature               : Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). [cdegC] (type:int16_t)

        """
        return MAVLink_scaled_imu_message(time_boot_ms, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, temperature)

## scaled_imu_send
    def scaled_imu_send(self, time_boot_ms: int, xacc: int, yacc: int, zacc: int, xgyro: int, ygyro: int, zgyro: int, xmag: int, ymag: int, zmag: int, temperature: int = 0, force_mavlink1: bool = False) -> None:
        """
        The RAW IMU readings for the usual 9DOF sensor setup. This message
        should contain the scaled values to the described units

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)
        xgyro                     : Angular speed around X axis [mrad/s] (type:int16_t)
        ygyro                     : Angular speed around Y axis [mrad/s] (type:int16_t)
        zgyro                     : Angular speed around Z axis [mrad/s] (type:int16_t)
        xmag                      : X Magnetic field [mgauss] (type:int16_t)
        ymag                      : Y Magnetic field [mgauss] (type:int16_t)
        zmag                      : Z Magnetic field [mgauss] (type:int16_t)
        temperature               : Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). [cdegC] (type:int16_t)

        """
        self.send(self.scaled_imu_encode(time_boot_ms, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, temperature), force_mavlink1=force_mavlink1)

## raw_imu_encode
    def raw_imu_encode(self, time_usec: int, xacc: int, yacc: int, zacc: int, xgyro: int, ygyro: int, zgyro: int, xmag: int, ymag: int, zmag: int, id: int = 0, temperature: int = 0) -> MAVLink_raw_imu_message:
        """
        The RAW IMU readings for a 9DOF sensor, which is identified by the id
        (default IMU1). This message should always contain the true
        raw values without any scaling to allow data capture and
        system debugging.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        xacc                      : X acceleration (raw) (type:int16_t)
        yacc                      : Y acceleration (raw) (type:int16_t)
        zacc                      : Z acceleration (raw) (type:int16_t)
        xgyro                     : Angular speed around X axis (raw) (type:int16_t)
        ygyro                     : Angular speed around Y axis (raw) (type:int16_t)
        zgyro                     : Angular speed around Z axis (raw) (type:int16_t)
        xmag                      : X Magnetic field (raw) (type:int16_t)
        ymag                      : Y Magnetic field (raw) (type:int16_t)
        zmag                      : Z Magnetic field (raw) (type:int16_t)
        id                        : Id. Ids are numbered from 0 and map to IMUs numbered from 1 (e.g. IMU1 will have a message with id=0) (type:uint8_t)
        temperature               : Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). [cdegC] (type:int16_t)

        """
        return MAVLink_raw_imu_message(time_usec, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, id, temperature)

## raw_imu_send
    def raw_imu_send(self, time_usec: int, xacc: int, yacc: int, zacc: int, xgyro: int, ygyro: int, zgyro: int, xmag: int, ymag: int, zmag: int, id: int = 0, temperature: int = 0, force_mavlink1: bool = False) -> None:
        """
        The RAW IMU readings for a 9DOF sensor, which is identified by the id
        (default IMU1). This message should always contain the true
        raw values without any scaling to allow data capture and
        system debugging.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        xacc                      : X acceleration (raw) (type:int16_t)
        yacc                      : Y acceleration (raw) (type:int16_t)
        zacc                      : Z acceleration (raw) (type:int16_t)
        xgyro                     : Angular speed around X axis (raw) (type:int16_t)
        ygyro                     : Angular speed around Y axis (raw) (type:int16_t)
        zgyro                     : Angular speed around Z axis (raw) (type:int16_t)
        xmag                      : X Magnetic field (raw) (type:int16_t)
        ymag                      : Y Magnetic field (raw) (type:int16_t)
        zmag                      : Z Magnetic field (raw) (type:int16_t)
        id                        : Id. Ids are numbered from 0 and map to IMUs numbered from 1 (e.g. IMU1 will have a message with id=0) (type:uint8_t)
        temperature               : Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). [cdegC] (type:int16_t)

        """
        self.send(self.raw_imu_encode(time_usec, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, id, temperature), force_mavlink1=force_mavlink1)

## raw_pressure_encode
    def raw_pressure_encode(self, time_usec: int, press_abs: int, press_diff1: int, press_diff2: int, temperature: int) -> MAVLink_raw_pressure_message:
        """
        The RAW pressure readings for the typical setup of one absolute
        pressure and one differential pressure sensor. The sensor
        values should be the raw, UNSCALED ADC values.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        press_abs                 : Absolute pressure (raw) (type:int16_t)
        press_diff1               : Differential pressure 1 (raw, 0 if nonexistent) (type:int16_t)
        press_diff2               : Differential pressure 2 (raw, 0 if nonexistent) (type:int16_t)
        temperature               : Raw Temperature measurement (raw) (type:int16_t)

        """
        return MAVLink_raw_pressure_message(time_usec, press_abs, press_diff1, press_diff2, temperature)

## raw_pressure_send
    def raw_pressure_send(self, time_usec: int, press_abs: int, press_diff1: int, press_diff2: int, temperature: int, force_mavlink1: bool = False) -> None:
        """
        The RAW pressure readings for the typical setup of one absolute
        pressure and one differential pressure sensor. The sensor
        values should be the raw, UNSCALED ADC values.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        press_abs                 : Absolute pressure (raw) (type:int16_t)
        press_diff1               : Differential pressure 1 (raw, 0 if nonexistent) (type:int16_t)
        press_diff2               : Differential pressure 2 (raw, 0 if nonexistent) (type:int16_t)
        temperature               : Raw Temperature measurement (raw) (type:int16_t)

        """
        self.send(self.raw_pressure_encode(time_usec, press_abs, press_diff1, press_diff2, temperature), force_mavlink1=force_mavlink1)

## scaled_pressure_encode
    def scaled_pressure_encode(self, time_boot_ms: int, press_abs: float, press_diff: float, temperature: int, temperature_press_diff: int = 0) -> MAVLink_scaled_pressure_message:
        """
        The pressure readings for the typical setup of one absolute and
        differential pressure sensor. The units are as specified in
        each field.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        press_abs                 : Absolute pressure [hPa] (type:float)
        press_diff                : Differential pressure 1 [hPa] (type:float)
        temperature               : Absolute pressure temperature [cdegC] (type:int16_t)
        temperature_press_diff        : Differential pressure temperature (0, if not available). Report values of 0 (or 1) as 1 cdegC. [cdegC] (type:int16_t)

        """
        return MAVLink_scaled_pressure_message(time_boot_ms, press_abs, press_diff, temperature, temperature_press_diff)

## scaled_pressure_send
    def scaled_pressure_send(self, time_boot_ms: int, press_abs: float, press_diff: float, temperature: int, temperature_press_diff: int = 0, force_mavlink1: bool = False) -> None:
        """
        The pressure readings for the typical setup of one absolute and
        differential pressure sensor. The units are as specified in
        each field.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        press_abs                 : Absolute pressure [hPa] (type:float)
        press_diff                : Differential pressure 1 [hPa] (type:float)
        temperature               : Absolute pressure temperature [cdegC] (type:int16_t)
        temperature_press_diff        : Differential pressure temperature (0, if not available). Report values of 0 (or 1) as 1 cdegC. [cdegC] (type:int16_t)

        """
        self.send(self.scaled_pressure_encode(time_boot_ms, press_abs, press_diff, temperature, temperature_press_diff), force_mavlink1=force_mavlink1)

## attitude_encode
    def attitude_encode(self, time_boot_ms: int, roll: float, pitch: float, yaw: float, rollspeed: float, pitchspeed: float, yawspeed: float) -> MAVLink_attitude_message:
        """
        The attitude in the aeronautical frame (right-handed, Z-down, X-front,
        Y-right).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        roll                      : Roll angle (-pi..+pi) [rad] (type:float)
        pitch                     : Pitch angle (-pi..+pi) [rad] (type:float)
        yaw                       : Yaw angle (-pi..+pi) [rad] (type:float)
        rollspeed                 : Roll angular speed [rad/s] (type:float)
        pitchspeed                : Pitch angular speed [rad/s] (type:float)
        yawspeed                  : Yaw angular speed [rad/s] (type:float)

        """
        return MAVLink_attitude_message(time_boot_ms, roll, pitch, yaw, rollspeed, pitchspeed, yawspeed)

## attitude_send
    def attitude_send(self, time_boot_ms: int, roll: float, pitch: float, yaw: float, rollspeed: float, pitchspeed: float, yawspeed: float, force_mavlink1: bool = False) -> None:
        """
        The attitude in the aeronautical frame (right-handed, Z-down, X-front,
        Y-right).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        roll                      : Roll angle (-pi..+pi) [rad] (type:float)
        pitch                     : Pitch angle (-pi..+pi) [rad] (type:float)
        yaw                       : Yaw angle (-pi..+pi) [rad] (type:float)
        rollspeed                 : Roll angular speed [rad/s] (type:float)
        pitchspeed                : Pitch angular speed [rad/s] (type:float)
        yawspeed                  : Yaw angular speed [rad/s] (type:float)

        """
        self.send(self.attitude_encode(time_boot_ms, roll, pitch, yaw, rollspeed, pitchspeed, yawspeed), force_mavlink1=force_mavlink1)

## attitude_quaternion_encode
    def attitude_quaternion_encode(self, time_boot_ms: int, q1: float, q2: float, q3: float, q4: float, rollspeed: float, pitchspeed: float, yawspeed: float, repr_offset_q: Sequence[float] = (0, 0, 0, 0)) -> MAVLink_attitude_quaternion_message:
        """
        The attitude in the aeronautical frame (right-handed, Z-down, X-front,
        Y-right), expressed as quaternion. Quaternion order is w, x,
        y, z and a zero rotation would be expressed as (1 0 0 0).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        q1                        : Quaternion component 1, w (1 in null-rotation) (type:float)
        q2                        : Quaternion component 2, x (0 in null-rotation) (type:float)
        q3                        : Quaternion component 3, y (0 in null-rotation) (type:float)
        q4                        : Quaternion component 4, z (0 in null-rotation) (type:float)
        rollspeed                 : Roll angular speed [rad/s] (type:float)
        pitchspeed                : Pitch angular speed [rad/s] (type:float)
        yawspeed                  : Yaw angular speed [rad/s] (type:float)
        repr_offset_q             : Rotation offset by which the attitude quaternion and angular speed vector should be rotated for user display (quaternion with [w, x, y, z] order, zero-rotation is [1, 0, 0, 0], send [0, 0, 0, 0] if field not supported). This field is intended for systems in which the reference attitude may change during flight. For example, tailsitters VTOLs rotate their reference attitude by 90 degrees between hover mode and fixed wing mode, thus repr_offset_q is equal to [1, 0, 0, 0] in hover mode and equal to [0.7071, 0, 0.7071, 0] in fixed wing mode. (type:float)

        """
        return MAVLink_attitude_quaternion_message(time_boot_ms, q1, q2, q3, q4, rollspeed, pitchspeed, yawspeed, repr_offset_q)

## attitude_quaternion_send
    def attitude_quaternion_send(self, time_boot_ms: int, q1: float, q2: float, q3: float, q4: float, rollspeed: float, pitchspeed: float, yawspeed: float, repr_offset_q: Sequence[float] = (0, 0, 0, 0), force_mavlink1: bool = False) -> None:
        """
        The attitude in the aeronautical frame (right-handed, Z-down, X-front,
        Y-right), expressed as quaternion. Quaternion order is w, x,
        y, z and a zero rotation would be expressed as (1 0 0 0).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        q1                        : Quaternion component 1, w (1 in null-rotation) (type:float)
        q2                        : Quaternion component 2, x (0 in null-rotation) (type:float)
        q3                        : Quaternion component 3, y (0 in null-rotation) (type:float)
        q4                        : Quaternion component 4, z (0 in null-rotation) (type:float)
        rollspeed                 : Roll angular speed [rad/s] (type:float)
        pitchspeed                : Pitch angular speed [rad/s] (type:float)
        yawspeed                  : Yaw angular speed [rad/s] (type:float)
        repr_offset_q             : Rotation offset by which the attitude quaternion and angular speed vector should be rotated for user display (quaternion with [w, x, y, z] order, zero-rotation is [1, 0, 0, 0], send [0, 0, 0, 0] if field not supported). This field is intended for systems in which the reference attitude may change during flight. For example, tailsitters VTOLs rotate their reference attitude by 90 degrees between hover mode and fixed wing mode, thus repr_offset_q is equal to [1, 0, 0, 0] in hover mode and equal to [0.7071, 0, 0.7071, 0] in fixed wing mode. (type:float)

        """
        self.send(self.attitude_quaternion_encode(time_boot_ms, q1, q2, q3, q4, rollspeed, pitchspeed, yawspeed, repr_offset_q), force_mavlink1=force_mavlink1)

## local_position_ned_encode
    def local_position_ned_encode(self, time_boot_ms: int, x: float, y: float, z: float, vx: float, vy: float, vz: float) -> MAVLink_local_position_ned_message:
        """
        The filtered local position (e.g. fused computer vision and
        accelerometers). Coordinate frame is right-handed, Z-axis down
        (aeronautical frame, NED / north-east-down convention)

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        x                         : X Position [m] (type:float)
        y                         : Y Position [m] (type:float)
        z                         : Z Position [m] (type:float)
        vx                        : X Speed [m/s] (type:float)
        vy                        : Y Speed [m/s] (type:float)
        vz                        : Z Speed [m/s] (type:float)

        """
        return MAVLink_local_position_ned_message(time_boot_ms, x, y, z, vx, vy, vz)

## local_position_ned_send
    def local_position_ned_send(self, time_boot_ms: int, x: float, y: float, z: float, vx: float, vy: float, vz: float, force_mavlink1: bool = False) -> None:
        """
        The filtered local position (e.g. fused computer vision and
        accelerometers). Coordinate frame is right-handed, Z-axis down
        (aeronautical frame, NED / north-east-down convention)

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        x                         : X Position [m] (type:float)
        y                         : Y Position [m] (type:float)
        z                         : Z Position [m] (type:float)
        vx                        : X Speed [m/s] (type:float)
        vy                        : Y Speed [m/s] (type:float)
        vz                        : Z Speed [m/s] (type:float)

        """
        self.send(self.local_position_ned_encode(time_boot_ms, x, y, z, vx, vy, vz), force_mavlink1=force_mavlink1)

## global_position_int_encode
    def global_position_int_encode(self, time_boot_ms: int, lat: int, lon: int, alt: int, relative_alt: int, vx: int, vy: int, vz: int, hdg: int) -> MAVLink_global_position_int_message:
        """
        The filtered global position (e.g. fused GPS and accelerometers). The
        position is in GPS-frame (right-handed, Z-up). It
        is designed as scaled integer message since the resolution of
        float is not sufficient.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        lat                       : Latitude, expressed [degE7] (type:int32_t)
        lon                       : Longitude, expressed [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Note that virtually all GPS modules provide both WGS84 and MSL. [mm] (type:int32_t)
        relative_alt              : Altitude above home [mm] (type:int32_t)
        vx                        : Ground X Speed (Latitude, positive north) [cm/s] (type:int16_t)
        vy                        : Ground Y Speed (Longitude, positive east) [cm/s] (type:int16_t)
        vz                        : Ground Z Speed (Altitude, positive down) [cm/s] (type:int16_t)
        hdg                       : Vehicle heading (yaw angle), 0.0..359.99 degrees. If unknown, set to: UINT16_MAX [cdeg] (type:uint16_t)

        """
        return MAVLink_global_position_int_message(time_boot_ms, lat, lon, alt, relative_alt, vx, vy, vz, hdg)

## global_position_int_send
    def global_position_int_send(self, time_boot_ms: int, lat: int, lon: int, alt: int, relative_alt: int, vx: int, vy: int, vz: int, hdg: int, force_mavlink1: bool = False) -> None:
        """
        The filtered global position (e.g. fused GPS and accelerometers). The
        position is in GPS-frame (right-handed, Z-up). It
        is designed as scaled integer message since the resolution of
        float is not sufficient.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        lat                       : Latitude, expressed [degE7] (type:int32_t)
        lon                       : Longitude, expressed [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Note that virtually all GPS modules provide both WGS84 and MSL. [mm] (type:int32_t)
        relative_alt              : Altitude above home [mm] (type:int32_t)
        vx                        : Ground X Speed (Latitude, positive north) [cm/s] (type:int16_t)
        vy                        : Ground Y Speed (Longitude, positive east) [cm/s] (type:int16_t)
        vz                        : Ground Z Speed (Altitude, positive down) [cm/s] (type:int16_t)
        hdg                       : Vehicle heading (yaw angle), 0.0..359.99 degrees. If unknown, set to: UINT16_MAX [cdeg] (type:uint16_t)

        """
        self.send(self.global_position_int_encode(time_boot_ms, lat, lon, alt, relative_alt, vx, vy, vz, hdg), force_mavlink1=force_mavlink1)

## rc_channels_scaled_encode
    def rc_channels_scaled_encode(self, time_boot_ms: int, port: int, chan1_scaled: int, chan2_scaled: int, chan3_scaled: int, chan4_scaled: int, chan5_scaled: int, chan6_scaled: int, chan7_scaled: int, chan8_scaled: int, rssi: int) -> MAVLink_rc_channels_scaled_message:
        """
        The scaled values of the RC channels received: (-100%) -10000, (0%) 0,
        (100%) 10000. Channels that are inactive should be set to
        UINT16_MAX.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        port                      : Servo output port (set of 8 outputs = 1 port). Flight stacks running on Pixhawk should use: 0 = MAIN, 1 = AUX. (type:uint8_t)
        chan1_scaled              : RC channel 1 value scaled. (type:int16_t)
        chan2_scaled              : RC channel 2 value scaled. (type:int16_t)
        chan3_scaled              : RC channel 3 value scaled. (type:int16_t)
        chan4_scaled              : RC channel 4 value scaled. (type:int16_t)
        chan5_scaled              : RC channel 5 value scaled. (type:int16_t)
        chan6_scaled              : RC channel 6 value scaled. (type:int16_t)
        chan7_scaled              : RC channel 7 value scaled. (type:int16_t)
        chan8_scaled              : RC channel 8 value scaled. (type:int16_t)
        rssi                      : Receive signal strength indicator in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)

        """
        return MAVLink_rc_channels_scaled_message(time_boot_ms, port, chan1_scaled, chan2_scaled, chan3_scaled, chan4_scaled, chan5_scaled, chan6_scaled, chan7_scaled, chan8_scaled, rssi)

## rc_channels_scaled_send
    def rc_channels_scaled_send(self, time_boot_ms: int, port: int, chan1_scaled: int, chan2_scaled: int, chan3_scaled: int, chan4_scaled: int, chan5_scaled: int, chan6_scaled: int, chan7_scaled: int, chan8_scaled: int, rssi: int, force_mavlink1: bool = False) -> None:
        """
        The scaled values of the RC channels received: (-100%) -10000, (0%) 0,
        (100%) 10000. Channels that are inactive should be set to
        UINT16_MAX.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        port                      : Servo output port (set of 8 outputs = 1 port). Flight stacks running on Pixhawk should use: 0 = MAIN, 1 = AUX. (type:uint8_t)
        chan1_scaled              : RC channel 1 value scaled. (type:int16_t)
        chan2_scaled              : RC channel 2 value scaled. (type:int16_t)
        chan3_scaled              : RC channel 3 value scaled. (type:int16_t)
        chan4_scaled              : RC channel 4 value scaled. (type:int16_t)
        chan5_scaled              : RC channel 5 value scaled. (type:int16_t)
        chan6_scaled              : RC channel 6 value scaled. (type:int16_t)
        chan7_scaled              : RC channel 7 value scaled. (type:int16_t)
        chan8_scaled              : RC channel 8 value scaled. (type:int16_t)
        rssi                      : Receive signal strength indicator in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)

        """
        self.send(self.rc_channels_scaled_encode(time_boot_ms, port, chan1_scaled, chan2_scaled, chan3_scaled, chan4_scaled, chan5_scaled, chan6_scaled, chan7_scaled, chan8_scaled, rssi), force_mavlink1=force_mavlink1)

## rc_channels_raw_encode
    def rc_channels_raw_encode(self, time_boot_ms: int, port: int, chan1_raw: int, chan2_raw: int, chan3_raw: int, chan4_raw: int, chan5_raw: int, chan6_raw: int, chan7_raw: int, chan8_raw: int, rssi: int) -> MAVLink_rc_channels_raw_message:
        """
        The RAW values of the RC channels received. The standard PPM
        modulation is as follows: 1000 microseconds: 0%, 2000
        microseconds: 100%. A value of UINT16_MAX implies the channel
        is unused. Individual receivers/transmitters might violate
        this specification.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        port                      : Servo output port (set of 8 outputs = 1 port). Flight stacks running on Pixhawk should use: 0 = MAIN, 1 = AUX. (type:uint8_t)
        chan1_raw                 : RC channel 1 value. [us] (type:uint16_t)
        chan2_raw                 : RC channel 2 value. [us] (type:uint16_t)
        chan3_raw                 : RC channel 3 value. [us] (type:uint16_t)
        chan4_raw                 : RC channel 4 value. [us] (type:uint16_t)
        chan5_raw                 : RC channel 5 value. [us] (type:uint16_t)
        chan6_raw                 : RC channel 6 value. [us] (type:uint16_t)
        chan7_raw                 : RC channel 7 value. [us] (type:uint16_t)
        chan8_raw                 : RC channel 8 value. [us] (type:uint16_t)
        rssi                      : Receive signal strength indicator in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)

        """
        return MAVLink_rc_channels_raw_message(time_boot_ms, port, chan1_raw, chan2_raw, chan3_raw, chan4_raw, chan5_raw, chan6_raw, chan7_raw, chan8_raw, rssi)

## rc_channels_raw_send
    def rc_channels_raw_send(self, time_boot_ms: int, port: int, chan1_raw: int, chan2_raw: int, chan3_raw: int, chan4_raw: int, chan5_raw: int, chan6_raw: int, chan7_raw: int, chan8_raw: int, rssi: int, force_mavlink1: bool = False) -> None:
        """
        The RAW values of the RC channels received. The standard PPM
        modulation is as follows: 1000 microseconds: 0%, 2000
        microseconds: 100%. A value of UINT16_MAX implies the channel
        is unused. Individual receivers/transmitters might violate
        this specification.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        port                      : Servo output port (set of 8 outputs = 1 port). Flight stacks running on Pixhawk should use: 0 = MAIN, 1 = AUX. (type:uint8_t)
        chan1_raw                 : RC channel 1 value. [us] (type:uint16_t)
        chan2_raw                 : RC channel 2 value. [us] (type:uint16_t)
        chan3_raw                 : RC channel 3 value. [us] (type:uint16_t)
        chan4_raw                 : RC channel 4 value. [us] (type:uint16_t)
        chan5_raw                 : RC channel 5 value. [us] (type:uint16_t)
        chan6_raw                 : RC channel 6 value. [us] (type:uint16_t)
        chan7_raw                 : RC channel 7 value. [us] (type:uint16_t)
        chan8_raw                 : RC channel 8 value. [us] (type:uint16_t)
        rssi                      : Receive signal strength indicator in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)

        """
        self.send(self.rc_channels_raw_encode(time_boot_ms, port, chan1_raw, chan2_raw, chan3_raw, chan4_raw, chan5_raw, chan6_raw, chan7_raw, chan8_raw, rssi), force_mavlink1=force_mavlink1)

## servo_output_raw_encode
    def servo_output_raw_encode(self, time_usec: int, port: int, servo1_raw: int, servo2_raw: int, servo3_raw: int, servo4_raw: int, servo5_raw: int, servo6_raw: int, servo7_raw: int, servo8_raw: int, servo9_raw: int = 0, servo10_raw: int = 0, servo11_raw: int = 0, servo12_raw: int = 0, servo13_raw: int = 0, servo14_raw: int = 0, servo15_raw: int = 0, servo16_raw: int = 0) -> MAVLink_servo_output_raw_message:
        """
        Superseded by ACTUATOR_OUTPUT_STATUS. The RAW values of the servo
        outputs (for RC input from the remote, use the RC_CHANNELS
        messages). The standard PPM modulation is as follows: 1000
        microseconds: 0%, 2000 microseconds: 100%.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint32_t)
        port                      : Servo output port (set of 8 outputs = 1 port). Flight stacks running on Pixhawk should use: 0 = MAIN, 1 = AUX. (type:uint8_t)
        servo1_raw                : Servo output 1 value [us] (type:uint16_t)
        servo2_raw                : Servo output 2 value [us] (type:uint16_t)
        servo3_raw                : Servo output 3 value [us] (type:uint16_t)
        servo4_raw                : Servo output 4 value [us] (type:uint16_t)
        servo5_raw                : Servo output 5 value [us] (type:uint16_t)
        servo6_raw                : Servo output 6 value [us] (type:uint16_t)
        servo7_raw                : Servo output 7 value [us] (type:uint16_t)
        servo8_raw                : Servo output 8 value [us] (type:uint16_t)
        servo9_raw                : Servo output 9 value [us] (type:uint16_t)
        servo10_raw               : Servo output 10 value [us] (type:uint16_t)
        servo11_raw               : Servo output 11 value [us] (type:uint16_t)
        servo12_raw               : Servo output 12 value [us] (type:uint16_t)
        servo13_raw               : Servo output 13 value [us] (type:uint16_t)
        servo14_raw               : Servo output 14 value [us] (type:uint16_t)
        servo15_raw               : Servo output 15 value [us] (type:uint16_t)
        servo16_raw               : Servo output 16 value [us] (type:uint16_t)

        """
        return MAVLink_servo_output_raw_message(time_usec, port, servo1_raw, servo2_raw, servo3_raw, servo4_raw, servo5_raw, servo6_raw, servo7_raw, servo8_raw, servo9_raw, servo10_raw, servo11_raw, servo12_raw, servo13_raw, servo14_raw, servo15_raw, servo16_raw)

## servo_output_raw_send
    def servo_output_raw_send(self, time_usec: int, port: int, servo1_raw: int, servo2_raw: int, servo3_raw: int, servo4_raw: int, servo5_raw: int, servo6_raw: int, servo7_raw: int, servo8_raw: int, servo9_raw: int = 0, servo10_raw: int = 0, servo11_raw: int = 0, servo12_raw: int = 0, servo13_raw: int = 0, servo14_raw: int = 0, servo15_raw: int = 0, servo16_raw: int = 0, force_mavlink1: bool = False) -> None:
        """
        Superseded by ACTUATOR_OUTPUT_STATUS. The RAW values of the servo
        outputs (for RC input from the remote, use the RC_CHANNELS
        messages). The standard PPM modulation is as follows: 1000
        microseconds: 0%, 2000 microseconds: 100%.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint32_t)
        port                      : Servo output port (set of 8 outputs = 1 port). Flight stacks running on Pixhawk should use: 0 = MAIN, 1 = AUX. (type:uint8_t)
        servo1_raw                : Servo output 1 value [us] (type:uint16_t)
        servo2_raw                : Servo output 2 value [us] (type:uint16_t)
        servo3_raw                : Servo output 3 value [us] (type:uint16_t)
        servo4_raw                : Servo output 4 value [us] (type:uint16_t)
        servo5_raw                : Servo output 5 value [us] (type:uint16_t)
        servo6_raw                : Servo output 6 value [us] (type:uint16_t)
        servo7_raw                : Servo output 7 value [us] (type:uint16_t)
        servo8_raw                : Servo output 8 value [us] (type:uint16_t)
        servo9_raw                : Servo output 9 value [us] (type:uint16_t)
        servo10_raw               : Servo output 10 value [us] (type:uint16_t)
        servo11_raw               : Servo output 11 value [us] (type:uint16_t)
        servo12_raw               : Servo output 12 value [us] (type:uint16_t)
        servo13_raw               : Servo output 13 value [us] (type:uint16_t)
        servo14_raw               : Servo output 14 value [us] (type:uint16_t)
        servo15_raw               : Servo output 15 value [us] (type:uint16_t)
        servo16_raw               : Servo output 16 value [us] (type:uint16_t)

        """
        self.send(self.servo_output_raw_encode(time_usec, port, servo1_raw, servo2_raw, servo3_raw, servo4_raw, servo5_raw, servo6_raw, servo7_raw, servo8_raw, servo9_raw, servo10_raw, servo11_raw, servo12_raw, servo13_raw, servo14_raw, servo15_raw, servo16_raw), force_mavlink1=force_mavlink1)

## mission_request_partial_list_encode
    def mission_request_partial_list_encode(self, target_system: int, target_component: int, start_index: int, end_index: int, mission_type: int = 0) -> MAVLink_mission_request_partial_list_message:
        """
        Request a partial list of mission items from the system/component.
        https://mavlink.io/en/services/mission.html. If start and end
        index are the same, just send one waypoint.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        start_index               : Start index (type:int16_t)
        end_index                 : End index, -1 by default (-1: send list to end). Else a valid index of the list (type:int16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_request_partial_list_message(target_system, target_component, start_index, end_index, mission_type)

## mission_request_partial_list_send
    def mission_request_partial_list_send(self, target_system: int, target_component: int, start_index: int, end_index: int, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        Request a partial list of mission items from the system/component.
        https://mavlink.io/en/services/mission.html. If start and end
        index are the same, just send one waypoint.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        start_index               : Start index (type:int16_t)
        end_index                 : End index, -1 by default (-1: send list to end). Else a valid index of the list (type:int16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_request_partial_list_encode(target_system, target_component, start_index, end_index, mission_type), force_mavlink1=force_mavlink1)

## mission_write_partial_list_encode
    def mission_write_partial_list_encode(self, target_system: int, target_component: int, start_index: int, end_index: int, mission_type: int = 0) -> MAVLink_mission_write_partial_list_message:
        """
        This message is sent to the MAV to write a partial list. If start
        index == end index, only one item will be transmitted /
        updated. If the start index is NOT 0 and above the current
        list size, this request should be REJECTED!

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        start_index               : Start index. Must be smaller / equal to the largest index of the current onboard list. (type:int16_t)
        end_index                 : End index, equal or greater than start index. (type:int16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_write_partial_list_message(target_system, target_component, start_index, end_index, mission_type)

## mission_write_partial_list_send
    def mission_write_partial_list_send(self, target_system: int, target_component: int, start_index: int, end_index: int, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        This message is sent to the MAV to write a partial list. If start
        index == end index, only one item will be transmitted /
        updated. If the start index is NOT 0 and above the current
        list size, this request should be REJECTED!

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        start_index               : Start index. Must be smaller / equal to the largest index of the current onboard list. (type:int16_t)
        end_index                 : End index, equal or greater than start index. (type:int16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_write_partial_list_encode(target_system, target_component, start_index, end_index, mission_type), force_mavlink1=force_mavlink1)

## mission_item_encode
    def mission_item_encode(self, target_system: int, target_component: int, seq: int, frame: int, command: int, current: int, autocontinue: int, param1: float, param2: float, param3: float, param4: float, x: float, y: float, z: float, mission_type: int = 0) -> MAVLink_mission_item_message:
        """
        Message encoding a mission item. This message is emitted to announce
        the presence of a mission item and to set a mission item on
        the system. The mission item can be either in x, y, z meters
        (type: LOCAL) or x:lat, y:lon, z:altitude. Local frame is
        Z-down, right handed (NED), global frame is Z-up, right handed
        (ENU). NaN may be used to indicate an optional/default value
        (e.g. to use the system's current latitude or yaw rather than
        a specific value). See also
        https://mavlink.io/en/services/mission.html.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Sequence (type:uint16_t)
        frame                     : The coordinate system of the waypoint. (type:uint8_t, values:MAV_FRAME)
        command                   : The scheduled action for the waypoint. (type:uint16_t, values:MAV_CMD)
        current                   : false:0, true:1 (type:uint8_t)
        autocontinue              : Autocontinue to next waypoint (type:uint8_t)
        param1                    : PARAM1, see MAV_CMD enum (type:float)
        param2                    : PARAM2, see MAV_CMD enum (type:float)
        param3                    : PARAM3, see MAV_CMD enum (type:float)
        param4                    : PARAM4, see MAV_CMD enum (type:float)
        x                         : PARAM5 / local: X coordinate, global: latitude (type:float)
        y                         : PARAM6 / local: Y coordinate, global: longitude (type:float)
        z                         : PARAM7 / local: Z coordinate, global: altitude (relative or absolute, depending on frame). (type:float)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_item_message(target_system, target_component, seq, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z, mission_type)

## mission_item_send
    def mission_item_send(self, target_system: int, target_component: int, seq: int, frame: int, command: int, current: int, autocontinue: int, param1: float, param2: float, param3: float, param4: float, x: float, y: float, z: float, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        Message encoding a mission item. This message is emitted to announce
        the presence of a mission item and to set a mission item on
        the system. The mission item can be either in x, y, z meters
        (type: LOCAL) or x:lat, y:lon, z:altitude. Local frame is
        Z-down, right handed (NED), global frame is Z-up, right handed
        (ENU). NaN may be used to indicate an optional/default value
        (e.g. to use the system's current latitude or yaw rather than
        a specific value). See also
        https://mavlink.io/en/services/mission.html.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Sequence (type:uint16_t)
        frame                     : The coordinate system of the waypoint. (type:uint8_t, values:MAV_FRAME)
        command                   : The scheduled action for the waypoint. (type:uint16_t, values:MAV_CMD)
        current                   : false:0, true:1 (type:uint8_t)
        autocontinue              : Autocontinue to next waypoint (type:uint8_t)
        param1                    : PARAM1, see MAV_CMD enum (type:float)
        param2                    : PARAM2, see MAV_CMD enum (type:float)
        param3                    : PARAM3, see MAV_CMD enum (type:float)
        param4                    : PARAM4, see MAV_CMD enum (type:float)
        x                         : PARAM5 / local: X coordinate, global: latitude (type:float)
        y                         : PARAM6 / local: Y coordinate, global: longitude (type:float)
        z                         : PARAM7 / local: Z coordinate, global: altitude (relative or absolute, depending on frame). (type:float)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_item_encode(target_system, target_component, seq, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z, mission_type), force_mavlink1=force_mavlink1)

## mission_request_encode
    def mission_request_encode(self, target_system: int, target_component: int, seq: int, mission_type: int = 0) -> MAVLink_mission_request_message:
        """
        Request the information of the mission item with the sequence number
        seq. The response of the system to this message should be a
        MISSION_ITEM message.
        https://mavlink.io/en/services/mission.html

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Sequence (type:uint16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_request_message(target_system, target_component, seq, mission_type)

## mission_request_send
    def mission_request_send(self, target_system: int, target_component: int, seq: int, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        Request the information of the mission item with the sequence number
        seq. The response of the system to this message should be a
        MISSION_ITEM message.
        https://mavlink.io/en/services/mission.html

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Sequence (type:uint16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_request_encode(target_system, target_component, seq, mission_type), force_mavlink1=force_mavlink1)

## mission_set_current_encode
    def mission_set_current_encode(self, target_system: int, target_component: int, seq: int) -> MAVLink_mission_set_current_message:
        """
        Set the mission item with sequence number seq as current item. This
        means that the MAV will continue to this mission item on the
        shortest path (not following the mission items in-between).

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Sequence (type:uint16_t)

        """
        return MAVLink_mission_set_current_message(target_system, target_component, seq)

## mission_set_current_send
    def mission_set_current_send(self, target_system: int, target_component: int, seq: int, force_mavlink1: bool = False) -> None:
        """
        Set the mission item with sequence number seq as current item. This
        means that the MAV will continue to this mission item on the
        shortest path (not following the mission items in-between).

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Sequence (type:uint16_t)

        """
        self.send(self.mission_set_current_encode(target_system, target_component, seq), force_mavlink1=force_mavlink1)

## mission_current_encode
    def mission_current_encode(self, seq: int, total: int = 0, mission_state: int = 0, mission_mode: int = 0) -> MAVLink_mission_current_message:
        """
        Message that announces the sequence number of the current active
        mission item. The MAV will fly towards this mission item.

        seq                       : Sequence (type:uint16_t)
        total                     : Total number of mission items on vehicle (on last item, sequence == total). If the autopilot stores its home location as part of the mission this will be excluded from the total. 0: Not supported, UINT16_MAX if no mission is present on the vehicle. (type:uint16_t)
        mission_state             : Mission state machine state. MISSION_STATE_UNKNOWN if state reporting not supported. (type:uint8_t, values:MISSION_STATE)
        mission_mode              : Vehicle is in a mode that can execute mission items or suspended. 0: Unknown, 1: In mission mode, 2: Suspended (not in mission mode). (type:uint8_t)

        """
        return MAVLink_mission_current_message(seq, total, mission_state, mission_mode)

## mission_current_send
    def mission_current_send(self, seq: int, total: int = 0, mission_state: int = 0, mission_mode: int = 0, force_mavlink1: bool = False) -> None:
        """
        Message that announces the sequence number of the current active
        mission item. The MAV will fly towards this mission item.

        seq                       : Sequence (type:uint16_t)
        total                     : Total number of mission items on vehicle (on last item, sequence == total). If the autopilot stores its home location as part of the mission this will be excluded from the total. 0: Not supported, UINT16_MAX if no mission is present on the vehicle. (type:uint16_t)
        mission_state             : Mission state machine state. MISSION_STATE_UNKNOWN if state reporting not supported. (type:uint8_t, values:MISSION_STATE)
        mission_mode              : Vehicle is in a mode that can execute mission items or suspended. 0: Unknown, 1: In mission mode, 2: Suspended (not in mission mode). (type:uint8_t)

        """
        self.send(self.mission_current_encode(seq, total, mission_state, mission_mode), force_mavlink1=force_mavlink1)

## mission_request_list_encode
    def mission_request_list_encode(self, target_system: int, target_component: int, mission_type: int = 0) -> MAVLink_mission_request_list_message:
        """
        Request the overall list of mission items from the system/component.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_request_list_message(target_system, target_component, mission_type)

## mission_request_list_send
    def mission_request_list_send(self, target_system: int, target_component: int, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        Request the overall list of mission items from the system/component.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_request_list_encode(target_system, target_component, mission_type), force_mavlink1=force_mavlink1)

## mission_count_encode
    def mission_count_encode(self, target_system: int, target_component: int, count: int, mission_type: int = 0) -> MAVLink_mission_count_message:
        """
        This message is emitted as response to MISSION_REQUEST_LIST by the MAV
        and to initiate a write transaction. The GCS can then request
        the individual mission item based on the knowledge of the
        total number of waypoints.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        count                     : Number of mission items in the sequence (type:uint16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_count_message(target_system, target_component, count, mission_type)

## mission_count_send
    def mission_count_send(self, target_system: int, target_component: int, count: int, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        This message is emitted as response to MISSION_REQUEST_LIST by the MAV
        and to initiate a write transaction. The GCS can then request
        the individual mission item based on the knowledge of the
        total number of waypoints.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        count                     : Number of mission items in the sequence (type:uint16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_count_encode(target_system, target_component, count, mission_type), force_mavlink1=force_mavlink1)

## mission_clear_all_encode
    def mission_clear_all_encode(self, target_system: int, target_component: int, mission_type: int = 0) -> MAVLink_mission_clear_all_message:
        """
        Delete all mission items at once.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_clear_all_message(target_system, target_component, mission_type)

## mission_clear_all_send
    def mission_clear_all_send(self, target_system: int, target_component: int, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        Delete all mission items at once.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_clear_all_encode(target_system, target_component, mission_type), force_mavlink1=force_mavlink1)

## mission_item_reached_encode
    def mission_item_reached_encode(self, seq: int) -> MAVLink_mission_item_reached_message:
        """
        A certain mission item has been reached. The system will either hold
        this position (or circle on the orbit) or (if the autocontinue
        on the WP was set) continue to the next waypoint.

        seq                       : Sequence (type:uint16_t)

        """
        return MAVLink_mission_item_reached_message(seq)

## mission_item_reached_send
    def mission_item_reached_send(self, seq: int, force_mavlink1: bool = False) -> None:
        """
        A certain mission item has been reached. The system will either hold
        this position (or circle on the orbit) or (if the autocontinue
        on the WP was set) continue to the next waypoint.

        seq                       : Sequence (type:uint16_t)

        """
        self.send(self.mission_item_reached_encode(seq), force_mavlink1=force_mavlink1)

## mission_ack_encode
    def mission_ack_encode(self, target_system: int, target_component: int, type: int, mission_type: int = 0) -> MAVLink_mission_ack_message:
        """
        Acknowledgment message during waypoint handling. The type field states
        if this message is a positive ack (type=0) or if an error
        happened (type=non-zero).

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        type                      : Mission result. (type:uint8_t, values:MAV_MISSION_RESULT)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_ack_message(target_system, target_component, type, mission_type)

## mission_ack_send
    def mission_ack_send(self, target_system: int, target_component: int, type: int, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        Acknowledgment message during waypoint handling. The type field states
        if this message is a positive ack (type=0) or if an error
        happened (type=non-zero).

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        type                      : Mission result. (type:uint8_t, values:MAV_MISSION_RESULT)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_ack_encode(target_system, target_component, type, mission_type), force_mavlink1=force_mavlink1)

## set_gps_global_origin_encode
    def set_gps_global_origin_encode(self, target_system: int, latitude: int, longitude: int, altitude: int, time_usec: int = 0) -> MAVLink_set_gps_global_origin_message:
        """
        Sets the GPS coordinates of the vehicle local origin (0,0,0) position.
        Vehicle should emit GPS_GLOBAL_ORIGIN irrespective of whether
        the origin is changed. This enables transform between the
        local coordinate frame and the global (GPS) coordinate frame,
        which may be necessary when (for example) indoor and outdoor
        settings are connected and the MAV should move from in- to
        outdoor.

        target_system             : System ID (type:uint8_t)
        latitude                  : Latitude (WGS84) [degE7] (type:int32_t)
        longitude                 : Longitude (WGS84) [degE7] (type:int32_t)
        altitude                  : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)

        """
        return MAVLink_set_gps_global_origin_message(target_system, latitude, longitude, altitude, time_usec)

## set_gps_global_origin_send
    def set_gps_global_origin_send(self, target_system: int, latitude: int, longitude: int, altitude: int, time_usec: int = 0, force_mavlink1: bool = False) -> None:
        """
        Sets the GPS coordinates of the vehicle local origin (0,0,0) position.
        Vehicle should emit GPS_GLOBAL_ORIGIN irrespective of whether
        the origin is changed. This enables transform between the
        local coordinate frame and the global (GPS) coordinate frame,
        which may be necessary when (for example) indoor and outdoor
        settings are connected and the MAV should move from in- to
        outdoor.

        target_system             : System ID (type:uint8_t)
        latitude                  : Latitude (WGS84) [degE7] (type:int32_t)
        longitude                 : Longitude (WGS84) [degE7] (type:int32_t)
        altitude                  : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)

        """
        self.send(self.set_gps_global_origin_encode(target_system, latitude, longitude, altitude, time_usec), force_mavlink1=force_mavlink1)

## gps_global_origin_encode
    def gps_global_origin_encode(self, latitude: int, longitude: int, altitude: int, time_usec: int = 0) -> MAVLink_gps_global_origin_message:
        """
        Publishes the GPS coordinates of the vehicle local origin (0,0,0)
        position. Emitted whenever a new GPS-Local position mapping is
        requested or set - e.g. following SET_GPS_GLOBAL_ORIGIN
        message.

        latitude                  : Latitude (WGS84) [degE7] (type:int32_t)
        longitude                 : Longitude (WGS84) [degE7] (type:int32_t)
        altitude                  : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)

        """
        return MAVLink_gps_global_origin_message(latitude, longitude, altitude, time_usec)

## gps_global_origin_send
    def gps_global_origin_send(self, latitude: int, longitude: int, altitude: int, time_usec: int = 0, force_mavlink1: bool = False) -> None:
        """
        Publishes the GPS coordinates of the vehicle local origin (0,0,0)
        position. Emitted whenever a new GPS-Local position mapping is
        requested or set - e.g. following SET_GPS_GLOBAL_ORIGIN
        message.

        latitude                  : Latitude (WGS84) [degE7] (type:int32_t)
        longitude                 : Longitude (WGS84) [degE7] (type:int32_t)
        altitude                  : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)

        """
        self.send(self.gps_global_origin_encode(latitude, longitude, altitude, time_usec), force_mavlink1=force_mavlink1)

## param_map_rc_encode
    def param_map_rc_encode(self, target_system: int, target_component: int, param_id: bytes, param_index: int, parameter_rc_channel_index: int, param_value0: float, scale: float, param_value_min: float, param_value_max: float) -> MAVLink_param_map_rc_message:
        """
        Bind a RC channel to a parameter. The parameter should change
        according to the RC channel value.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_index               : Parameter index. Send -1 to use the param ID field as identifier (else the param id will be ignored), send -2 to disable any existing map for this rc_channel_index. (type:int16_t)
        parameter_rc_channel_index        : Index of parameter RC channel. Not equal to the RC channel id. Typically corresponds to a potentiometer-knob on the RC. (type:uint8_t)
        param_value0              : Initial parameter value (type:float)
        scale                     : Scale, maps the RC range [-1, 1] to a parameter value (type:float)
        param_value_min           : Minimum param value. The protocol does not define if this overwrites an onboard minimum value. (Depends on implementation) (type:float)
        param_value_max           : Maximum param value. The protocol does not define if this overwrites an onboard maximum value. (Depends on implementation) (type:float)

        """
        return MAVLink_param_map_rc_message(target_system, target_component, param_id, param_index, parameter_rc_channel_index, param_value0, scale, param_value_min, param_value_max)

## param_map_rc_send
    def param_map_rc_send(self, target_system: int, target_component: int, param_id: bytes, param_index: int, parameter_rc_channel_index: int, param_value0: float, scale: float, param_value_min: float, param_value_max: float, force_mavlink1: bool = False) -> None:
        """
        Bind a RC channel to a parameter. The parameter should change
        according to the RC channel value.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_index               : Parameter index. Send -1 to use the param ID field as identifier (else the param id will be ignored), send -2 to disable any existing map for this rc_channel_index. (type:int16_t)
        parameter_rc_channel_index        : Index of parameter RC channel. Not equal to the RC channel id. Typically corresponds to a potentiometer-knob on the RC. (type:uint8_t)
        param_value0              : Initial parameter value (type:float)
        scale                     : Scale, maps the RC range [-1, 1] to a parameter value (type:float)
        param_value_min           : Minimum param value. The protocol does not define if this overwrites an onboard minimum value. (Depends on implementation) (type:float)
        param_value_max           : Maximum param value. The protocol does not define if this overwrites an onboard maximum value. (Depends on implementation) (type:float)

        """
        self.send(self.param_map_rc_encode(target_system, target_component, param_id, param_index, parameter_rc_channel_index, param_value0, scale, param_value_min, param_value_max), force_mavlink1=force_mavlink1)

## mission_request_int_encode
    def mission_request_int_encode(self, target_system: int, target_component: int, seq: int, mission_type: int = 0) -> MAVLink_mission_request_int_message:
        """
        Request the information of the mission item with the sequence number
        seq. The response of the system to this message should be a
        MISSION_ITEM_INT message.
        https://mavlink.io/en/services/mission.html

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Sequence (type:uint16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_request_int_message(target_system, target_component, seq, mission_type)

## mission_request_int_send
    def mission_request_int_send(self, target_system: int, target_component: int, seq: int, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        Request the information of the mission item with the sequence number
        seq. The response of the system to this message should be a
        MISSION_ITEM_INT message.
        https://mavlink.io/en/services/mission.html

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Sequence (type:uint16_t)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_request_int_encode(target_system, target_component, seq, mission_type), force_mavlink1=force_mavlink1)

## safety_set_allowed_area_encode
    def safety_set_allowed_area_encode(self, target_system: int, target_component: int, frame: int, p1x: float, p1y: float, p1z: float, p2x: float, p2y: float, p2z: float) -> MAVLink_safety_set_allowed_area_message:
        """
        Set a safety zone (volume), which is defined by two corners of a cube.
        This message can be used to tell the MAV which
        setpoints/waypoints to accept and which to reject. Safety
        areas are often enforced by national or competition
        regulations.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        frame                     : Coordinate frame. Can be either global, GPS, right-handed with Z axis up or local, right handed, Z axis down. (type:uint8_t, values:MAV_FRAME)
        p1x                       : x position 1 / Latitude 1 [m] (type:float)
        p1y                       : y position 1 / Longitude 1 [m] (type:float)
        p1z                       : z position 1 / Altitude 1 [m] (type:float)
        p2x                       : x position 2 / Latitude 2 [m] (type:float)
        p2y                       : y position 2 / Longitude 2 [m] (type:float)
        p2z                       : z position 2 / Altitude 2 [m] (type:float)

        """
        return MAVLink_safety_set_allowed_area_message(target_system, target_component, frame, p1x, p1y, p1z, p2x, p2y, p2z)

## safety_set_allowed_area_send
    def safety_set_allowed_area_send(self, target_system: int, target_component: int, frame: int, p1x: float, p1y: float, p1z: float, p2x: float, p2y: float, p2z: float, force_mavlink1: bool = False) -> None:
        """
        Set a safety zone (volume), which is defined by two corners of a cube.
        This message can be used to tell the MAV which
        setpoints/waypoints to accept and which to reject. Safety
        areas are often enforced by national or competition
        regulations.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        frame                     : Coordinate frame. Can be either global, GPS, right-handed with Z axis up or local, right handed, Z axis down. (type:uint8_t, values:MAV_FRAME)
        p1x                       : x position 1 / Latitude 1 [m] (type:float)
        p1y                       : y position 1 / Longitude 1 [m] (type:float)
        p1z                       : z position 1 / Altitude 1 [m] (type:float)
        p2x                       : x position 2 / Latitude 2 [m] (type:float)
        p2y                       : y position 2 / Longitude 2 [m] (type:float)
        p2z                       : z position 2 / Altitude 2 [m] (type:float)

        """
        self.send(self.safety_set_allowed_area_encode(target_system, target_component, frame, p1x, p1y, p1z, p2x, p2y, p2z), force_mavlink1=force_mavlink1)

## safety_allowed_area_encode
    def safety_allowed_area_encode(self, frame: int, p1x: float, p1y: float, p1z: float, p2x: float, p2y: float, p2z: float) -> MAVLink_safety_allowed_area_message:
        """
        Read out the safety zone the MAV currently assumes.

        frame                     : Coordinate frame. Can be either global, GPS, right-handed with Z axis up or local, right handed, Z axis down. (type:uint8_t, values:MAV_FRAME)
        p1x                       : x position 1 / Latitude 1 [m] (type:float)
        p1y                       : y position 1 / Longitude 1 [m] (type:float)
        p1z                       : z position 1 / Altitude 1 [m] (type:float)
        p2x                       : x position 2 / Latitude 2 [m] (type:float)
        p2y                       : y position 2 / Longitude 2 [m] (type:float)
        p2z                       : z position 2 / Altitude 2 [m] (type:float)

        """
        return MAVLink_safety_allowed_area_message(frame, p1x, p1y, p1z, p2x, p2y, p2z)

## safety_allowed_area_send
    def safety_allowed_area_send(self, frame: int, p1x: float, p1y: float, p1z: float, p2x: float, p2y: float, p2z: float, force_mavlink1: bool = False) -> None:
        """
        Read out the safety zone the MAV currently assumes.

        frame                     : Coordinate frame. Can be either global, GPS, right-handed with Z axis up or local, right handed, Z axis down. (type:uint8_t, values:MAV_FRAME)
        p1x                       : x position 1 / Latitude 1 [m] (type:float)
        p1y                       : y position 1 / Longitude 1 [m] (type:float)
        p1z                       : z position 1 / Altitude 1 [m] (type:float)
        p2x                       : x position 2 / Latitude 2 [m] (type:float)
        p2y                       : y position 2 / Longitude 2 [m] (type:float)
        p2z                       : z position 2 / Altitude 2 [m] (type:float)

        """
        self.send(self.safety_allowed_area_encode(frame, p1x, p1y, p1z, p2x, p2y, p2z), force_mavlink1=force_mavlink1)

## attitude_quaternion_cov_encode
    def attitude_quaternion_cov_encode(self, time_usec: int, q: Sequence[float], rollspeed: float, pitchspeed: float, yawspeed: float, covariance: Sequence[float]) -> MAVLink_attitude_quaternion_cov_message:
        """
        The attitude in the aeronautical frame (right-handed, Z-down, X-front,
        Y-right), expressed as quaternion. Quaternion order is w, x,
        y, z and a zero rotation would be expressed as (1 0 0 0).

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation) (type:float)
        rollspeed                 : Roll angular speed [rad/s] (type:float)
        pitchspeed                : Pitch angular speed [rad/s] (type:float)
        yawspeed                  : Yaw angular speed [rad/s] (type:float)
        covariance                : Row-major representation of a 3x3 attitude covariance matrix (states: roll, pitch, yaw; first three entries are the first ROW, next three entries are the second row, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        return MAVLink_attitude_quaternion_cov_message(time_usec, q, rollspeed, pitchspeed, yawspeed, covariance)

## attitude_quaternion_cov_send
    def attitude_quaternion_cov_send(self, time_usec: int, q: Sequence[float], rollspeed: float, pitchspeed: float, yawspeed: float, covariance: Sequence[float], force_mavlink1: bool = False) -> None:
        """
        The attitude in the aeronautical frame (right-handed, Z-down, X-front,
        Y-right), expressed as quaternion. Quaternion order is w, x,
        y, z and a zero rotation would be expressed as (1 0 0 0).

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation) (type:float)
        rollspeed                 : Roll angular speed [rad/s] (type:float)
        pitchspeed                : Pitch angular speed [rad/s] (type:float)
        yawspeed                  : Yaw angular speed [rad/s] (type:float)
        covariance                : Row-major representation of a 3x3 attitude covariance matrix (states: roll, pitch, yaw; first three entries are the first ROW, next three entries are the second row, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        self.send(self.attitude_quaternion_cov_encode(time_usec, q, rollspeed, pitchspeed, yawspeed, covariance), force_mavlink1=force_mavlink1)

## nav_controller_output_encode
    def nav_controller_output_encode(self, nav_roll: float, nav_pitch: float, nav_bearing: int, target_bearing: int, wp_dist: int, alt_error: float, aspd_error: float, xtrack_error: float) -> MAVLink_nav_controller_output_message:
        """
        The state of the navigation and position controller.

        nav_roll                  : Current desired roll [deg] (type:float)
        nav_pitch                 : Current desired pitch [deg] (type:float)
        nav_bearing               : Current desired heading [deg] (type:int16_t)
        target_bearing            : Bearing to current waypoint/target [deg] (type:int16_t)
        wp_dist                   : Distance to active waypoint [m] (type:uint16_t)
        alt_error                 : Current altitude error [m] (type:float)
        aspd_error                : Current airspeed error [m/s] (type:float)
        xtrack_error              : Current crosstrack error on x-y plane [m] (type:float)

        """
        return MAVLink_nav_controller_output_message(nav_roll, nav_pitch, nav_bearing, target_bearing, wp_dist, alt_error, aspd_error, xtrack_error)

## nav_controller_output_send
    def nav_controller_output_send(self, nav_roll: float, nav_pitch: float, nav_bearing: int, target_bearing: int, wp_dist: int, alt_error: float, aspd_error: float, xtrack_error: float, force_mavlink1: bool = False) -> None:
        """
        The state of the navigation and position controller.

        nav_roll                  : Current desired roll [deg] (type:float)
        nav_pitch                 : Current desired pitch [deg] (type:float)
        nav_bearing               : Current desired heading [deg] (type:int16_t)
        target_bearing            : Bearing to current waypoint/target [deg] (type:int16_t)
        wp_dist                   : Distance to active waypoint [m] (type:uint16_t)
        alt_error                 : Current altitude error [m] (type:float)
        aspd_error                : Current airspeed error [m/s] (type:float)
        xtrack_error              : Current crosstrack error on x-y plane [m] (type:float)

        """
        self.send(self.nav_controller_output_encode(nav_roll, nav_pitch, nav_bearing, target_bearing, wp_dist, alt_error, aspd_error, xtrack_error), force_mavlink1=force_mavlink1)

## global_position_int_cov_encode
    def global_position_int_cov_encode(self, time_usec: int, estimator_type: int, lat: int, lon: int, alt: int, relative_alt: int, vx: float, vy: float, vz: float, covariance: Sequence[float]) -> MAVLink_global_position_int_cov_message:
        """
        The filtered global position (e.g. fused GPS and accelerometers). The
        position is in GPS-frame (right-handed, Z-up). It  is designed
        as scaled integer message since the resolution of float is not
        sufficient. NOTE: This message is intended for onboard
        networks / companion computers and higher-bandwidth links and
        optimized for accuracy and completeness. Please use the
        GLOBAL_POSITION_INT message for a minimal subset.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        estimator_type            : Class id of the estimator this estimate originated from. (type:uint8_t, values:MAV_ESTIMATOR_TYPE)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        alt                       : Altitude in meters above MSL [mm] (type:int32_t)
        relative_alt              : Altitude above ground [mm] (type:int32_t)
        vx                        : Ground X Speed (Latitude) [m/s] (type:float)
        vy                        : Ground Y Speed (Longitude) [m/s] (type:float)
        vz                        : Ground Z Speed (Altitude) [m/s] (type:float)
        covariance                : Row-major representation of a 6x6 position and velocity 6x6 cross-covariance matrix (states: lat, lon, alt, vx, vy, vz; first six entries are the first ROW, next six entries are the second row, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        return MAVLink_global_position_int_cov_message(time_usec, estimator_type, lat, lon, alt, relative_alt, vx, vy, vz, covariance)

## global_position_int_cov_send
    def global_position_int_cov_send(self, time_usec: int, estimator_type: int, lat: int, lon: int, alt: int, relative_alt: int, vx: float, vy: float, vz: float, covariance: Sequence[float], force_mavlink1: bool = False) -> None:
        """
        The filtered global position (e.g. fused GPS and accelerometers). The
        position is in GPS-frame (right-handed, Z-up). It  is designed
        as scaled integer message since the resolution of float is not
        sufficient. NOTE: This message is intended for onboard
        networks / companion computers and higher-bandwidth links and
        optimized for accuracy and completeness. Please use the
        GLOBAL_POSITION_INT message for a minimal subset.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        estimator_type            : Class id of the estimator this estimate originated from. (type:uint8_t, values:MAV_ESTIMATOR_TYPE)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        alt                       : Altitude in meters above MSL [mm] (type:int32_t)
        relative_alt              : Altitude above ground [mm] (type:int32_t)
        vx                        : Ground X Speed (Latitude) [m/s] (type:float)
        vy                        : Ground Y Speed (Longitude) [m/s] (type:float)
        vz                        : Ground Z Speed (Altitude) [m/s] (type:float)
        covariance                : Row-major representation of a 6x6 position and velocity 6x6 cross-covariance matrix (states: lat, lon, alt, vx, vy, vz; first six entries are the first ROW, next six entries are the second row, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        self.send(self.global_position_int_cov_encode(time_usec, estimator_type, lat, lon, alt, relative_alt, vx, vy, vz, covariance), force_mavlink1=force_mavlink1)

## local_position_ned_cov_encode
    def local_position_ned_cov_encode(self, time_usec: int, estimator_type: int, x: float, y: float, z: float, vx: float, vy: float, vz: float, ax: float, ay: float, az: float, covariance: Sequence[float]) -> MAVLink_local_position_ned_cov_message:
        """
        The filtered local position (e.g. fused computer vision and
        accelerometers). Coordinate frame is right-handed, Z-axis down
        (aeronautical frame, NED / north-east-down convention)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        estimator_type            : Class id of the estimator this estimate originated from. (type:uint8_t, values:MAV_ESTIMATOR_TYPE)
        x                         : X Position [m] (type:float)
        y                         : Y Position [m] (type:float)
        z                         : Z Position [m] (type:float)
        vx                        : X Speed [m/s] (type:float)
        vy                        : Y Speed [m/s] (type:float)
        vz                        : Z Speed [m/s] (type:float)
        ax                        : X Acceleration [m/s/s] (type:float)
        ay                        : Y Acceleration [m/s/s] (type:float)
        az                        : Z Acceleration [m/s/s] (type:float)
        covariance                : Row-major representation of position, velocity and acceleration 9x9 cross-covariance matrix upper right triangle (states: x, y, z, vx, vy, vz, ax, ay, az; first nine entries are the first ROW, next eight entries are the second row, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        return MAVLink_local_position_ned_cov_message(time_usec, estimator_type, x, y, z, vx, vy, vz, ax, ay, az, covariance)

## local_position_ned_cov_send
    def local_position_ned_cov_send(self, time_usec: int, estimator_type: int, x: float, y: float, z: float, vx: float, vy: float, vz: float, ax: float, ay: float, az: float, covariance: Sequence[float], force_mavlink1: bool = False) -> None:
        """
        The filtered local position (e.g. fused computer vision and
        accelerometers). Coordinate frame is right-handed, Z-axis down
        (aeronautical frame, NED / north-east-down convention)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        estimator_type            : Class id of the estimator this estimate originated from. (type:uint8_t, values:MAV_ESTIMATOR_TYPE)
        x                         : X Position [m] (type:float)
        y                         : Y Position [m] (type:float)
        z                         : Z Position [m] (type:float)
        vx                        : X Speed [m/s] (type:float)
        vy                        : Y Speed [m/s] (type:float)
        vz                        : Z Speed [m/s] (type:float)
        ax                        : X Acceleration [m/s/s] (type:float)
        ay                        : Y Acceleration [m/s/s] (type:float)
        az                        : Z Acceleration [m/s/s] (type:float)
        covariance                : Row-major representation of position, velocity and acceleration 9x9 cross-covariance matrix upper right triangle (states: x, y, z, vx, vy, vz, ax, ay, az; first nine entries are the first ROW, next eight entries are the second row, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        self.send(self.local_position_ned_cov_encode(time_usec, estimator_type, x, y, z, vx, vy, vz, ax, ay, az, covariance), force_mavlink1=force_mavlink1)

## rc_channels_encode
    def rc_channels_encode(self, time_boot_ms: int, chancount: int, chan1_raw: int, chan2_raw: int, chan3_raw: int, chan4_raw: int, chan5_raw: int, chan6_raw: int, chan7_raw: int, chan8_raw: int, chan9_raw: int, chan10_raw: int, chan11_raw: int, chan12_raw: int, chan13_raw: int, chan14_raw: int, chan15_raw: int, chan16_raw: int, chan17_raw: int, chan18_raw: int, rssi: int) -> MAVLink_rc_channels_message:
        """
        The PPM values of the RC channels received. The standard PPM
        modulation is as follows: 1000 microseconds: 0%, 2000
        microseconds: 100%.  A value of UINT16_MAX implies the channel
        is unused. Individual receivers/transmitters might violate
        this specification.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        chancount                 : Total number of RC channels being received. This can be larger than 18, indicating that more channels are available but not given in this message. This value should be 0 when no RC channels are available. (type:uint8_t)
        chan1_raw                 : RC channel 1 value. [us] (type:uint16_t)
        chan2_raw                 : RC channel 2 value. [us] (type:uint16_t)
        chan3_raw                 : RC channel 3 value. [us] (type:uint16_t)
        chan4_raw                 : RC channel 4 value. [us] (type:uint16_t)
        chan5_raw                 : RC channel 5 value. [us] (type:uint16_t)
        chan6_raw                 : RC channel 6 value. [us] (type:uint16_t)
        chan7_raw                 : RC channel 7 value. [us] (type:uint16_t)
        chan8_raw                 : RC channel 8 value. [us] (type:uint16_t)
        chan9_raw                 : RC channel 9 value. [us] (type:uint16_t)
        chan10_raw                : RC channel 10 value. [us] (type:uint16_t)
        chan11_raw                : RC channel 11 value. [us] (type:uint16_t)
        chan12_raw                : RC channel 12 value. [us] (type:uint16_t)
        chan13_raw                : RC channel 13 value. [us] (type:uint16_t)
        chan14_raw                : RC channel 14 value. [us] (type:uint16_t)
        chan15_raw                : RC channel 15 value. [us] (type:uint16_t)
        chan16_raw                : RC channel 16 value. [us] (type:uint16_t)
        chan17_raw                : RC channel 17 value. [us] (type:uint16_t)
        chan18_raw                : RC channel 18 value. [us] (type:uint16_t)
        rssi                      : Receive signal strength indicator in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)

        """
        return MAVLink_rc_channels_message(time_boot_ms, chancount, chan1_raw, chan2_raw, chan3_raw, chan4_raw, chan5_raw, chan6_raw, chan7_raw, chan8_raw, chan9_raw, chan10_raw, chan11_raw, chan12_raw, chan13_raw, chan14_raw, chan15_raw, chan16_raw, chan17_raw, chan18_raw, rssi)

## rc_channels_send
    def rc_channels_send(self, time_boot_ms: int, chancount: int, chan1_raw: int, chan2_raw: int, chan3_raw: int, chan4_raw: int, chan5_raw: int, chan6_raw: int, chan7_raw: int, chan8_raw: int, chan9_raw: int, chan10_raw: int, chan11_raw: int, chan12_raw: int, chan13_raw: int, chan14_raw: int, chan15_raw: int, chan16_raw: int, chan17_raw: int, chan18_raw: int, rssi: int, force_mavlink1: bool = False) -> None:
        """
        The PPM values of the RC channels received. The standard PPM
        modulation is as follows: 1000 microseconds: 0%, 2000
        microseconds: 100%.  A value of UINT16_MAX implies the channel
        is unused. Individual receivers/transmitters might violate
        this specification.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        chancount                 : Total number of RC channels being received. This can be larger than 18, indicating that more channels are available but not given in this message. This value should be 0 when no RC channels are available. (type:uint8_t)
        chan1_raw                 : RC channel 1 value. [us] (type:uint16_t)
        chan2_raw                 : RC channel 2 value. [us] (type:uint16_t)
        chan3_raw                 : RC channel 3 value. [us] (type:uint16_t)
        chan4_raw                 : RC channel 4 value. [us] (type:uint16_t)
        chan5_raw                 : RC channel 5 value. [us] (type:uint16_t)
        chan6_raw                 : RC channel 6 value. [us] (type:uint16_t)
        chan7_raw                 : RC channel 7 value. [us] (type:uint16_t)
        chan8_raw                 : RC channel 8 value. [us] (type:uint16_t)
        chan9_raw                 : RC channel 9 value. [us] (type:uint16_t)
        chan10_raw                : RC channel 10 value. [us] (type:uint16_t)
        chan11_raw                : RC channel 11 value. [us] (type:uint16_t)
        chan12_raw                : RC channel 12 value. [us] (type:uint16_t)
        chan13_raw                : RC channel 13 value. [us] (type:uint16_t)
        chan14_raw                : RC channel 14 value. [us] (type:uint16_t)
        chan15_raw                : RC channel 15 value. [us] (type:uint16_t)
        chan16_raw                : RC channel 16 value. [us] (type:uint16_t)
        chan17_raw                : RC channel 17 value. [us] (type:uint16_t)
        chan18_raw                : RC channel 18 value. [us] (type:uint16_t)
        rssi                      : Receive signal strength indicator in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)

        """
        self.send(self.rc_channels_encode(time_boot_ms, chancount, chan1_raw, chan2_raw, chan3_raw, chan4_raw, chan5_raw, chan6_raw, chan7_raw, chan8_raw, chan9_raw, chan10_raw, chan11_raw, chan12_raw, chan13_raw, chan14_raw, chan15_raw, chan16_raw, chan17_raw, chan18_raw, rssi), force_mavlink1=force_mavlink1)

## request_data_stream_encode
    def request_data_stream_encode(self, target_system: int, target_component: int, req_stream_id: int, req_message_rate: int, start_stop: int) -> MAVLink_request_data_stream_message:
        """
        Request a data stream.

        target_system             : The target requested to send the message stream. (type:uint8_t)
        target_component          : The target requested to send the message stream. (type:uint8_t)
        req_stream_id             : The ID of the requested data stream (type:uint8_t)
        req_message_rate          : The requested message rate [Hz] (type:uint16_t)
        start_stop                : 1 to start sending, 0 to stop sending. (type:uint8_t)

        """
        return MAVLink_request_data_stream_message(target_system, target_component, req_stream_id, req_message_rate, start_stop)

## request_data_stream_send
    def request_data_stream_send(self, target_system: int, target_component: int, req_stream_id: int, req_message_rate: int, start_stop: int, force_mavlink1: bool = False) -> None:
        """
        Request a data stream.

        target_system             : The target requested to send the message stream. (type:uint8_t)
        target_component          : The target requested to send the message stream. (type:uint8_t)
        req_stream_id             : The ID of the requested data stream (type:uint8_t)
        req_message_rate          : The requested message rate [Hz] (type:uint16_t)
        start_stop                : 1 to start sending, 0 to stop sending. (type:uint8_t)

        """
        self.send(self.request_data_stream_encode(target_system, target_component, req_stream_id, req_message_rate, start_stop), force_mavlink1=force_mavlink1)

## data_stream_encode
    def data_stream_encode(self, stream_id: int, message_rate: int, on_off: int) -> MAVLink_data_stream_message:
        """
        Data stream status information.

        stream_id                 : The ID of the requested data stream (type:uint8_t)
        message_rate              : The message rate [Hz] (type:uint16_t)
        on_off                    : 1 stream is enabled, 0 stream is stopped. (type:uint8_t)

        """
        return MAVLink_data_stream_message(stream_id, message_rate, on_off)

## data_stream_send
    def data_stream_send(self, stream_id: int, message_rate: int, on_off: int, force_mavlink1: bool = False) -> None:
        """
        Data stream status information.

        stream_id                 : The ID of the requested data stream (type:uint8_t)
        message_rate              : The message rate [Hz] (type:uint16_t)
        on_off                    : 1 stream is enabled, 0 stream is stopped. (type:uint8_t)

        """
        self.send(self.data_stream_encode(stream_id, message_rate, on_off), force_mavlink1=force_mavlink1)

## manual_control_encode
    def manual_control_encode(self, target: int, x: int, y: int, z: int, r: int, buttons: int, buttons2: int = 0, enabled_extensions: int = 0, s: int = 0, t: int = 0, aux1: int = 0, aux2: int = 0, aux3: int = 0, aux4: int = 0, aux5: int = 0, aux6: int = 0) -> MAVLink_manual_control_message:
        """
        This message provides an API for manually controlling the vehicle
        using standard joystick axes nomenclature, along with a
        joystick-like input device. Unused axes can be disabled and
        buttons states are transmitted as individual on/off bits of a
        bitmask

        target                    : The system to be controlled. (type:uint8_t)
        x                         : X-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to forward(1000)-backward(-1000) movement on a joystick and the pitch of a vehicle. (type:int16_t)
        y                         : Y-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to left(-1000)-right(1000) movement on a joystick and the roll of a vehicle. (type:int16_t)
        z                         : Z-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to a separate slider movement with maximum being 1000 and minimum being -1000 on a joystick and the thrust of a vehicle. Positive values are positive thrust, negative values are negative thrust. (type:int16_t)
        r                         : R-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to a twisting of the joystick, with counter-clockwise being 1000 and clockwise being -1000, and the yaw of a vehicle. (type:int16_t)
        buttons                   : A bitfield corresponding to the joystick buttons' current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 1. (type:uint16_t)
        buttons2                  : A bitfield corresponding to the joystick buttons' 16-31 current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 16. (type:uint16_t)
        enabled_extensions        : Set bits to 1 to indicate which of the following extension fields contain valid data: bit 0: pitch, bit 1: roll, bit 2: aux1, bit 3: aux2, bit 4: aux3, bit 5: aux4, bit 6: aux5, bit 7: aux6 (type:uint8_t)
        s                         : Pitch-only-axis, normalized to the range [-1000,1000]. Generally corresponds to pitch on vehicles with additional degrees of freedom. Valid if bit 0 of enabled_extensions field is set. Set to 0 if invalid. (type:int16_t)
        t                         : Roll-only-axis, normalized to the range [-1000,1000]. Generally corresponds to roll on vehicles with additional degrees of freedom. Valid if bit 1 of enabled_extensions field is set. Set to 0 if invalid. (type:int16_t)
        aux1                      : Aux continuous input field 1. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 2 of enabled_extensions field is set. 0 if bit 2 is unset. (type:int16_t)
        aux2                      : Aux continuous input field 2. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 3 of enabled_extensions field is set. 0 if bit 3 is unset. (type:int16_t)
        aux3                      : Aux continuous input field 3. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 4 of enabled_extensions field is set. 0 if bit 4 is unset. (type:int16_t)
        aux4                      : Aux continuous input field 4. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 5 of enabled_extensions field is set. 0 if bit 5 is unset. (type:int16_t)
        aux5                      : Aux continuous input field 5. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 6 of enabled_extensions field is set. 0 if bit 6 is unset. (type:int16_t)
        aux6                      : Aux continuous input field 6. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 7 of enabled_extensions field is set. 0 if bit 7 is unset. (type:int16_t)

        """
        return MAVLink_manual_control_message(target, x, y, z, r, buttons, buttons2, enabled_extensions, s, t, aux1, aux2, aux3, aux4, aux5, aux6)

## manual_control_send
    def manual_control_send(self, target: int, x: int, y: int, z: int, r: int, buttons: int, buttons2: int = 0, enabled_extensions: int = 0, s: int = 0, t: int = 0, aux1: int = 0, aux2: int = 0, aux3: int = 0, aux4: int = 0, aux5: int = 0, aux6: int = 0, force_mavlink1: bool = False) -> None:
        """
        This message provides an API for manually controlling the vehicle
        using standard joystick axes nomenclature, along with a
        joystick-like input device. Unused axes can be disabled and
        buttons states are transmitted as individual on/off bits of a
        bitmask

        target                    : The system to be controlled. (type:uint8_t)
        x                         : X-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to forward(1000)-backward(-1000) movement on a joystick and the pitch of a vehicle. (type:int16_t)
        y                         : Y-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to left(-1000)-right(1000) movement on a joystick and the roll of a vehicle. (type:int16_t)
        z                         : Z-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to a separate slider movement with maximum being 1000 and minimum being -1000 on a joystick and the thrust of a vehicle. Positive values are positive thrust, negative values are negative thrust. (type:int16_t)
        r                         : R-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to a twisting of the joystick, with counter-clockwise being 1000 and clockwise being -1000, and the yaw of a vehicle. (type:int16_t)
        buttons                   : A bitfield corresponding to the joystick buttons' current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 1. (type:uint16_t)
        buttons2                  : A bitfield corresponding to the joystick buttons' 16-31 current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 16. (type:uint16_t)
        enabled_extensions        : Set bits to 1 to indicate which of the following extension fields contain valid data: bit 0: pitch, bit 1: roll, bit 2: aux1, bit 3: aux2, bit 4: aux3, bit 5: aux4, bit 6: aux5, bit 7: aux6 (type:uint8_t)
        s                         : Pitch-only-axis, normalized to the range [-1000,1000]. Generally corresponds to pitch on vehicles with additional degrees of freedom. Valid if bit 0 of enabled_extensions field is set. Set to 0 if invalid. (type:int16_t)
        t                         : Roll-only-axis, normalized to the range [-1000,1000]. Generally corresponds to roll on vehicles with additional degrees of freedom. Valid if bit 1 of enabled_extensions field is set. Set to 0 if invalid. (type:int16_t)
        aux1                      : Aux continuous input field 1. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 2 of enabled_extensions field is set. 0 if bit 2 is unset. (type:int16_t)
        aux2                      : Aux continuous input field 2. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 3 of enabled_extensions field is set. 0 if bit 3 is unset. (type:int16_t)
        aux3                      : Aux continuous input field 3. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 4 of enabled_extensions field is set. 0 if bit 4 is unset. (type:int16_t)
        aux4                      : Aux continuous input field 4. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 5 of enabled_extensions field is set. 0 if bit 5 is unset. (type:int16_t)
        aux5                      : Aux continuous input field 5. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 6 of enabled_extensions field is set. 0 if bit 6 is unset. (type:int16_t)
        aux6                      : Aux continuous input field 6. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 7 of enabled_extensions field is set. 0 if bit 7 is unset. (type:int16_t)

        """
        self.send(self.manual_control_encode(target, x, y, z, r, buttons, buttons2, enabled_extensions, s, t, aux1, aux2, aux3, aux4, aux5, aux6), force_mavlink1=force_mavlink1)

## rc_channels_override_encode
    def rc_channels_override_encode(self, target_system: int, target_component: int, chan1_raw: int, chan2_raw: int, chan3_raw: int, chan4_raw: int, chan5_raw: int, chan6_raw: int, chan7_raw: int, chan8_raw: int, chan9_raw: int = 0, chan10_raw: int = 0, chan11_raw: int = 0, chan12_raw: int = 0, chan13_raw: int = 0, chan14_raw: int = 0, chan15_raw: int = 0, chan16_raw: int = 0, chan17_raw: int = 0, chan18_raw: int = 0) -> MAVLink_rc_channels_override_message:
        """
        The RAW values of the RC channels sent to the MAV to override info
        received from the RC radio. The standard PPM modulation is as
        follows: 1000 microseconds: 0%, 2000 microseconds: 100%.
        Individual receivers/transmitters might violate this
        specification.  Note carefully the semantic differences
        between the first 8 channels and the subsequent channels

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        chan1_raw                 : RC channel 1 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan2_raw                 : RC channel 2 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan3_raw                 : RC channel 3 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan4_raw                 : RC channel 4 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan5_raw                 : RC channel 5 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan6_raw                 : RC channel 6 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan7_raw                 : RC channel 7 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan8_raw                 : RC channel 8 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan9_raw                 : RC channel 9 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan10_raw                : RC channel 10 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan11_raw                : RC channel 11 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan12_raw                : RC channel 12 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan13_raw                : RC channel 13 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan14_raw                : RC channel 14 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan15_raw                : RC channel 15 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan16_raw                : RC channel 16 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan17_raw                : RC channel 17 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan18_raw                : RC channel 18 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)

        """
        return MAVLink_rc_channels_override_message(target_system, target_component, chan1_raw, chan2_raw, chan3_raw, chan4_raw, chan5_raw, chan6_raw, chan7_raw, chan8_raw, chan9_raw, chan10_raw, chan11_raw, chan12_raw, chan13_raw, chan14_raw, chan15_raw, chan16_raw, chan17_raw, chan18_raw)

## rc_channels_override_send
    def rc_channels_override_send(self, target_system: int, target_component: int, chan1_raw: int, chan2_raw: int, chan3_raw: int, chan4_raw: int, chan5_raw: int, chan6_raw: int, chan7_raw: int, chan8_raw: int, chan9_raw: int = 0, chan10_raw: int = 0, chan11_raw: int = 0, chan12_raw: int = 0, chan13_raw: int = 0, chan14_raw: int = 0, chan15_raw: int = 0, chan16_raw: int = 0, chan17_raw: int = 0, chan18_raw: int = 0, force_mavlink1: bool = False) -> None:
        """
        The RAW values of the RC channels sent to the MAV to override info
        received from the RC radio. The standard PPM modulation is as
        follows: 1000 microseconds: 0%, 2000 microseconds: 100%.
        Individual receivers/transmitters might violate this
        specification.  Note carefully the semantic differences
        between the first 8 channels and the subsequent channels

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        chan1_raw                 : RC channel 1 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan2_raw                 : RC channel 2 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan3_raw                 : RC channel 3 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan4_raw                 : RC channel 4 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan5_raw                 : RC channel 5 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan6_raw                 : RC channel 6 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan7_raw                 : RC channel 7 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan8_raw                 : RC channel 8 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan9_raw                 : RC channel 9 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan10_raw                : RC channel 10 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan11_raw                : RC channel 11 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan12_raw                : RC channel 12 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan13_raw                : RC channel 13 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan14_raw                : RC channel 14 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan15_raw                : RC channel 15 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan16_raw                : RC channel 16 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan17_raw                : RC channel 17 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)
        chan18_raw                : RC channel 18 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. [us] (type:uint16_t)

        """
        self.send(self.rc_channels_override_encode(target_system, target_component, chan1_raw, chan2_raw, chan3_raw, chan4_raw, chan5_raw, chan6_raw, chan7_raw, chan8_raw, chan9_raw, chan10_raw, chan11_raw, chan12_raw, chan13_raw, chan14_raw, chan15_raw, chan16_raw, chan17_raw, chan18_raw), force_mavlink1=force_mavlink1)

## mission_item_int_encode
    def mission_item_int_encode(self, target_system: int, target_component: int, seq: int, frame: int, command: int, current: int, autocontinue: int, param1: float, param2: float, param3: float, param4: float, x: int, y: int, z: float, mission_type: int = 0) -> MAVLink_mission_item_int_message:
        """
        Message encoding a mission item. This message is emitted to announce
        the presence of a mission item and to set a mission item on
        the system. The mission item can be either in x, y, z meters
        (type: LOCAL) or x:lat, y:lon, z:altitude. Local frame is
        Z-down, right handed (NED), global frame is Z-up, right handed
        (ENU). NaN or INT32_MAX may be used in float/integer params
        (respectively) to indicate optional/default values (e.g. to
        use the component's current latitude, yaw rather than a
        specific value). See also
        https://mavlink.io/en/services/mission.html.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Waypoint ID (sequence number). Starts at zero. Increases monotonically for each waypoint, no gaps in the sequence (0,1,2,3,4). (type:uint16_t)
        frame                     : The coordinate system of the waypoint. (type:uint8_t, values:MAV_FRAME)
        command                   : The scheduled action for the waypoint. (type:uint16_t, values:MAV_CMD)
        current                   : false:0, true:1 (type:uint8_t)
        autocontinue              : Autocontinue to next waypoint (type:uint8_t)
        param1                    : PARAM1, see MAV_CMD enum (type:float)
        param2                    : PARAM2, see MAV_CMD enum (type:float)
        param3                    : PARAM3, see MAV_CMD enum (type:float)
        param4                    : PARAM4, see MAV_CMD enum (type:float)
        x                         : PARAM5 / local: x position in meters * 1e4, global: latitude in degrees * 10^7 (type:int32_t)
        y                         : PARAM6 / y position: local: x position in meters * 1e4, global: longitude in degrees *10^7 (type:int32_t)
        z                         : PARAM7 / z position: global: altitude in meters (relative or absolute, depending on frame. (type:float)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        return MAVLink_mission_item_int_message(target_system, target_component, seq, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z, mission_type)

## mission_item_int_send
    def mission_item_int_send(self, target_system: int, target_component: int, seq: int, frame: int, command: int, current: int, autocontinue: int, param1: float, param2: float, param3: float, param4: float, x: int, y: int, z: float, mission_type: int = 0, force_mavlink1: bool = False) -> None:
        """
        Message encoding a mission item. This message is emitted to announce
        the presence of a mission item and to set a mission item on
        the system. The mission item can be either in x, y, z meters
        (type: LOCAL) or x:lat, y:lon, z:altitude. Local frame is
        Z-down, right handed (NED), global frame is Z-up, right handed
        (ENU). NaN or INT32_MAX may be used in float/integer params
        (respectively) to indicate optional/default values (e.g. to
        use the component's current latitude, yaw rather than a
        specific value). See also
        https://mavlink.io/en/services/mission.html.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        seq                       : Waypoint ID (sequence number). Starts at zero. Increases monotonically for each waypoint, no gaps in the sequence (0,1,2,3,4). (type:uint16_t)
        frame                     : The coordinate system of the waypoint. (type:uint8_t, values:MAV_FRAME)
        command                   : The scheduled action for the waypoint. (type:uint16_t, values:MAV_CMD)
        current                   : false:0, true:1 (type:uint8_t)
        autocontinue              : Autocontinue to next waypoint (type:uint8_t)
        param1                    : PARAM1, see MAV_CMD enum (type:float)
        param2                    : PARAM2, see MAV_CMD enum (type:float)
        param3                    : PARAM3, see MAV_CMD enum (type:float)
        param4                    : PARAM4, see MAV_CMD enum (type:float)
        x                         : PARAM5 / local: x position in meters * 1e4, global: latitude in degrees * 10^7 (type:int32_t)
        y                         : PARAM6 / y position: local: x position in meters * 1e4, global: longitude in degrees *10^7 (type:int32_t)
        z                         : PARAM7 / z position: global: altitude in meters (relative or absolute, depending on frame. (type:float)
        mission_type              : Mission type. (type:uint8_t, values:MAV_MISSION_TYPE)

        """
        self.send(self.mission_item_int_encode(target_system, target_component, seq, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z, mission_type), force_mavlink1=force_mavlink1)

## vfr_hud_encode
    def vfr_hud_encode(self, airspeed: float, groundspeed: float, heading: int, throttle: int, alt: float, climb: float) -> MAVLink_vfr_hud_message:
        """
        Metrics typically displayed on a HUD for fixed wing aircraft.

        airspeed                  : Vehicle speed in form appropriate for vehicle type. For standard aircraft this is typically calibrated airspeed (CAS) or indicated airspeed (IAS) - either of which can be used by a pilot to estimate stall speed. [m/s] (type:float)
        groundspeed               : Current ground speed. [m/s] (type:float)
        heading                   : Current heading in compass units (0-360, 0=north). [deg] (type:int16_t)
        throttle                  : Current throttle setting (0 to 100). [%] (type:uint16_t)
        alt                       : Current altitude (MSL). [m] (type:float)
        climb                     : Current climb rate. [m/s] (type:float)

        """
        return MAVLink_vfr_hud_message(airspeed, groundspeed, heading, throttle, alt, climb)

## vfr_hud_send
    def vfr_hud_send(self, airspeed: float, groundspeed: float, heading: int, throttle: int, alt: float, climb: float, force_mavlink1: bool = False) -> None:
        """
        Metrics typically displayed on a HUD for fixed wing aircraft.

        airspeed                  : Vehicle speed in form appropriate for vehicle type. For standard aircraft this is typically calibrated airspeed (CAS) or indicated airspeed (IAS) - either of which can be used by a pilot to estimate stall speed. [m/s] (type:float)
        groundspeed               : Current ground speed. [m/s] (type:float)
        heading                   : Current heading in compass units (0-360, 0=north). [deg] (type:int16_t)
        throttle                  : Current throttle setting (0 to 100). [%] (type:uint16_t)
        alt                       : Current altitude (MSL). [m] (type:float)
        climb                     : Current climb rate. [m/s] (type:float)

        """
        self.send(self.vfr_hud_encode(airspeed, groundspeed, heading, throttle, alt, climb), force_mavlink1=force_mavlink1)

## command_int_encode
    def command_int_encode(self, target_system: int, target_component: int, frame: int, command: int, current: int, autocontinue: int, param1: float, param2: float, param3: float, param4: float, x: int, y: int, z: float) -> MAVLink_command_int_message:
        """
        Message encoding a command with parameters as scaled integers. Scaling
        depends on the actual command value. The command microservice
        is documented at https://mavlink.io/en/services/command.html

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        frame                     : The coordinate system of the COMMAND. (type:uint8_t, values:MAV_FRAME)
        command                   : The scheduled action for the mission item. (type:uint16_t, values:MAV_CMD)
        current                   : Not used. (type:uint8_t)
        autocontinue              : Not used (set 0). (type:uint8_t)
        param1                    : PARAM1, see MAV_CMD enum (type:float)
        param2                    : PARAM2, see MAV_CMD enum (type:float)
        param3                    : PARAM3, see MAV_CMD enum (type:float)
        param4                    : PARAM4, see MAV_CMD enum (type:float)
        x                         : PARAM5 / local: x position in meters * 1e4, global: latitude in degrees * 10^7 (type:int32_t)
        y                         : PARAM6 / local: y position in meters * 1e4, global: longitude in degrees * 10^7 (type:int32_t)
        z                         : PARAM7 / z position: global: altitude in meters (relative or absolute, depending on frame). (type:float)

        """
        return MAVLink_command_int_message(target_system, target_component, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z)

## command_int_send
    def command_int_send(self, target_system: int, target_component: int, frame: int, command: int, current: int, autocontinue: int, param1: float, param2: float, param3: float, param4: float, x: int, y: int, z: float, force_mavlink1: bool = False) -> None:
        """
        Message encoding a command with parameters as scaled integers. Scaling
        depends on the actual command value. The command microservice
        is documented at https://mavlink.io/en/services/command.html

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        frame                     : The coordinate system of the COMMAND. (type:uint8_t, values:MAV_FRAME)
        command                   : The scheduled action for the mission item. (type:uint16_t, values:MAV_CMD)
        current                   : Not used. (type:uint8_t)
        autocontinue              : Not used (set 0). (type:uint8_t)
        param1                    : PARAM1, see MAV_CMD enum (type:float)
        param2                    : PARAM2, see MAV_CMD enum (type:float)
        param3                    : PARAM3, see MAV_CMD enum (type:float)
        param4                    : PARAM4, see MAV_CMD enum (type:float)
        x                         : PARAM5 / local: x position in meters * 1e4, global: latitude in degrees * 10^7 (type:int32_t)
        y                         : PARAM6 / local: y position in meters * 1e4, global: longitude in degrees * 10^7 (type:int32_t)
        z                         : PARAM7 / z position: global: altitude in meters (relative or absolute, depending on frame). (type:float)

        """
        self.send(self.command_int_encode(target_system, target_component, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z), force_mavlink1=force_mavlink1)

## command_long_encode
    def command_long_encode(self, target_system: int, target_component: int, command: int, confirmation: int, param1: float, param2: float, param3: float, param4: float, param5: float, param6: float, param7: float) -> MAVLink_command_long_message:
        """
        Send a command with up to seven parameters to the MAV. The command
        microservice is documented at
        https://mavlink.io/en/services/command.html

        target_system             : System which should execute the command (type:uint8_t)
        target_component          : Component which should execute the command, 0 for all components (type:uint8_t)
        command                   : Command ID (of command to send). (type:uint16_t, values:MAV_CMD)
        confirmation              : 0: First transmission of this command. 1-255: Confirmation transmissions (e.g. for kill command) (type:uint8_t)
        param1                    : Parameter 1 (for the specific command). (type:float)
        param2                    : Parameter 2 (for the specific command). (type:float)
        param3                    : Parameter 3 (for the specific command). (type:float)
        param4                    : Parameter 4 (for the specific command). (type:float)
        param5                    : Parameter 5 (for the specific command). (type:float)
        param6                    : Parameter 6 (for the specific command). (type:float)
        param7                    : Parameter 7 (for the specific command). (type:float)

        """
        return MAVLink_command_long_message(target_system, target_component, command, confirmation, param1, param2, param3, param4, param5, param6, param7)

## command_long_send
    def command_long_send(self, target_system: int, target_component: int, command: int, confirmation: int, param1: float, param2: float, param3: float, param4: float, param5: float, param6: float, param7: float, force_mavlink1: bool = False) -> None:
        """
        Send a command with up to seven parameters to the MAV. The command
        microservice is documented at
        https://mavlink.io/en/services/command.html

        target_system             : System which should execute the command (type:uint8_t)
        target_component          : Component which should execute the command, 0 for all components (type:uint8_t)
        command                   : Command ID (of command to send). (type:uint16_t, values:MAV_CMD)
        confirmation              : 0: First transmission of this command. 1-255: Confirmation transmissions (e.g. for kill command) (type:uint8_t)
        param1                    : Parameter 1 (for the specific command). (type:float)
        param2                    : Parameter 2 (for the specific command). (type:float)
        param3                    : Parameter 3 (for the specific command). (type:float)
        param4                    : Parameter 4 (for the specific command). (type:float)
        param5                    : Parameter 5 (for the specific command). (type:float)
        param6                    : Parameter 6 (for the specific command). (type:float)
        param7                    : Parameter 7 (for the specific command). (type:float)

        """
        self.send(self.command_long_encode(target_system, target_component, command, confirmation, param1, param2, param3, param4, param5, param6, param7), force_mavlink1=force_mavlink1)

## command_ack_encode
    def command_ack_encode(self, command: int, result: int, progress: int = 0, result_param2: int = 0, target_system: int = 0, target_component: int = 0) -> MAVLink_command_ack_message:
        """
        Report status of a command. Includes feedback whether the command was
        executed. The command microservice is documented at
        https://mavlink.io/en/services/command.html

        command                   : Command ID (of acknowledged command). (type:uint16_t, values:MAV_CMD)
        result                    : Result of command. (type:uint8_t, values:MAV_RESULT)
        progress                  : Also used as result_param1, it can be set with a enum containing the errors reasons of why the command was denied or the progress percentage or 255 if unknown the progress when result is MAV_RESULT_IN_PROGRESS. (type:uint8_t)
        result_param2             : Additional parameter of the result, example: which parameter of MAV_CMD_NAV_WAYPOINT caused it to be denied. (type:int32_t)
        target_system             : System which requested the command to be executed (type:uint8_t)
        target_component          : Component which requested the command to be executed (type:uint8_t)

        """
        return MAVLink_command_ack_message(command, result, progress, result_param2, target_system, target_component)

## command_ack_send
    def command_ack_send(self, command: int, result: int, progress: int = 0, result_param2: int = 0, target_system: int = 0, target_component: int = 0, force_mavlink1: bool = False) -> None:
        """
        Report status of a command. Includes feedback whether the command was
        executed. The command microservice is documented at
        https://mavlink.io/en/services/command.html

        command                   : Command ID (of acknowledged command). (type:uint16_t, values:MAV_CMD)
        result                    : Result of command. (type:uint8_t, values:MAV_RESULT)
        progress                  : Also used as result_param1, it can be set with a enum containing the errors reasons of why the command was denied or the progress percentage or 255 if unknown the progress when result is MAV_RESULT_IN_PROGRESS. (type:uint8_t)
        result_param2             : Additional parameter of the result, example: which parameter of MAV_CMD_NAV_WAYPOINT caused it to be denied. (type:int32_t)
        target_system             : System which requested the command to be executed (type:uint8_t)
        target_component          : Component which requested the command to be executed (type:uint8_t)

        """
        self.send(self.command_ack_encode(command, result, progress, result_param2, target_system, target_component), force_mavlink1=force_mavlink1)

## manual_setpoint_encode
    def manual_setpoint_encode(self, time_boot_ms: int, roll: float, pitch: float, yaw: float, thrust: float, mode_switch: int, manual_override_switch: int) -> MAVLink_manual_setpoint_message:
        """
        Setpoint in roll, pitch, yaw and thrust from the operator

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        roll                      : Desired roll rate [rad/s] (type:float)
        pitch                     : Desired pitch rate [rad/s] (type:float)
        yaw                       : Desired yaw rate [rad/s] (type:float)
        thrust                    : Collective thrust, normalized to 0 .. 1 (type:float)
        mode_switch               : Flight mode switch position, 0.. 255 (type:uint8_t)
        manual_override_switch        : Override mode switch position, 0.. 255 (type:uint8_t)

        """
        return MAVLink_manual_setpoint_message(time_boot_ms, roll, pitch, yaw, thrust, mode_switch, manual_override_switch)

## manual_setpoint_send
    def manual_setpoint_send(self, time_boot_ms: int, roll: float, pitch: float, yaw: float, thrust: float, mode_switch: int, manual_override_switch: int, force_mavlink1: bool = False) -> None:
        """
        Setpoint in roll, pitch, yaw and thrust from the operator

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        roll                      : Desired roll rate [rad/s] (type:float)
        pitch                     : Desired pitch rate [rad/s] (type:float)
        yaw                       : Desired yaw rate [rad/s] (type:float)
        thrust                    : Collective thrust, normalized to 0 .. 1 (type:float)
        mode_switch               : Flight mode switch position, 0.. 255 (type:uint8_t)
        manual_override_switch        : Override mode switch position, 0.. 255 (type:uint8_t)

        """
        self.send(self.manual_setpoint_encode(time_boot_ms, roll, pitch, yaw, thrust, mode_switch, manual_override_switch), force_mavlink1=force_mavlink1)

## set_attitude_target_encode
    def set_attitude_target_encode(self, time_boot_ms: int, target_system: int, target_component: int, type_mask: int, q: Sequence[float], body_roll_rate: float, body_pitch_rate: float, body_yaw_rate: float, thrust: float) -> MAVLink_set_attitude_target_message:
        """
        Sets a desired vehicle attitude. Used by an external controller to
        command the vehicle (manual controller or other system).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint8_t, values:ATTITUDE_TARGET_TYPEMASK)
        q                         : Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        body_roll_rate            : Body roll rate [rad/s] (type:float)
        body_pitch_rate           : Body pitch rate [rad/s] (type:float)
        body_yaw_rate             : Body yaw rate [rad/s] (type:float)
        thrust                    : Collective thrust, normalized to 0 .. 1 (-1 .. 1 for vehicles capable of reverse trust) (type:float)

        """
        return MAVLink_set_attitude_target_message(time_boot_ms, target_system, target_component, type_mask, q, body_roll_rate, body_pitch_rate, body_yaw_rate, thrust)

## set_attitude_target_send
    def set_attitude_target_send(self, time_boot_ms: int, target_system: int, target_component: int, type_mask: int, q: Sequence[float], body_roll_rate: float, body_pitch_rate: float, body_yaw_rate: float, thrust: float, force_mavlink1: bool = False) -> None:
        """
        Sets a desired vehicle attitude. Used by an external controller to
        command the vehicle (manual controller or other system).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint8_t, values:ATTITUDE_TARGET_TYPEMASK)
        q                         : Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        body_roll_rate            : Body roll rate [rad/s] (type:float)
        body_pitch_rate           : Body pitch rate [rad/s] (type:float)
        body_yaw_rate             : Body yaw rate [rad/s] (type:float)
        thrust                    : Collective thrust, normalized to 0 .. 1 (-1 .. 1 for vehicles capable of reverse trust) (type:float)

        """
        self.send(self.set_attitude_target_encode(time_boot_ms, target_system, target_component, type_mask, q, body_roll_rate, body_pitch_rate, body_yaw_rate, thrust), force_mavlink1=force_mavlink1)

## attitude_target_encode
    def attitude_target_encode(self, time_boot_ms: int, type_mask: int, q: Sequence[float], body_roll_rate: float, body_pitch_rate: float, body_yaw_rate: float, thrust: float) -> MAVLink_attitude_target_message:
        """
        Reports the current commanded attitude of the vehicle as specified by
        the autopilot. This should match the commands sent in a
        SET_ATTITUDE_TARGET message if the vehicle is being controlled
        this way.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint8_t, values:ATTITUDE_TARGET_TYPEMASK)
        q                         : Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        body_roll_rate            : Body roll rate [rad/s] (type:float)
        body_pitch_rate           : Body pitch rate [rad/s] (type:float)
        body_yaw_rate             : Body yaw rate [rad/s] (type:float)
        thrust                    : Collective thrust, normalized to 0 .. 1 (-1 .. 1 for vehicles capable of reverse trust) (type:float)

        """
        return MAVLink_attitude_target_message(time_boot_ms, type_mask, q, body_roll_rate, body_pitch_rate, body_yaw_rate, thrust)

## attitude_target_send
    def attitude_target_send(self, time_boot_ms: int, type_mask: int, q: Sequence[float], body_roll_rate: float, body_pitch_rate: float, body_yaw_rate: float, thrust: float, force_mavlink1: bool = False) -> None:
        """
        Reports the current commanded attitude of the vehicle as specified by
        the autopilot. This should match the commands sent in a
        SET_ATTITUDE_TARGET message if the vehicle is being controlled
        this way.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint8_t, values:ATTITUDE_TARGET_TYPEMASK)
        q                         : Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        body_roll_rate            : Body roll rate [rad/s] (type:float)
        body_pitch_rate           : Body pitch rate [rad/s] (type:float)
        body_yaw_rate             : Body yaw rate [rad/s] (type:float)
        thrust                    : Collective thrust, normalized to 0 .. 1 (-1 .. 1 for vehicles capable of reverse trust) (type:float)

        """
        self.send(self.attitude_target_encode(time_boot_ms, type_mask, q, body_roll_rate, body_pitch_rate, body_yaw_rate, thrust), force_mavlink1=force_mavlink1)

## set_position_target_local_ned_encode
    def set_position_target_local_ned_encode(self, time_boot_ms: int, target_system: int, target_component: int, coordinate_frame: int, type_mask: int, x: float, y: float, z: float, vx: float, vy: float, vz: float, afx: float, afy: float, afz: float, yaw: float, yaw_rate: float) -> MAVLink_set_position_target_local_ned_message:
        """
        Sets a desired vehicle position in a local north-east-down coordinate
        frame. Used by an external controller to command the vehicle
        (manual controller or other system).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        coordinate_frame          : Valid options are: MAV_FRAME_LOCAL_NED = 1, MAV_FRAME_LOCAL_OFFSET_NED = 7, MAV_FRAME_BODY_NED = 8, MAV_FRAME_BODY_OFFSET_NED = 9 (type:uint8_t, values:MAV_FRAME)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint16_t, values:POSITION_TARGET_TYPEMASK)
        x                         : X Position in NED frame [m] (type:float)
        y                         : Y Position in NED frame [m] (type:float)
        z                         : Z Position in NED frame (note, altitude is negative in NED) [m] (type:float)
        vx                        : X velocity in NED frame [m/s] (type:float)
        vy                        : Y velocity in NED frame [m/s] (type:float)
        vz                        : Z velocity in NED frame [m/s] (type:float)
        afx                       : X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afy                       : Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afz                       : Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        yaw                       : yaw setpoint [rad] (type:float)
        yaw_rate                  : yaw rate setpoint [rad/s] (type:float)

        """
        return MAVLink_set_position_target_local_ned_message(time_boot_ms, target_system, target_component, coordinate_frame, type_mask, x, y, z, vx, vy, vz, afx, afy, afz, yaw, yaw_rate)

## set_position_target_local_ned_send
    def set_position_target_local_ned_send(self, time_boot_ms: int, target_system: int, target_component: int, coordinate_frame: int, type_mask: int, x: float, y: float, z: float, vx: float, vy: float, vz: float, afx: float, afy: float, afz: float, yaw: float, yaw_rate: float, force_mavlink1: bool = False) -> None:
        """
        Sets a desired vehicle position in a local north-east-down coordinate
        frame. Used by an external controller to command the vehicle
        (manual controller or other system).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        coordinate_frame          : Valid options are: MAV_FRAME_LOCAL_NED = 1, MAV_FRAME_LOCAL_OFFSET_NED = 7, MAV_FRAME_BODY_NED = 8, MAV_FRAME_BODY_OFFSET_NED = 9 (type:uint8_t, values:MAV_FRAME)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint16_t, values:POSITION_TARGET_TYPEMASK)
        x                         : X Position in NED frame [m] (type:float)
        y                         : Y Position in NED frame [m] (type:float)
        z                         : Z Position in NED frame (note, altitude is negative in NED) [m] (type:float)
        vx                        : X velocity in NED frame [m/s] (type:float)
        vy                        : Y velocity in NED frame [m/s] (type:float)
        vz                        : Z velocity in NED frame [m/s] (type:float)
        afx                       : X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afy                       : Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afz                       : Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        yaw                       : yaw setpoint [rad] (type:float)
        yaw_rate                  : yaw rate setpoint [rad/s] (type:float)

        """
        self.send(self.set_position_target_local_ned_encode(time_boot_ms, target_system, target_component, coordinate_frame, type_mask, x, y, z, vx, vy, vz, afx, afy, afz, yaw, yaw_rate), force_mavlink1=force_mavlink1)

## position_target_local_ned_encode
    def position_target_local_ned_encode(self, time_boot_ms: int, coordinate_frame: int, type_mask: int, x: float, y: float, z: float, vx: float, vy: float, vz: float, afx: float, afy: float, afz: float, yaw: float, yaw_rate: float) -> MAVLink_position_target_local_ned_message:
        """
        Reports the current commanded vehicle position, velocity, and
        acceleration as specified by the autopilot. This should match
        the commands sent in SET_POSITION_TARGET_LOCAL_NED if the
        vehicle is being controlled this way.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        coordinate_frame          : Valid options are: MAV_FRAME_LOCAL_NED = 1, MAV_FRAME_LOCAL_OFFSET_NED = 7, MAV_FRAME_BODY_NED = 8, MAV_FRAME_BODY_OFFSET_NED = 9 (type:uint8_t, values:MAV_FRAME)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint16_t, values:POSITION_TARGET_TYPEMASK)
        x                         : X Position in NED frame [m] (type:float)
        y                         : Y Position in NED frame [m] (type:float)
        z                         : Z Position in NED frame (note, altitude is negative in NED) [m] (type:float)
        vx                        : X velocity in NED frame [m/s] (type:float)
        vy                        : Y velocity in NED frame [m/s] (type:float)
        vz                        : Z velocity in NED frame [m/s] (type:float)
        afx                       : X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afy                       : Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afz                       : Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        yaw                       : yaw setpoint [rad] (type:float)
        yaw_rate                  : yaw rate setpoint [rad/s] (type:float)

        """
        return MAVLink_position_target_local_ned_message(time_boot_ms, coordinate_frame, type_mask, x, y, z, vx, vy, vz, afx, afy, afz, yaw, yaw_rate)

## position_target_local_ned_send
    def position_target_local_ned_send(self, time_boot_ms: int, coordinate_frame: int, type_mask: int, x: float, y: float, z: float, vx: float, vy: float, vz: float, afx: float, afy: float, afz: float, yaw: float, yaw_rate: float, force_mavlink1: bool = False) -> None:
        """
        Reports the current commanded vehicle position, velocity, and
        acceleration as specified by the autopilot. This should match
        the commands sent in SET_POSITION_TARGET_LOCAL_NED if the
        vehicle is being controlled this way.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        coordinate_frame          : Valid options are: MAV_FRAME_LOCAL_NED = 1, MAV_FRAME_LOCAL_OFFSET_NED = 7, MAV_FRAME_BODY_NED = 8, MAV_FRAME_BODY_OFFSET_NED = 9 (type:uint8_t, values:MAV_FRAME)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint16_t, values:POSITION_TARGET_TYPEMASK)
        x                         : X Position in NED frame [m] (type:float)
        y                         : Y Position in NED frame [m] (type:float)
        z                         : Z Position in NED frame (note, altitude is negative in NED) [m] (type:float)
        vx                        : X velocity in NED frame [m/s] (type:float)
        vy                        : Y velocity in NED frame [m/s] (type:float)
        vz                        : Z velocity in NED frame [m/s] (type:float)
        afx                       : X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afy                       : Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afz                       : Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        yaw                       : yaw setpoint [rad] (type:float)
        yaw_rate                  : yaw rate setpoint [rad/s] (type:float)

        """
        self.send(self.position_target_local_ned_encode(time_boot_ms, coordinate_frame, type_mask, x, y, z, vx, vy, vz, afx, afy, afz, yaw, yaw_rate), force_mavlink1=force_mavlink1)

## set_position_target_global_int_encode
    def set_position_target_global_int_encode(self, time_boot_ms: int, target_system: int, target_component: int, coordinate_frame: int, type_mask: int, lat_int: int, lon_int: int, alt: float, vx: float, vy: float, vz: float, afx: float, afy: float, afz: float, yaw: float, yaw_rate: float) -> MAVLink_set_position_target_global_int_message:
        """
        Sets a desired vehicle position, velocity, and/or acceleration in a
        global coordinate system (WGS84). Used by an external
        controller to command the vehicle (manual controller or other
        system).

        time_boot_ms              : Timestamp (time since system boot). The rationale for the timestamp in the setpoint is to allow the system to compensate for the transport delay of the setpoint. This allows the system to compensate processing latency. [ms] (type:uint32_t)
        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        coordinate_frame          : Valid options are: MAV_FRAME_GLOBAL = 0, MAV_FRAME_GLOBAL_RELATIVE_ALT = 3, MAV_FRAME_GLOBAL_TERRAIN_ALT = 10 (MAV_FRAME_GLOBAL_INT, MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, MAV_FRAME_GLOBAL_TERRAIN_ALT_INT are allowed synonyms, but have been deprecated) (type:uint8_t, values:MAV_FRAME)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint16_t, values:POSITION_TARGET_TYPEMASK)
        lat_int                   : Latitude in WGS84 frame [degE7] (type:int32_t)
        lon_int                   : Longitude in WGS84 frame [degE7] (type:int32_t)
        alt                       : Altitude (MSL, Relative to home, or AGL - depending on frame) [m] (type:float)
        vx                        : X velocity in NED frame [m/s] (type:float)
        vy                        : Y velocity in NED frame [m/s] (type:float)
        vz                        : Z velocity in NED frame [m/s] (type:float)
        afx                       : X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afy                       : Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afz                       : Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        yaw                       : yaw setpoint [rad] (type:float)
        yaw_rate                  : yaw rate setpoint [rad/s] (type:float)

        """
        return MAVLink_set_position_target_global_int_message(time_boot_ms, target_system, target_component, coordinate_frame, type_mask, lat_int, lon_int, alt, vx, vy, vz, afx, afy, afz, yaw, yaw_rate)

## set_position_target_global_int_send
    def set_position_target_global_int_send(self, time_boot_ms: int, target_system: int, target_component: int, coordinate_frame: int, type_mask: int, lat_int: int, lon_int: int, alt: float, vx: float, vy: float, vz: float, afx: float, afy: float, afz: float, yaw: float, yaw_rate: float, force_mavlink1: bool = False) -> None:
        """
        Sets a desired vehicle position, velocity, and/or acceleration in a
        global coordinate system (WGS84). Used by an external
        controller to command the vehicle (manual controller or other
        system).

        time_boot_ms              : Timestamp (time since system boot). The rationale for the timestamp in the setpoint is to allow the system to compensate for the transport delay of the setpoint. This allows the system to compensate processing latency. [ms] (type:uint32_t)
        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        coordinate_frame          : Valid options are: MAV_FRAME_GLOBAL = 0, MAV_FRAME_GLOBAL_RELATIVE_ALT = 3, MAV_FRAME_GLOBAL_TERRAIN_ALT = 10 (MAV_FRAME_GLOBAL_INT, MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, MAV_FRAME_GLOBAL_TERRAIN_ALT_INT are allowed synonyms, but have been deprecated) (type:uint8_t, values:MAV_FRAME)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint16_t, values:POSITION_TARGET_TYPEMASK)
        lat_int                   : Latitude in WGS84 frame [degE7] (type:int32_t)
        lon_int                   : Longitude in WGS84 frame [degE7] (type:int32_t)
        alt                       : Altitude (MSL, Relative to home, or AGL - depending on frame) [m] (type:float)
        vx                        : X velocity in NED frame [m/s] (type:float)
        vy                        : Y velocity in NED frame [m/s] (type:float)
        vz                        : Z velocity in NED frame [m/s] (type:float)
        afx                       : X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afy                       : Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afz                       : Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        yaw                       : yaw setpoint [rad] (type:float)
        yaw_rate                  : yaw rate setpoint [rad/s] (type:float)

        """
        self.send(self.set_position_target_global_int_encode(time_boot_ms, target_system, target_component, coordinate_frame, type_mask, lat_int, lon_int, alt, vx, vy, vz, afx, afy, afz, yaw, yaw_rate), force_mavlink1=force_mavlink1)

## position_target_global_int_encode
    def position_target_global_int_encode(self, time_boot_ms: int, coordinate_frame: int, type_mask: int, lat_int: int, lon_int: int, alt: float, vx: float, vy: float, vz: float, afx: float, afy: float, afz: float, yaw: float, yaw_rate: float) -> MAVLink_position_target_global_int_message:
        """
        Reports the current commanded vehicle position, velocity, and
        acceleration as specified by the autopilot. This should match
        the commands sent in SET_POSITION_TARGET_GLOBAL_INT if the
        vehicle is being controlled this way.

        time_boot_ms              : Timestamp (time since system boot). The rationale for the timestamp in the setpoint is to allow the system to compensate for the transport delay of the setpoint. This allows the system to compensate processing latency. [ms] (type:uint32_t)
        coordinate_frame          : Valid options are: MAV_FRAME_GLOBAL = 0, MAV_FRAME_GLOBAL_RELATIVE_ALT = 3, MAV_FRAME_GLOBAL_TERRAIN_ALT = 10 (MAV_FRAME_GLOBAL_INT, MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, MAV_FRAME_GLOBAL_TERRAIN_ALT_INT are allowed synonyms, but have been deprecated) (type:uint8_t, values:MAV_FRAME)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint16_t, values:POSITION_TARGET_TYPEMASK)
        lat_int                   : Latitude in WGS84 frame [degE7] (type:int32_t)
        lon_int                   : Longitude in WGS84 frame [degE7] (type:int32_t)
        alt                       : Altitude (MSL, AGL or relative to home altitude, depending on frame) [m] (type:float)
        vx                        : X velocity in NED frame [m/s] (type:float)
        vy                        : Y velocity in NED frame [m/s] (type:float)
        vz                        : Z velocity in NED frame [m/s] (type:float)
        afx                       : X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afy                       : Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afz                       : Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        yaw                       : yaw setpoint [rad] (type:float)
        yaw_rate                  : yaw rate setpoint [rad/s] (type:float)

        """
        return MAVLink_position_target_global_int_message(time_boot_ms, coordinate_frame, type_mask, lat_int, lon_int, alt, vx, vy, vz, afx, afy, afz, yaw, yaw_rate)

## position_target_global_int_send
    def position_target_global_int_send(self, time_boot_ms: int, coordinate_frame: int, type_mask: int, lat_int: int, lon_int: int, alt: float, vx: float, vy: float, vz: float, afx: float, afy: float, afz: float, yaw: float, yaw_rate: float, force_mavlink1: bool = False) -> None:
        """
        Reports the current commanded vehicle position, velocity, and
        acceleration as specified by the autopilot. This should match
        the commands sent in SET_POSITION_TARGET_GLOBAL_INT if the
        vehicle is being controlled this way.

        time_boot_ms              : Timestamp (time since system boot). The rationale for the timestamp in the setpoint is to allow the system to compensate for the transport delay of the setpoint. This allows the system to compensate processing latency. [ms] (type:uint32_t)
        coordinate_frame          : Valid options are: MAV_FRAME_GLOBAL = 0, MAV_FRAME_GLOBAL_RELATIVE_ALT = 3, MAV_FRAME_GLOBAL_TERRAIN_ALT = 10 (MAV_FRAME_GLOBAL_INT, MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, MAV_FRAME_GLOBAL_TERRAIN_ALT_INT are allowed synonyms, but have been deprecated) (type:uint8_t, values:MAV_FRAME)
        type_mask                 : Bitmap to indicate which dimensions should be ignored by the vehicle. (type:uint16_t, values:POSITION_TARGET_TYPEMASK)
        lat_int                   : Latitude in WGS84 frame [degE7] (type:int32_t)
        lon_int                   : Longitude in WGS84 frame [degE7] (type:int32_t)
        alt                       : Altitude (MSL, AGL or relative to home altitude, depending on frame) [m] (type:float)
        vx                        : X velocity in NED frame [m/s] (type:float)
        vy                        : Y velocity in NED frame [m/s] (type:float)
        vz                        : Z velocity in NED frame [m/s] (type:float)
        afx                       : X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afy                       : Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        afz                       : Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N [m/s/s] (type:float)
        yaw                       : yaw setpoint [rad] (type:float)
        yaw_rate                  : yaw rate setpoint [rad/s] (type:float)

        """
        self.send(self.position_target_global_int_encode(time_boot_ms, coordinate_frame, type_mask, lat_int, lon_int, alt, vx, vy, vz, afx, afy, afz, yaw, yaw_rate), force_mavlink1=force_mavlink1)

## local_position_ned_system_global_offset_encode
    def local_position_ned_system_global_offset_encode(self, time_boot_ms: int, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> MAVLink_local_position_ned_system_global_offset_message:
        """
        The offset in X, Y, Z and yaw between the LOCAL_POSITION_NED messages
        of MAV X and the global coordinate frame in NED coordinates.
        Coordinate frame is right-handed, Z-axis down (aeronautical
        frame, NED / north-east-down convention)

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        x                         : X Position [m] (type:float)
        y                         : Y Position [m] (type:float)
        z                         : Z Position [m] (type:float)
        roll                      : Roll [rad] (type:float)
        pitch                     : Pitch [rad] (type:float)
        yaw                       : Yaw [rad] (type:float)

        """
        return MAVLink_local_position_ned_system_global_offset_message(time_boot_ms, x, y, z, roll, pitch, yaw)

## local_position_ned_system_global_offset_send
    def local_position_ned_system_global_offset_send(self, time_boot_ms: int, x: float, y: float, z: float, roll: float, pitch: float, yaw: float, force_mavlink1: bool = False) -> None:
        """
        The offset in X, Y, Z and yaw between the LOCAL_POSITION_NED messages
        of MAV X and the global coordinate frame in NED coordinates.
        Coordinate frame is right-handed, Z-axis down (aeronautical
        frame, NED / north-east-down convention)

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        x                         : X Position [m] (type:float)
        y                         : Y Position [m] (type:float)
        z                         : Z Position [m] (type:float)
        roll                      : Roll [rad] (type:float)
        pitch                     : Pitch [rad] (type:float)
        yaw                       : Yaw [rad] (type:float)

        """
        self.send(self.local_position_ned_system_global_offset_encode(time_boot_ms, x, y, z, roll, pitch, yaw), force_mavlink1=force_mavlink1)

## hil_state_encode
    def hil_state_encode(self, time_usec: int, roll: float, pitch: float, yaw: float, rollspeed: float, pitchspeed: float, yawspeed: float, lat: int, lon: int, alt: int, vx: int, vy: int, vz: int, xacc: int, yacc: int, zacc: int) -> MAVLink_hil_state_message:
        """
        Sent from simulation to autopilot. This packet is useful for high
        throughput applications such as hardware in the loop
        simulations.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        rollspeed                 : Body frame roll / phi angular speed [rad/s] (type:float)
        pitchspeed                : Body frame pitch / theta angular speed [rad/s] (type:float)
        yawspeed                  : Body frame yaw / psi angular speed [rad/s] (type:float)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        alt                       : Altitude [mm] (type:int32_t)
        vx                        : Ground X Speed (Latitude) [cm/s] (type:int16_t)
        vy                        : Ground Y Speed (Longitude) [cm/s] (type:int16_t)
        vz                        : Ground Z Speed (Altitude) [cm/s] (type:int16_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)

        """
        return MAVLink_hil_state_message(time_usec, roll, pitch, yaw, rollspeed, pitchspeed, yawspeed, lat, lon, alt, vx, vy, vz, xacc, yacc, zacc)

## hil_state_send
    def hil_state_send(self, time_usec: int, roll: float, pitch: float, yaw: float, rollspeed: float, pitchspeed: float, yawspeed: float, lat: int, lon: int, alt: int, vx: int, vy: int, vz: int, xacc: int, yacc: int, zacc: int, force_mavlink1: bool = False) -> None:
        """
        Sent from simulation to autopilot. This packet is useful for high
        throughput applications such as hardware in the loop
        simulations.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        rollspeed                 : Body frame roll / phi angular speed [rad/s] (type:float)
        pitchspeed                : Body frame pitch / theta angular speed [rad/s] (type:float)
        yawspeed                  : Body frame yaw / psi angular speed [rad/s] (type:float)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        alt                       : Altitude [mm] (type:int32_t)
        vx                        : Ground X Speed (Latitude) [cm/s] (type:int16_t)
        vy                        : Ground Y Speed (Longitude) [cm/s] (type:int16_t)
        vz                        : Ground Z Speed (Altitude) [cm/s] (type:int16_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)

        """
        self.send(self.hil_state_encode(time_usec, roll, pitch, yaw, rollspeed, pitchspeed, yawspeed, lat, lon, alt, vx, vy, vz, xacc, yacc, zacc), force_mavlink1=force_mavlink1)

## hil_controls_encode
    def hil_controls_encode(self, time_usec: int, roll_ailerons: float, pitch_elevator: float, yaw_rudder: float, throttle: float, aux1: float, aux2: float, aux3: float, aux4: float, mode: int, nav_mode: int) -> MAVLink_hil_controls_message:
        """
        Sent from autopilot to simulation. Hardware in the loop control
        outputs

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        roll_ailerons             : Control output -1 .. 1 (type:float)
        pitch_elevator            : Control output -1 .. 1 (type:float)
        yaw_rudder                : Control output -1 .. 1 (type:float)
        throttle                  : Throttle 0 .. 1 (type:float)
        aux1                      : Aux 1, -1 .. 1 (type:float)
        aux2                      : Aux 2, -1 .. 1 (type:float)
        aux3                      : Aux 3, -1 .. 1 (type:float)
        aux4                      : Aux 4, -1 .. 1 (type:float)
        mode                      : System mode. (type:uint8_t, values:MAV_MODE)
        nav_mode                  : Navigation mode (MAV_NAV_MODE) (type:uint8_t)

        """
        return MAVLink_hil_controls_message(time_usec, roll_ailerons, pitch_elevator, yaw_rudder, throttle, aux1, aux2, aux3, aux4, mode, nav_mode)

## hil_controls_send
    def hil_controls_send(self, time_usec: int, roll_ailerons: float, pitch_elevator: float, yaw_rudder: float, throttle: float, aux1: float, aux2: float, aux3: float, aux4: float, mode: int, nav_mode: int, force_mavlink1: bool = False) -> None:
        """
        Sent from autopilot to simulation. Hardware in the loop control
        outputs

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        roll_ailerons             : Control output -1 .. 1 (type:float)
        pitch_elevator            : Control output -1 .. 1 (type:float)
        yaw_rudder                : Control output -1 .. 1 (type:float)
        throttle                  : Throttle 0 .. 1 (type:float)
        aux1                      : Aux 1, -1 .. 1 (type:float)
        aux2                      : Aux 2, -1 .. 1 (type:float)
        aux3                      : Aux 3, -1 .. 1 (type:float)
        aux4                      : Aux 4, -1 .. 1 (type:float)
        mode                      : System mode. (type:uint8_t, values:MAV_MODE)
        nav_mode                  : Navigation mode (MAV_NAV_MODE) (type:uint8_t)

        """
        self.send(self.hil_controls_encode(time_usec, roll_ailerons, pitch_elevator, yaw_rudder, throttle, aux1, aux2, aux3, aux4, mode, nav_mode), force_mavlink1=force_mavlink1)

## hil_rc_inputs_raw_encode
    def hil_rc_inputs_raw_encode(self, time_usec: int, chan1_raw: int, chan2_raw: int, chan3_raw: int, chan4_raw: int, chan5_raw: int, chan6_raw: int, chan7_raw: int, chan8_raw: int, chan9_raw: int, chan10_raw: int, chan11_raw: int, chan12_raw: int, rssi: int) -> MAVLink_hil_rc_inputs_raw_message:
        """
        Sent from simulation to autopilot. The RAW values of the RC channels
        received. The standard PPM modulation is as follows: 1000
        microseconds: 0%, 2000 microseconds: 100%. Individual
        receivers/transmitters might violate this specification.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        chan1_raw                 : RC channel 1 value [us] (type:uint16_t)
        chan2_raw                 : RC channel 2 value [us] (type:uint16_t)
        chan3_raw                 : RC channel 3 value [us] (type:uint16_t)
        chan4_raw                 : RC channel 4 value [us] (type:uint16_t)
        chan5_raw                 : RC channel 5 value [us] (type:uint16_t)
        chan6_raw                 : RC channel 6 value [us] (type:uint16_t)
        chan7_raw                 : RC channel 7 value [us] (type:uint16_t)
        chan8_raw                 : RC channel 8 value [us] (type:uint16_t)
        chan9_raw                 : RC channel 9 value [us] (type:uint16_t)
        chan10_raw                : RC channel 10 value [us] (type:uint16_t)
        chan11_raw                : RC channel 11 value [us] (type:uint16_t)
        chan12_raw                : RC channel 12 value [us] (type:uint16_t)
        rssi                      : Receive signal strength indicator in device-dependent units/scale. Values: [0-254], UINT8_MAX: invalid/unknown. (type:uint8_t)

        """
        return MAVLink_hil_rc_inputs_raw_message(time_usec, chan1_raw, chan2_raw, chan3_raw, chan4_raw, chan5_raw, chan6_raw, chan7_raw, chan8_raw, chan9_raw, chan10_raw, chan11_raw, chan12_raw, rssi)

## hil_rc_inputs_raw_send
    def hil_rc_inputs_raw_send(self, time_usec: int, chan1_raw: int, chan2_raw: int, chan3_raw: int, chan4_raw: int, chan5_raw: int, chan6_raw: int, chan7_raw: int, chan8_raw: int, chan9_raw: int, chan10_raw: int, chan11_raw: int, chan12_raw: int, rssi: int, force_mavlink1: bool = False) -> None:
        """
        Sent from simulation to autopilot. The RAW values of the RC channels
        received. The standard PPM modulation is as follows: 1000
        microseconds: 0%, 2000 microseconds: 100%. Individual
        receivers/transmitters might violate this specification.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        chan1_raw                 : RC channel 1 value [us] (type:uint16_t)
        chan2_raw                 : RC channel 2 value [us] (type:uint16_t)
        chan3_raw                 : RC channel 3 value [us] (type:uint16_t)
        chan4_raw                 : RC channel 4 value [us] (type:uint16_t)
        chan5_raw                 : RC channel 5 value [us] (type:uint16_t)
        chan6_raw                 : RC channel 6 value [us] (type:uint16_t)
        chan7_raw                 : RC channel 7 value [us] (type:uint16_t)
        chan8_raw                 : RC channel 8 value [us] (type:uint16_t)
        chan9_raw                 : RC channel 9 value [us] (type:uint16_t)
        chan10_raw                : RC channel 10 value [us] (type:uint16_t)
        chan11_raw                : RC channel 11 value [us] (type:uint16_t)
        chan12_raw                : RC channel 12 value [us] (type:uint16_t)
        rssi                      : Receive signal strength indicator in device-dependent units/scale. Values: [0-254], UINT8_MAX: invalid/unknown. (type:uint8_t)

        """
        self.send(self.hil_rc_inputs_raw_encode(time_usec, chan1_raw, chan2_raw, chan3_raw, chan4_raw, chan5_raw, chan6_raw, chan7_raw, chan8_raw, chan9_raw, chan10_raw, chan11_raw, chan12_raw, rssi), force_mavlink1=force_mavlink1)

## hil_actuator_controls_encode
    def hil_actuator_controls_encode(self, time_usec: int, controls: Sequence[float], mode: int, flags: int) -> MAVLink_hil_actuator_controls_message:
        """
        Sent from autopilot to simulation. Hardware in the loop control
        outputs (replacement for HIL_CONTROLS)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        controls                  : Control outputs -1 .. 1. Channel assignment depends on the simulated hardware. (type:float)
        mode                      : System mode. Includes arming state. (type:uint8_t, values:MAV_MODE_FLAG)
        flags                     : Flags as bitfield, 1: indicate simulation using lockstep. (type:uint64_t)

        """
        return MAVLink_hil_actuator_controls_message(time_usec, controls, mode, flags)

## hil_actuator_controls_send
    def hil_actuator_controls_send(self, time_usec: int, controls: Sequence[float], mode: int, flags: int, force_mavlink1: bool = False) -> None:
        """
        Sent from autopilot to simulation. Hardware in the loop control
        outputs (replacement for HIL_CONTROLS)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        controls                  : Control outputs -1 .. 1. Channel assignment depends on the simulated hardware. (type:float)
        mode                      : System mode. Includes arming state. (type:uint8_t, values:MAV_MODE_FLAG)
        flags                     : Flags as bitfield, 1: indicate simulation using lockstep. (type:uint64_t)

        """
        self.send(self.hil_actuator_controls_encode(time_usec, controls, mode, flags), force_mavlink1=force_mavlink1)

## optical_flow_encode
    def optical_flow_encode(self, time_usec: int, sensor_id: int, flow_x: int, flow_y: int, flow_comp_m_x: float, flow_comp_m_y: float, quality: int, ground_distance: float, flow_rate_x: float = 0, flow_rate_y: float = 0) -> MAVLink_optical_flow_message:
        """
        Optical flow from a flow sensor (e.g. optical mouse sensor)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        sensor_id                 : Sensor ID (type:uint8_t)
        flow_x                    : Flow rate around X-axis (deprecated; use flow_rate_x) [rad/s] (type:int16_t)
        flow_y                    : Flow rate around Y-axis (deprecated; use flow_rate_y) [rad/s] (type:int16_t)
        flow_comp_m_x             : Flow in x-sensor direction, angular-speed compensated [m/s] (type:float)
        flow_comp_m_y             : Flow in y-sensor direction, angular-speed compensated [m/s] (type:float)
        quality                   : Optical flow quality / confidence. 0: bad, 255: maximum quality (type:uint8_t)
        ground_distance           : Ground distance. Positive value: distance known. Negative value: Unknown distance [m] (type:float)
        flow_rate_x               : Flow rate about X axis [rad/s] (type:float)
        flow_rate_y               : Flow rate about Y axis [rad/s] (type:float)

        """
        return MAVLink_optical_flow_message(time_usec, sensor_id, flow_x, flow_y, flow_comp_m_x, flow_comp_m_y, quality, ground_distance, flow_rate_x, flow_rate_y)

## optical_flow_send
    def optical_flow_send(self, time_usec: int, sensor_id: int, flow_x: int, flow_y: int, flow_comp_m_x: float, flow_comp_m_y: float, quality: int, ground_distance: float, flow_rate_x: float = 0, flow_rate_y: float = 0, force_mavlink1: bool = False) -> None:
        """
        Optical flow from a flow sensor (e.g. optical mouse sensor)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        sensor_id                 : Sensor ID (type:uint8_t)
        flow_x                    : Flow rate around X-axis (deprecated; use flow_rate_x) [rad/s] (type:int16_t)
        flow_y                    : Flow rate around Y-axis (deprecated; use flow_rate_y) [rad/s] (type:int16_t)
        flow_comp_m_x             : Flow in x-sensor direction, angular-speed compensated [m/s] (type:float)
        flow_comp_m_y             : Flow in y-sensor direction, angular-speed compensated [m/s] (type:float)
        quality                   : Optical flow quality / confidence. 0: bad, 255: maximum quality (type:uint8_t)
        ground_distance           : Ground distance. Positive value: distance known. Negative value: Unknown distance [m] (type:float)
        flow_rate_x               : Flow rate about X axis [rad/s] (type:float)
        flow_rate_y               : Flow rate about Y axis [rad/s] (type:float)

        """
        self.send(self.optical_flow_encode(time_usec, sensor_id, flow_x, flow_y, flow_comp_m_x, flow_comp_m_y, quality, ground_distance, flow_rate_x, flow_rate_y), force_mavlink1=force_mavlink1)

## global_vision_position_estimate_encode
    def global_vision_position_estimate_encode(self, usec: int, x: float, y: float, z: float, roll: float, pitch: float, yaw: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), reset_counter: int = 0) -> MAVLink_global_vision_position_estimate_message:
        """
        Global position/attitude estimate from a vision source.

        usec                      : Timestamp (UNIX time or since system boot) [us] (type:uint64_t)
        x                         : Global X position [m] (type:float)
        y                         : Global Y position [m] (type:float)
        z                         : Global Z position [m] (type:float)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        covariance                : Row-major representation of pose 6x6 cross-covariance matrix upper right triangle (states: x_global, y_global, z_global, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        reset_counter             : Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. (type:uint8_t)

        """
        return MAVLink_global_vision_position_estimate_message(usec, x, y, z, roll, pitch, yaw, covariance, reset_counter)

## global_vision_position_estimate_send
    def global_vision_position_estimate_send(self, usec: int, x: float, y: float, z: float, roll: float, pitch: float, yaw: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), reset_counter: int = 0, force_mavlink1: bool = False) -> None:
        """
        Global position/attitude estimate from a vision source.

        usec                      : Timestamp (UNIX time or since system boot) [us] (type:uint64_t)
        x                         : Global X position [m] (type:float)
        y                         : Global Y position [m] (type:float)
        z                         : Global Z position [m] (type:float)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        covariance                : Row-major representation of pose 6x6 cross-covariance matrix upper right triangle (states: x_global, y_global, z_global, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        reset_counter             : Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. (type:uint8_t)

        """
        self.send(self.global_vision_position_estimate_encode(usec, x, y, z, roll, pitch, yaw, covariance, reset_counter), force_mavlink1=force_mavlink1)

## vision_position_estimate_encode
    def vision_position_estimate_encode(self, usec: int, x: float, y: float, z: float, roll: float, pitch: float, yaw: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), reset_counter: int = 0) -> MAVLink_vision_position_estimate_message:
        """
        Local position/attitude estimate from a vision source.

        usec                      : Timestamp (UNIX time or time since system boot) [us] (type:uint64_t)
        x                         : Local X position [m] (type:float)
        y                         : Local Y position [m] (type:float)
        z                         : Local Z position [m] (type:float)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        covariance                : Row-major representation of pose 6x6 cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        reset_counter             : Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. (type:uint8_t)

        """
        return MAVLink_vision_position_estimate_message(usec, x, y, z, roll, pitch, yaw, covariance, reset_counter)

## vision_position_estimate_send
    def vision_position_estimate_send(self, usec: int, x: float, y: float, z: float, roll: float, pitch: float, yaw: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), reset_counter: int = 0, force_mavlink1: bool = False) -> None:
        """
        Local position/attitude estimate from a vision source.

        usec                      : Timestamp (UNIX time or time since system boot) [us] (type:uint64_t)
        x                         : Local X position [m] (type:float)
        y                         : Local Y position [m] (type:float)
        z                         : Local Z position [m] (type:float)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        covariance                : Row-major representation of pose 6x6 cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        reset_counter             : Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. (type:uint8_t)

        """
        self.send(self.vision_position_estimate_encode(usec, x, y, z, roll, pitch, yaw, covariance, reset_counter), force_mavlink1=force_mavlink1)

## vision_speed_estimate_encode
    def vision_speed_estimate_encode(self, usec: int, x: float, y: float, z: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0), reset_counter: int = 0) -> MAVLink_vision_speed_estimate_message:
        """
        Speed estimate from a vision source.

        usec                      : Timestamp (UNIX time or time since system boot) [us] (type:uint64_t)
        x                         : Global X speed [m/s] (type:float)
        y                         : Global Y speed [m/s] (type:float)
        z                         : Global Z speed [m/s] (type:float)
        covariance                : Row-major representation of 3x3 linear velocity covariance matrix (states: vx, vy, vz; 1st three entries - 1st row, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        reset_counter             : Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. (type:uint8_t)

        """
        return MAVLink_vision_speed_estimate_message(usec, x, y, z, covariance, reset_counter)

## vision_speed_estimate_send
    def vision_speed_estimate_send(self, usec: int, x: float, y: float, z: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0), reset_counter: int = 0, force_mavlink1: bool = False) -> None:
        """
        Speed estimate from a vision source.

        usec                      : Timestamp (UNIX time or time since system boot) [us] (type:uint64_t)
        x                         : Global X speed [m/s] (type:float)
        y                         : Global Y speed [m/s] (type:float)
        z                         : Global Z speed [m/s] (type:float)
        covariance                : Row-major representation of 3x3 linear velocity covariance matrix (states: vx, vy, vz; 1st three entries - 1st row, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        reset_counter             : Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. (type:uint8_t)

        """
        self.send(self.vision_speed_estimate_encode(usec, x, y, z, covariance, reset_counter), force_mavlink1=force_mavlink1)

## vicon_position_estimate_encode
    def vicon_position_estimate_encode(self, usec: int, x: float, y: float, z: float, roll: float, pitch: float, yaw: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)) -> MAVLink_vicon_position_estimate_message:
        """
        Global position estimate from a Vicon motion system source.

        usec                      : Timestamp (UNIX time or time since system boot) [us] (type:uint64_t)
        x                         : Global X position [m] (type:float)
        y                         : Global Y position [m] (type:float)
        z                         : Global Z position [m] (type:float)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        covariance                : Row-major representation of 6x6 pose cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        return MAVLink_vicon_position_estimate_message(usec, x, y, z, roll, pitch, yaw, covariance)

## vicon_position_estimate_send
    def vicon_position_estimate_send(self, usec: int, x: float, y: float, z: float, roll: float, pitch: float, yaw: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), force_mavlink1: bool = False) -> None:
        """
        Global position estimate from a Vicon motion system source.

        usec                      : Timestamp (UNIX time or time since system boot) [us] (type:uint64_t)
        x                         : Global X position [m] (type:float)
        y                         : Global Y position [m] (type:float)
        z                         : Global Z position [m] (type:float)
        roll                      : Roll angle [rad] (type:float)
        pitch                     : Pitch angle [rad] (type:float)
        yaw                       : Yaw angle [rad] (type:float)
        covariance                : Row-major representation of 6x6 pose cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        self.send(self.vicon_position_estimate_encode(usec, x, y, z, roll, pitch, yaw, covariance), force_mavlink1=force_mavlink1)

## highres_imu_encode
    def highres_imu_encode(self, time_usec: int, xacc: float, yacc: float, zacc: float, xgyro: float, ygyro: float, zgyro: float, xmag: float, ymag: float, zmag: float, abs_pressure: float, diff_pressure: float, pressure_alt: float, temperature: float, fields_updated: int, id: int = 0) -> MAVLink_highres_imu_message:
        """
        The IMU readings in SI units in NED body frame

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        xacc                      : X acceleration [m/s/s] (type:float)
        yacc                      : Y acceleration [m/s/s] (type:float)
        zacc                      : Z acceleration [m/s/s] (type:float)
        xgyro                     : Angular speed around X axis [rad/s] (type:float)
        ygyro                     : Angular speed around Y axis [rad/s] (type:float)
        zgyro                     : Angular speed around Z axis [rad/s] (type:float)
        xmag                      : X Magnetic field [gauss] (type:float)
        ymag                      : Y Magnetic field [gauss] (type:float)
        zmag                      : Z Magnetic field [gauss] (type:float)
        abs_pressure              : Absolute pressure [hPa] (type:float)
        diff_pressure             : Differential pressure [hPa] (type:float)
        pressure_alt              : Altitude calculated from pressure (type:float)
        temperature               : Temperature [degC] (type:float)
        fields_updated            : Bitmap for fields that have updated since last message, bit 0 = xacc, bit 12: temperature (type:uint16_t)
        id                        : Id. Ids are numbered from 0 and map to IMUs numbered from 1 (e.g. IMU1 will have a message with id=0) (type:uint8_t)

        """
        return MAVLink_highres_imu_message(time_usec, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, abs_pressure, diff_pressure, pressure_alt, temperature, fields_updated, id)

## highres_imu_send
    def highres_imu_send(self, time_usec: int, xacc: float, yacc: float, zacc: float, xgyro: float, ygyro: float, zgyro: float, xmag: float, ymag: float, zmag: float, abs_pressure: float, diff_pressure: float, pressure_alt: float, temperature: float, fields_updated: int, id: int = 0, force_mavlink1: bool = False) -> None:
        """
        The IMU readings in SI units in NED body frame

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        xacc                      : X acceleration [m/s/s] (type:float)
        yacc                      : Y acceleration [m/s/s] (type:float)
        zacc                      : Z acceleration [m/s/s] (type:float)
        xgyro                     : Angular speed around X axis [rad/s] (type:float)
        ygyro                     : Angular speed around Y axis [rad/s] (type:float)
        zgyro                     : Angular speed around Z axis [rad/s] (type:float)
        xmag                      : X Magnetic field [gauss] (type:float)
        ymag                      : Y Magnetic field [gauss] (type:float)
        zmag                      : Z Magnetic field [gauss] (type:float)
        abs_pressure              : Absolute pressure [hPa] (type:float)
        diff_pressure             : Differential pressure [hPa] (type:float)
        pressure_alt              : Altitude calculated from pressure (type:float)
        temperature               : Temperature [degC] (type:float)
        fields_updated            : Bitmap for fields that have updated since last message, bit 0 = xacc, bit 12: temperature (type:uint16_t)
        id                        : Id. Ids are numbered from 0 and map to IMUs numbered from 1 (e.g. IMU1 will have a message with id=0) (type:uint8_t)

        """
        self.send(self.highres_imu_encode(time_usec, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, abs_pressure, diff_pressure, pressure_alt, temperature, fields_updated, id), force_mavlink1=force_mavlink1)

## optical_flow_rad_encode
    def optical_flow_rad_encode(self, time_usec: int, sensor_id: int, integration_time_us: int, integrated_x: float, integrated_y: float, integrated_xgyro: float, integrated_ygyro: float, integrated_zgyro: float, temperature: int, quality: int, time_delta_distance_us: int, distance: float) -> MAVLink_optical_flow_rad_message:
        """
        Optical flow from an angular rate flow sensor (e.g. PX4FLOW or mouse
        sensor)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        sensor_id                 : Sensor ID (type:uint8_t)
        integration_time_us        : Integration time. Divide integrated_x and integrated_y by the integration time to obtain average flow. The integration time also indicates the. [us] (type:uint32_t)
        integrated_x              : Flow around X axis (Sensor RH rotation about the X axis induces a positive flow. Sensor linear motion along the positive Y axis induces a negative flow.) [rad] (type:float)
        integrated_y              : Flow around Y axis (Sensor RH rotation about the Y axis induces a positive flow. Sensor linear motion along the positive X axis induces a positive flow.) [rad] (type:float)
        integrated_xgyro          : RH rotation around X axis [rad] (type:float)
        integrated_ygyro          : RH rotation around Y axis [rad] (type:float)
        integrated_zgyro          : RH rotation around Z axis [rad] (type:float)
        temperature               : Temperature [cdegC] (type:int16_t)
        quality                   : Optical flow quality / confidence. 0: no valid flow, 255: maximum quality (type:uint8_t)
        time_delta_distance_us        : Time since the distance was sampled. [us] (type:uint32_t)
        distance                  : Distance to the center of the flow field. Positive value (including zero): distance known. Negative value: Unknown distance. [m] (type:float)

        """
        return MAVLink_optical_flow_rad_message(time_usec, sensor_id, integration_time_us, integrated_x, integrated_y, integrated_xgyro, integrated_ygyro, integrated_zgyro, temperature, quality, time_delta_distance_us, distance)

## optical_flow_rad_send
    def optical_flow_rad_send(self, time_usec: int, sensor_id: int, integration_time_us: int, integrated_x: float, integrated_y: float, integrated_xgyro: float, integrated_ygyro: float, integrated_zgyro: float, temperature: int, quality: int, time_delta_distance_us: int, distance: float, force_mavlink1: bool = False) -> None:
        """
        Optical flow from an angular rate flow sensor (e.g. PX4FLOW or mouse
        sensor)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        sensor_id                 : Sensor ID (type:uint8_t)
        integration_time_us        : Integration time. Divide integrated_x and integrated_y by the integration time to obtain average flow. The integration time also indicates the. [us] (type:uint32_t)
        integrated_x              : Flow around X axis (Sensor RH rotation about the X axis induces a positive flow. Sensor linear motion along the positive Y axis induces a negative flow.) [rad] (type:float)
        integrated_y              : Flow around Y axis (Sensor RH rotation about the Y axis induces a positive flow. Sensor linear motion along the positive X axis induces a positive flow.) [rad] (type:float)
        integrated_xgyro          : RH rotation around X axis [rad] (type:float)
        integrated_ygyro          : RH rotation around Y axis [rad] (type:float)
        integrated_zgyro          : RH rotation around Z axis [rad] (type:float)
        temperature               : Temperature [cdegC] (type:int16_t)
        quality                   : Optical flow quality / confidence. 0: no valid flow, 255: maximum quality (type:uint8_t)
        time_delta_distance_us        : Time since the distance was sampled. [us] (type:uint32_t)
        distance                  : Distance to the center of the flow field. Positive value (including zero): distance known. Negative value: Unknown distance. [m] (type:float)

        """
        self.send(self.optical_flow_rad_encode(time_usec, sensor_id, integration_time_us, integrated_x, integrated_y, integrated_xgyro, integrated_ygyro, integrated_zgyro, temperature, quality, time_delta_distance_us, distance), force_mavlink1=force_mavlink1)

## hil_sensor_encode
    def hil_sensor_encode(self, time_usec: int, xacc: float, yacc: float, zacc: float, xgyro: float, ygyro: float, zgyro: float, xmag: float, ymag: float, zmag: float, abs_pressure: float, diff_pressure: float, pressure_alt: float, temperature: float, fields_updated: int, id: int = 0) -> MAVLink_hil_sensor_message:
        """
        The IMU readings in SI units in NED body frame

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        xacc                      : X acceleration [m/s/s] (type:float)
        yacc                      : Y acceleration [m/s/s] (type:float)
        zacc                      : Z acceleration [m/s/s] (type:float)
        xgyro                     : Angular speed around X axis in body frame [rad/s] (type:float)
        ygyro                     : Angular speed around Y axis in body frame [rad/s] (type:float)
        zgyro                     : Angular speed around Z axis in body frame [rad/s] (type:float)
        xmag                      : X Magnetic field [gauss] (type:float)
        ymag                      : Y Magnetic field [gauss] (type:float)
        zmag                      : Z Magnetic field [gauss] (type:float)
        abs_pressure              : Absolute pressure [hPa] (type:float)
        diff_pressure             : Differential pressure (airspeed) [hPa] (type:float)
        pressure_alt              : Altitude calculated from pressure (type:float)
        temperature               : Temperature [degC] (type:float)
        fields_updated            : Bitmap for fields that have updated since last message, bit 0 = xacc, bit 12: temperature, bit 31: full reset of attitude/position/velocities/etc was performed in sim. (type:uint32_t)
        id                        : Sensor ID (zero indexed). Used for multiple sensor inputs (type:uint8_t)

        """
        return MAVLink_hil_sensor_message(time_usec, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, abs_pressure, diff_pressure, pressure_alt, temperature, fields_updated, id)

## hil_sensor_send
    def hil_sensor_send(self, time_usec: int, xacc: float, yacc: float, zacc: float, xgyro: float, ygyro: float, zgyro: float, xmag: float, ymag: float, zmag: float, abs_pressure: float, diff_pressure: float, pressure_alt: float, temperature: float, fields_updated: int, id: int = 0, force_mavlink1: bool = False) -> None:
        """
        The IMU readings in SI units in NED body frame

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        xacc                      : X acceleration [m/s/s] (type:float)
        yacc                      : Y acceleration [m/s/s] (type:float)
        zacc                      : Z acceleration [m/s/s] (type:float)
        xgyro                     : Angular speed around X axis in body frame [rad/s] (type:float)
        ygyro                     : Angular speed around Y axis in body frame [rad/s] (type:float)
        zgyro                     : Angular speed around Z axis in body frame [rad/s] (type:float)
        xmag                      : X Magnetic field [gauss] (type:float)
        ymag                      : Y Magnetic field [gauss] (type:float)
        zmag                      : Z Magnetic field [gauss] (type:float)
        abs_pressure              : Absolute pressure [hPa] (type:float)
        diff_pressure             : Differential pressure (airspeed) [hPa] (type:float)
        pressure_alt              : Altitude calculated from pressure (type:float)
        temperature               : Temperature [degC] (type:float)
        fields_updated            : Bitmap for fields that have updated since last message, bit 0 = xacc, bit 12: temperature, bit 31: full reset of attitude/position/velocities/etc was performed in sim. (type:uint32_t)
        id                        : Sensor ID (zero indexed). Used for multiple sensor inputs (type:uint8_t)

        """
        self.send(self.hil_sensor_encode(time_usec, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, abs_pressure, diff_pressure, pressure_alt, temperature, fields_updated, id), force_mavlink1=force_mavlink1)

## sim_state_encode
    def sim_state_encode(self, q1: float, q2: float, q3: float, q4: float, roll: float, pitch: float, yaw: float, xacc: float, yacc: float, zacc: float, xgyro: float, ygyro: float, zgyro: float, lat: float, lon: float, alt: float, std_dev_horz: float, std_dev_vert: float, vn: float, ve: float, vd: float, lat_int: int = 0, lon_int: int = 0) -> MAVLink_sim_state_message:
        """
        Status of simulation environment, if used

        q1                        : True attitude quaternion component 1, w (1 in null-rotation) (type:float)
        q2                        : True attitude quaternion component 2, x (0 in null-rotation) (type:float)
        q3                        : True attitude quaternion component 3, y (0 in null-rotation) (type:float)
        q4                        : True attitude quaternion component 4, z (0 in null-rotation) (type:float)
        roll                      : Attitude roll expressed as Euler angles, not recommended except for human-readable outputs (type:float)
        pitch                     : Attitude pitch expressed as Euler angles, not recommended except for human-readable outputs (type:float)
        yaw                       : Attitude yaw expressed as Euler angles, not recommended except for human-readable outputs (type:float)
        xacc                      : X acceleration [m/s/s] (type:float)
        yacc                      : Y acceleration [m/s/s] (type:float)
        zacc                      : Z acceleration [m/s/s] (type:float)
        xgyro                     : Angular speed around X axis [rad/s] (type:float)
        ygyro                     : Angular speed around Y axis [rad/s] (type:float)
        zgyro                     : Angular speed around Z axis [rad/s] (type:float)
        lat                       : Latitude [deg] (type:float)
        lon                       : Longitude [deg] (type:float)
        alt                       : Altitude [m] (type:float)
        std_dev_horz              : Horizontal position standard deviation (type:float)
        std_dev_vert              : Vertical position standard deviation (type:float)
        vn                        : True velocity in north direction in earth-fixed NED frame [m/s] (type:float)
        ve                        : True velocity in east direction in earth-fixed NED frame [m/s] (type:float)
        vd                        : True velocity in down direction in earth-fixed NED frame [m/s] (type:float)
        lat_int                   : Latitude (higher precision). If 0, recipients should use the lat field value (otherwise this field is preferred). [degE7] (type:int32_t)
        lon_int                   : Longitude (higher precision). If 0, recipients should use the lon field value (otherwise this field is preferred). [degE7] (type:int32_t)

        """
        return MAVLink_sim_state_message(q1, q2, q3, q4, roll, pitch, yaw, xacc, yacc, zacc, xgyro, ygyro, zgyro, lat, lon, alt, std_dev_horz, std_dev_vert, vn, ve, vd, lat_int, lon_int)

## sim_state_send
    def sim_state_send(self, q1: float, q2: float, q3: float, q4: float, roll: float, pitch: float, yaw: float, xacc: float, yacc: float, zacc: float, xgyro: float, ygyro: float, zgyro: float, lat: float, lon: float, alt: float, std_dev_horz: float, std_dev_vert: float, vn: float, ve: float, vd: float, lat_int: int = 0, lon_int: int = 0, force_mavlink1: bool = False) -> None:
        """
        Status of simulation environment, if used

        q1                        : True attitude quaternion component 1, w (1 in null-rotation) (type:float)
        q2                        : True attitude quaternion component 2, x (0 in null-rotation) (type:float)
        q3                        : True attitude quaternion component 3, y (0 in null-rotation) (type:float)
        q4                        : True attitude quaternion component 4, z (0 in null-rotation) (type:float)
        roll                      : Attitude roll expressed as Euler angles, not recommended except for human-readable outputs (type:float)
        pitch                     : Attitude pitch expressed as Euler angles, not recommended except for human-readable outputs (type:float)
        yaw                       : Attitude yaw expressed as Euler angles, not recommended except for human-readable outputs (type:float)
        xacc                      : X acceleration [m/s/s] (type:float)
        yacc                      : Y acceleration [m/s/s] (type:float)
        zacc                      : Z acceleration [m/s/s] (type:float)
        xgyro                     : Angular speed around X axis [rad/s] (type:float)
        ygyro                     : Angular speed around Y axis [rad/s] (type:float)
        zgyro                     : Angular speed around Z axis [rad/s] (type:float)
        lat                       : Latitude [deg] (type:float)
        lon                       : Longitude [deg] (type:float)
        alt                       : Altitude [m] (type:float)
        std_dev_horz              : Horizontal position standard deviation (type:float)
        std_dev_vert              : Vertical position standard deviation (type:float)
        vn                        : True velocity in north direction in earth-fixed NED frame [m/s] (type:float)
        ve                        : True velocity in east direction in earth-fixed NED frame [m/s] (type:float)
        vd                        : True velocity in down direction in earth-fixed NED frame [m/s] (type:float)
        lat_int                   : Latitude (higher precision). If 0, recipients should use the lat field value (otherwise this field is preferred). [degE7] (type:int32_t)
        lon_int                   : Longitude (higher precision). If 0, recipients should use the lon field value (otherwise this field is preferred). [degE7] (type:int32_t)

        """
        self.send(self.sim_state_encode(q1, q2, q3, q4, roll, pitch, yaw, xacc, yacc, zacc, xgyro, ygyro, zgyro, lat, lon, alt, std_dev_horz, std_dev_vert, vn, ve, vd, lat_int, lon_int), force_mavlink1=force_mavlink1)

## radio_status_encode
    def radio_status_encode(self, rssi: int, remrssi: int, txbuf: int, noise: int, remnoise: int, rxerrors: int, fixed: int) -> MAVLink_radio_status_message:
        """
        Status generated by radio and injected into MAVLink stream.

        rssi                      : Local (message sender) received signal strength indication in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)
        remrssi                   : Remote (message receiver) signal strength indication in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)
        txbuf                     : Remaining free transmitter buffer space. [%] (type:uint8_t)
        noise                     : Local background noise level. These are device dependent RSSI values (scale as approx 2x dB on SiK radios). Values: [0-254], 255: invalid/unknown. (type:uint8_t)
        remnoise                  : Remote background noise level. These are device dependent RSSI values (scale as approx 2x dB on SiK radios). Values: [0-254], 255: invalid/unknown. (type:uint8_t)
        rxerrors                  : Count of radio packet receive errors (since boot). (type:uint16_t)
        fixed                     : Count of error corrected radio packets (since boot). (type:uint16_t)

        """
        return MAVLink_radio_status_message(rssi, remrssi, txbuf, noise, remnoise, rxerrors, fixed)

## radio_status_send
    def radio_status_send(self, rssi: int, remrssi: int, txbuf: int, noise: int, remnoise: int, rxerrors: int, fixed: int, force_mavlink1: bool = False) -> None:
        """
        Status generated by radio and injected into MAVLink stream.

        rssi                      : Local (message sender) received signal strength indication in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)
        remrssi                   : Remote (message receiver) signal strength indication in device-dependent units/scale. Values: [0-254], 255: invalid/unknown. (type:uint8_t)
        txbuf                     : Remaining free transmitter buffer space. [%] (type:uint8_t)
        noise                     : Local background noise level. These are device dependent RSSI values (scale as approx 2x dB on SiK radios). Values: [0-254], 255: invalid/unknown. (type:uint8_t)
        remnoise                  : Remote background noise level. These are device dependent RSSI values (scale as approx 2x dB on SiK radios). Values: [0-254], 255: invalid/unknown. (type:uint8_t)
        rxerrors                  : Count of radio packet receive errors (since boot). (type:uint16_t)
        fixed                     : Count of error corrected radio packets (since boot). (type:uint16_t)

        """
        self.send(self.radio_status_encode(rssi, remrssi, txbuf, noise, remnoise, rxerrors, fixed), force_mavlink1=force_mavlink1)

## file_transfer_protocol_encode
    def file_transfer_protocol_encode(self, target_network: int, target_system: int, target_component: int, payload: Sequence[int]) -> MAVLink_file_transfer_protocol_message:
        """
        File transfer protocol message:
        https://mavlink.io/en/services/ftp.html.

        target_network            : Network ID (0 for broadcast) (type:uint8_t)
        target_system             : System ID (0 for broadcast) (type:uint8_t)
        target_component          : Component ID (0 for broadcast) (type:uint8_t)
        payload                   : Variable length payload. The length is defined by the remaining message length when subtracting the header and other fields.  The entire content of this block is opaque unless you understand any the encoding message_type.  The particular encoding used can be extension specific and might not always be documented as part of the mavlink specification. (type:uint8_t)

        """
        return MAVLink_file_transfer_protocol_message(target_network, target_system, target_component, payload)

## file_transfer_protocol_send
    def file_transfer_protocol_send(self, target_network: int, target_system: int, target_component: int, payload: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        File transfer protocol message:
        https://mavlink.io/en/services/ftp.html.

        target_network            : Network ID (0 for broadcast) (type:uint8_t)
        target_system             : System ID (0 for broadcast) (type:uint8_t)
        target_component          : Component ID (0 for broadcast) (type:uint8_t)
        payload                   : Variable length payload. The length is defined by the remaining message length when subtracting the header and other fields.  The entire content of this block is opaque unless you understand any the encoding message_type.  The particular encoding used can be extension specific and might not always be documented as part of the mavlink specification. (type:uint8_t)

        """
        self.send(self.file_transfer_protocol_encode(target_network, target_system, target_component, payload), force_mavlink1=force_mavlink1)

## timesync_encode
    def timesync_encode(self, tc1: int, ts1: int) -> MAVLink_timesync_message:
        """
        Time synchronization message.

        tc1                       : Time sync timestamp 1 (type:int64_t)
        ts1                       : Time sync timestamp 2 (type:int64_t)

        """
        return MAVLink_timesync_message(tc1, ts1)

## timesync_send
    def timesync_send(self, tc1: int, ts1: int, force_mavlink1: bool = False) -> None:
        """
        Time synchronization message.

        tc1                       : Time sync timestamp 1 (type:int64_t)
        ts1                       : Time sync timestamp 2 (type:int64_t)

        """
        self.send(self.timesync_encode(tc1, ts1), force_mavlink1=force_mavlink1)

## camera_trigger_encode
    def camera_trigger_encode(self, time_usec: int, seq: int) -> MAVLink_camera_trigger_message:
        """
        Camera-IMU triggering and synchronisation message.

        time_usec                 : Timestamp for image frame (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        seq                       : Image frame sequence (type:uint32_t)

        """
        return MAVLink_camera_trigger_message(time_usec, seq)

## camera_trigger_send
    def camera_trigger_send(self, time_usec: int, seq: int, force_mavlink1: bool = False) -> None:
        """
        Camera-IMU triggering and synchronisation message.

        time_usec                 : Timestamp for image frame (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        seq                       : Image frame sequence (type:uint32_t)

        """
        self.send(self.camera_trigger_encode(time_usec, seq), force_mavlink1=force_mavlink1)

## hil_gps_encode
    def hil_gps_encode(self, time_usec: int, fix_type: int, lat: int, lon: int, alt: int, eph: int, epv: int, vel: int, vn: int, ve: int, vd: int, cog: int, satellites_visible: int, id: int = 0, yaw: int = 0) -> MAVLink_hil_gps_message:
        """
        The global position, as returned by the Global Positioning System
        (GPS). This is                  NOT the global position
        estimate of the system, but rather a RAW sensor value. See
        message GLOBAL_POSITION_INT for the global position estimate.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        fix_type                  : 0-1: no fix, 2: 2D fix, 3: 3D fix. Some applications will not use the value of this field unless it is at least two, so always correctly fill in the fix. (type:uint8_t)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        eph                       : GPS HDOP horizontal dilution of position (unitless * 100). If unknown, set to: UINT16_MAX (type:uint16_t)
        epv                       : GPS VDOP vertical dilution of position (unitless * 100). If unknown, set to: UINT16_MAX (type:uint16_t)
        vel                       : GPS ground speed. If unknown, set to: UINT16_MAX [cm/s] (type:uint16_t)
        vn                        : GPS velocity in north direction in earth-fixed NED frame [cm/s] (type:int16_t)
        ve                        : GPS velocity in east direction in earth-fixed NED frame [cm/s] (type:int16_t)
        vd                        : GPS velocity in down direction in earth-fixed NED frame [cm/s] (type:int16_t)
        cog                       : Course over ground (NOT heading, but direction of movement), 0.0..359.99 degrees. If unknown, set to: UINT16_MAX [cdeg] (type:uint16_t)
        satellites_visible        : Number of satellites visible. If unknown, set to UINT8_MAX (type:uint8_t)
        id                        : GPS ID (zero indexed). Used for multiple GPS inputs (type:uint8_t)
        yaw                       : Yaw of vehicle relative to Earth's North, zero means not available, use 36000 for north [cdeg] (type:uint16_t)

        """
        return MAVLink_hil_gps_message(time_usec, fix_type, lat, lon, alt, eph, epv, vel, vn, ve, vd, cog, satellites_visible, id, yaw)

## hil_gps_send
    def hil_gps_send(self, time_usec: int, fix_type: int, lat: int, lon: int, alt: int, eph: int, epv: int, vel: int, vn: int, ve: int, vd: int, cog: int, satellites_visible: int, id: int = 0, yaw: int = 0, force_mavlink1: bool = False) -> None:
        """
        The global position, as returned by the Global Positioning System
        (GPS). This is                  NOT the global position
        estimate of the system, but rather a RAW sensor value. See
        message GLOBAL_POSITION_INT for the global position estimate.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        fix_type                  : 0-1: no fix, 2: 2D fix, 3: 3D fix. Some applications will not use the value of this field unless it is at least two, so always correctly fill in the fix. (type:uint8_t)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        eph                       : GPS HDOP horizontal dilution of position (unitless * 100). If unknown, set to: UINT16_MAX (type:uint16_t)
        epv                       : GPS VDOP vertical dilution of position (unitless * 100). If unknown, set to: UINT16_MAX (type:uint16_t)
        vel                       : GPS ground speed. If unknown, set to: UINT16_MAX [cm/s] (type:uint16_t)
        vn                        : GPS velocity in north direction in earth-fixed NED frame [cm/s] (type:int16_t)
        ve                        : GPS velocity in east direction in earth-fixed NED frame [cm/s] (type:int16_t)
        vd                        : GPS velocity in down direction in earth-fixed NED frame [cm/s] (type:int16_t)
        cog                       : Course over ground (NOT heading, but direction of movement), 0.0..359.99 degrees. If unknown, set to: UINT16_MAX [cdeg] (type:uint16_t)
        satellites_visible        : Number of satellites visible. If unknown, set to UINT8_MAX (type:uint8_t)
        id                        : GPS ID (zero indexed). Used for multiple GPS inputs (type:uint8_t)
        yaw                       : Yaw of vehicle relative to Earth's North, zero means not available, use 36000 for north [cdeg] (type:uint16_t)

        """
        self.send(self.hil_gps_encode(time_usec, fix_type, lat, lon, alt, eph, epv, vel, vn, ve, vd, cog, satellites_visible, id, yaw), force_mavlink1=force_mavlink1)

## hil_optical_flow_encode
    def hil_optical_flow_encode(self, time_usec: int, sensor_id: int, integration_time_us: int, integrated_x: float, integrated_y: float, integrated_xgyro: float, integrated_ygyro: float, integrated_zgyro: float, temperature: int, quality: int, time_delta_distance_us: int, distance: float) -> MAVLink_hil_optical_flow_message:
        """
        Simulated optical flow from a flow sensor (e.g. PX4FLOW or optical
        mouse sensor)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        sensor_id                 : Sensor ID (type:uint8_t)
        integration_time_us        : Integration time. Divide integrated_x and integrated_y by the integration time to obtain average flow. The integration time also indicates the. [us] (type:uint32_t)
        integrated_x              : Flow in radians around X axis (Sensor RH rotation about the X axis induces a positive flow. Sensor linear motion along the positive Y axis induces a negative flow.) [rad] (type:float)
        integrated_y              : Flow in radians around Y axis (Sensor RH rotation about the Y axis induces a positive flow. Sensor linear motion along the positive X axis induces a positive flow.) [rad] (type:float)
        integrated_xgyro          : RH rotation around X axis [rad] (type:float)
        integrated_ygyro          : RH rotation around Y axis [rad] (type:float)
        integrated_zgyro          : RH rotation around Z axis [rad] (type:float)
        temperature               : Temperature [cdegC] (type:int16_t)
        quality                   : Optical flow quality / confidence. 0: no valid flow, 255: maximum quality (type:uint8_t)
        time_delta_distance_us        : Time since the distance was sampled. [us] (type:uint32_t)
        distance                  : Distance to the center of the flow field. Positive value (including zero): distance known. Negative value: Unknown distance. [m] (type:float)

        """
        return MAVLink_hil_optical_flow_message(time_usec, sensor_id, integration_time_us, integrated_x, integrated_y, integrated_xgyro, integrated_ygyro, integrated_zgyro, temperature, quality, time_delta_distance_us, distance)

## hil_optical_flow_send
    def hil_optical_flow_send(self, time_usec: int, sensor_id: int, integration_time_us: int, integrated_x: float, integrated_y: float, integrated_xgyro: float, integrated_ygyro: float, integrated_zgyro: float, temperature: int, quality: int, time_delta_distance_us: int, distance: float, force_mavlink1: bool = False) -> None:
        """
        Simulated optical flow from a flow sensor (e.g. PX4FLOW or optical
        mouse sensor)

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        sensor_id                 : Sensor ID (type:uint8_t)
        integration_time_us        : Integration time. Divide integrated_x and integrated_y by the integration time to obtain average flow. The integration time also indicates the. [us] (type:uint32_t)
        integrated_x              : Flow in radians around X axis (Sensor RH rotation about the X axis induces a positive flow. Sensor linear motion along the positive Y axis induces a negative flow.) [rad] (type:float)
        integrated_y              : Flow in radians around Y axis (Sensor RH rotation about the Y axis induces a positive flow. Sensor linear motion along the positive X axis induces a positive flow.) [rad] (type:float)
        integrated_xgyro          : RH rotation around X axis [rad] (type:float)
        integrated_ygyro          : RH rotation around Y axis [rad] (type:float)
        integrated_zgyro          : RH rotation around Z axis [rad] (type:float)
        temperature               : Temperature [cdegC] (type:int16_t)
        quality                   : Optical flow quality / confidence. 0: no valid flow, 255: maximum quality (type:uint8_t)
        time_delta_distance_us        : Time since the distance was sampled. [us] (type:uint32_t)
        distance                  : Distance to the center of the flow field. Positive value (including zero): distance known. Negative value: Unknown distance. [m] (type:float)

        """
        self.send(self.hil_optical_flow_encode(time_usec, sensor_id, integration_time_us, integrated_x, integrated_y, integrated_xgyro, integrated_ygyro, integrated_zgyro, temperature, quality, time_delta_distance_us, distance), force_mavlink1=force_mavlink1)

## hil_state_quaternion_encode
    def hil_state_quaternion_encode(self, time_usec: int, attitude_quaternion: Sequence[float], rollspeed: float, pitchspeed: float, yawspeed: float, lat: int, lon: int, alt: int, vx: int, vy: int, vz: int, ind_airspeed: int, true_airspeed: int, xacc: int, yacc: int, zacc: int) -> MAVLink_hil_state_quaternion_message:
        """
        Sent from simulation to autopilot, avoids in contrast to HIL_STATE
        singularities. This packet is useful for high throughput
        applications such as hardware in the loop simulations.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        attitude_quaternion        : Vehicle attitude expressed as normalized quaternion in w, x, y, z order (with 1 0 0 0 being the null-rotation) (type:float)
        rollspeed                 : Body frame roll / phi angular speed [rad/s] (type:float)
        pitchspeed                : Body frame pitch / theta angular speed [rad/s] (type:float)
        yawspeed                  : Body frame yaw / psi angular speed [rad/s] (type:float)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        alt                       : Altitude [mm] (type:int32_t)
        vx                        : Ground X Speed (Latitude) [cm/s] (type:int16_t)
        vy                        : Ground Y Speed (Longitude) [cm/s] (type:int16_t)
        vz                        : Ground Z Speed (Altitude) [cm/s] (type:int16_t)
        ind_airspeed              : Indicated airspeed [cm/s] (type:uint16_t)
        true_airspeed             : True airspeed [cm/s] (type:uint16_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)

        """
        return MAVLink_hil_state_quaternion_message(time_usec, attitude_quaternion, rollspeed, pitchspeed, yawspeed, lat, lon, alt, vx, vy, vz, ind_airspeed, true_airspeed, xacc, yacc, zacc)

## hil_state_quaternion_send
    def hil_state_quaternion_send(self, time_usec: int, attitude_quaternion: Sequence[float], rollspeed: float, pitchspeed: float, yawspeed: float, lat: int, lon: int, alt: int, vx: int, vy: int, vz: int, ind_airspeed: int, true_airspeed: int, xacc: int, yacc: int, zacc: int, force_mavlink1: bool = False) -> None:
        """
        Sent from simulation to autopilot, avoids in contrast to HIL_STATE
        singularities. This packet is useful for high throughput
        applications such as hardware in the loop simulations.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        attitude_quaternion        : Vehicle attitude expressed as normalized quaternion in w, x, y, z order (with 1 0 0 0 being the null-rotation) (type:float)
        rollspeed                 : Body frame roll / phi angular speed [rad/s] (type:float)
        pitchspeed                : Body frame pitch / theta angular speed [rad/s] (type:float)
        yawspeed                  : Body frame yaw / psi angular speed [rad/s] (type:float)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        alt                       : Altitude [mm] (type:int32_t)
        vx                        : Ground X Speed (Latitude) [cm/s] (type:int16_t)
        vy                        : Ground Y Speed (Longitude) [cm/s] (type:int16_t)
        vz                        : Ground Z Speed (Altitude) [cm/s] (type:int16_t)
        ind_airspeed              : Indicated airspeed [cm/s] (type:uint16_t)
        true_airspeed             : True airspeed [cm/s] (type:uint16_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)

        """
        self.send(self.hil_state_quaternion_encode(time_usec, attitude_quaternion, rollspeed, pitchspeed, yawspeed, lat, lon, alt, vx, vy, vz, ind_airspeed, true_airspeed, xacc, yacc, zacc), force_mavlink1=force_mavlink1)

## scaled_imu2_encode
    def scaled_imu2_encode(self, time_boot_ms: int, xacc: int, yacc: int, zacc: int, xgyro: int, ygyro: int, zgyro: int, xmag: int, ymag: int, zmag: int, temperature: int = 0) -> MAVLink_scaled_imu2_message:
        """
        The RAW IMU readings for secondary 9DOF sensor setup. This message
        should contain the scaled values to the described units

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)
        xgyro                     : Angular speed around X axis [mrad/s] (type:int16_t)
        ygyro                     : Angular speed around Y axis [mrad/s] (type:int16_t)
        zgyro                     : Angular speed around Z axis [mrad/s] (type:int16_t)
        xmag                      : X Magnetic field [mgauss] (type:int16_t)
        ymag                      : Y Magnetic field [mgauss] (type:int16_t)
        zmag                      : Z Magnetic field [mgauss] (type:int16_t)
        temperature               : Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). [cdegC] (type:int16_t)

        """
        return MAVLink_scaled_imu2_message(time_boot_ms, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, temperature)

## scaled_imu2_send
    def scaled_imu2_send(self, time_boot_ms: int, xacc: int, yacc: int, zacc: int, xgyro: int, ygyro: int, zgyro: int, xmag: int, ymag: int, zmag: int, temperature: int = 0, force_mavlink1: bool = False) -> None:
        """
        The RAW IMU readings for secondary 9DOF sensor setup. This message
        should contain the scaled values to the described units

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)
        xgyro                     : Angular speed around X axis [mrad/s] (type:int16_t)
        ygyro                     : Angular speed around Y axis [mrad/s] (type:int16_t)
        zgyro                     : Angular speed around Z axis [mrad/s] (type:int16_t)
        xmag                      : X Magnetic field [mgauss] (type:int16_t)
        ymag                      : Y Magnetic field [mgauss] (type:int16_t)
        zmag                      : Z Magnetic field [mgauss] (type:int16_t)
        temperature               : Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). [cdegC] (type:int16_t)

        """
        self.send(self.scaled_imu2_encode(time_boot_ms, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, temperature), force_mavlink1=force_mavlink1)

## log_request_list_encode
    def log_request_list_encode(self, target_system: int, target_component: int, start: int, end: int) -> MAVLink_log_request_list_message:
        """
        Request a list of available logs. On some systems calling this may
        stop on-board logging until LOG_REQUEST_END is called. If
        there are no log files available this request shall be
        answered with one LOG_ENTRY message with id = 0 and num_logs =
        0.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        start                     : First log id (0 for first available) (type:uint16_t)
        end                       : Last log id (0xffff for last available) (type:uint16_t)

        """
        return MAVLink_log_request_list_message(target_system, target_component, start, end)

## log_request_list_send
    def log_request_list_send(self, target_system: int, target_component: int, start: int, end: int, force_mavlink1: bool = False) -> None:
        """
        Request a list of available logs. On some systems calling this may
        stop on-board logging until LOG_REQUEST_END is called. If
        there are no log files available this request shall be
        answered with one LOG_ENTRY message with id = 0 and num_logs =
        0.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        start                     : First log id (0 for first available) (type:uint16_t)
        end                       : Last log id (0xffff for last available) (type:uint16_t)

        """
        self.send(self.log_request_list_encode(target_system, target_component, start, end), force_mavlink1=force_mavlink1)

## log_entry_encode
    def log_entry_encode(self, id: int, num_logs: int, last_log_num: int, time_utc: int, size: int) -> MAVLink_log_entry_message:
        """
        Reply to LOG_REQUEST_LIST

        id                        : Log id (type:uint16_t)
        num_logs                  : Total number of logs (type:uint16_t)
        last_log_num              : High log number (type:uint16_t)
        time_utc                  : UTC timestamp of log since 1970, or 0 if not available [s] (type:uint32_t)
        size                      : Size of the log (may be approximate) [bytes] (type:uint32_t)

        """
        return MAVLink_log_entry_message(id, num_logs, last_log_num, time_utc, size)

## log_entry_send
    def log_entry_send(self, id: int, num_logs: int, last_log_num: int, time_utc: int, size: int, force_mavlink1: bool = False) -> None:
        """
        Reply to LOG_REQUEST_LIST

        id                        : Log id (type:uint16_t)
        num_logs                  : Total number of logs (type:uint16_t)
        last_log_num              : High log number (type:uint16_t)
        time_utc                  : UTC timestamp of log since 1970, or 0 if not available [s] (type:uint32_t)
        size                      : Size of the log (may be approximate) [bytes] (type:uint32_t)

        """
        self.send(self.log_entry_encode(id, num_logs, last_log_num, time_utc, size), force_mavlink1=force_mavlink1)

## log_request_data_encode
    def log_request_data_encode(self, target_system: int, target_component: int, id: int, ofs: int, count: int) -> MAVLink_log_request_data_message:
        """
        Request a chunk of a log

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        id                        : Log id (from LOG_ENTRY reply) (type:uint16_t)
        ofs                       : Offset into the log (type:uint32_t)
        count                     : Number of bytes [bytes] (type:uint32_t)

        """
        return MAVLink_log_request_data_message(target_system, target_component, id, ofs, count)

## log_request_data_send
    def log_request_data_send(self, target_system: int, target_component: int, id: int, ofs: int, count: int, force_mavlink1: bool = False) -> None:
        """
        Request a chunk of a log

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        id                        : Log id (from LOG_ENTRY reply) (type:uint16_t)
        ofs                       : Offset into the log (type:uint32_t)
        count                     : Number of bytes [bytes] (type:uint32_t)

        """
        self.send(self.log_request_data_encode(target_system, target_component, id, ofs, count), force_mavlink1=force_mavlink1)

## log_data_encode
    def log_data_encode(self, id: int, ofs: int, count: int, data: Sequence[int]) -> MAVLink_log_data_message:
        """
        Reply to LOG_REQUEST_DATA

        id                        : Log id (from LOG_ENTRY reply) (type:uint16_t)
        ofs                       : Offset into the log (type:uint32_t)
        count                     : Number of bytes (zero for end of log) [bytes] (type:uint8_t)
        data                      : log data (type:uint8_t)

        """
        return MAVLink_log_data_message(id, ofs, count, data)

## log_data_send
    def log_data_send(self, id: int, ofs: int, count: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Reply to LOG_REQUEST_DATA

        id                        : Log id (from LOG_ENTRY reply) (type:uint16_t)
        ofs                       : Offset into the log (type:uint32_t)
        count                     : Number of bytes (zero for end of log) [bytes] (type:uint8_t)
        data                      : log data (type:uint8_t)

        """
        self.send(self.log_data_encode(id, ofs, count, data), force_mavlink1=force_mavlink1)

## log_erase_encode
    def log_erase_encode(self, target_system: int, target_component: int) -> MAVLink_log_erase_message:
        """
        Erase all logs

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)

        """
        return MAVLink_log_erase_message(target_system, target_component)

## log_erase_send
    def log_erase_send(self, target_system: int, target_component: int, force_mavlink1: bool = False) -> None:
        """
        Erase all logs

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)

        """
        self.send(self.log_erase_encode(target_system, target_component), force_mavlink1=force_mavlink1)

## log_request_end_encode
    def log_request_end_encode(self, target_system: int, target_component: int) -> MAVLink_log_request_end_message:
        """
        Stop log transfer and resume normal logging

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)

        """
        return MAVLink_log_request_end_message(target_system, target_component)

## log_request_end_send
    def log_request_end_send(self, target_system: int, target_component: int, force_mavlink1: bool = False) -> None:
        """
        Stop log transfer and resume normal logging

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)

        """
        self.send(self.log_request_end_encode(target_system, target_component), force_mavlink1=force_mavlink1)

## gps_inject_data_encode
    def gps_inject_data_encode(self, target_system: int, target_component: int, len: int, data: Sequence[int]) -> MAVLink_gps_inject_data_message:
        """
        Data for injecting into the onboard GPS (used for DGPS)

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        len                       : Data length [bytes] (type:uint8_t)
        data                      : Raw data (110 is enough for 12 satellites of RTCMv2) (type:uint8_t)

        """
        return MAVLink_gps_inject_data_message(target_system, target_component, len, data)

## gps_inject_data_send
    def gps_inject_data_send(self, target_system: int, target_component: int, len: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Data for injecting into the onboard GPS (used for DGPS)

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        len                       : Data length [bytes] (type:uint8_t)
        data                      : Raw data (110 is enough for 12 satellites of RTCMv2) (type:uint8_t)

        """
        self.send(self.gps_inject_data_encode(target_system, target_component, len, data), force_mavlink1=force_mavlink1)

## gps2_raw_encode
    def gps2_raw_encode(self, time_usec: int, fix_type: int, lat: int, lon: int, alt: int, eph: int, epv: int, vel: int, cog: int, satellites_visible: int, dgps_numch: int, dgps_age: int, yaw: int = 0, alt_ellipsoid: int = 0, h_acc: int = 0, v_acc: int = 0, vel_acc: int = 0, hdg_acc: int = 0) -> MAVLink_gps2_raw_message:
        """
        Second GPS data.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        fix_type                  : GPS fix type. (type:uint8_t, values:GPS_FIX_TYPE)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        eph                       : GPS HDOP horizontal dilution of position (unitless). If unknown, set to: UINT16_MAX (type:uint16_t)
        epv                       : GPS VDOP vertical dilution of position (unitless). If unknown, set to: UINT16_MAX (type:uint16_t)
        vel                       : GPS ground speed. If unknown, set to: UINT16_MAX [cm/s] (type:uint16_t)
        cog                       : Course over ground (NOT heading, but direction of movement): 0.0..359.99 degrees. If unknown, set to: UINT16_MAX [cdeg] (type:uint16_t)
        satellites_visible        : Number of satellites visible. If unknown, set to 255 (type:uint8_t)
        dgps_numch                : Number of DGPS satellites (type:uint8_t)
        dgps_age                  : Age of DGPS info [ms] (type:uint32_t)
        yaw                       : Yaw in earth frame from north. Use 0 if this GPS does not provide yaw. Use UINT16_MAX if this GPS is configured to provide yaw and is currently unable to provide it. Use 36000 for north. [cdeg] (type:uint16_t)
        alt_ellipsoid             : Altitude (above WGS84, EGM96 ellipsoid). Positive for up. [mm] (type:int32_t)
        h_acc                     : Position uncertainty. [mm] (type:uint32_t)
        v_acc                     : Altitude uncertainty. [mm] (type:uint32_t)
        vel_acc                   : Speed uncertainty. [mm/s] (type:uint32_t)
        hdg_acc                   : Heading / track uncertainty [degE5] (type:uint32_t)

        """
        return MAVLink_gps2_raw_message(time_usec, fix_type, lat, lon, alt, eph, epv, vel, cog, satellites_visible, dgps_numch, dgps_age, yaw, alt_ellipsoid, h_acc, v_acc, vel_acc, hdg_acc)

## gps2_raw_send
    def gps2_raw_send(self, time_usec: int, fix_type: int, lat: int, lon: int, alt: int, eph: int, epv: int, vel: int, cog: int, satellites_visible: int, dgps_numch: int, dgps_age: int, yaw: int = 0, alt_ellipsoid: int = 0, h_acc: int = 0, v_acc: int = 0, vel_acc: int = 0, hdg_acc: int = 0, force_mavlink1: bool = False) -> None:
        """
        Second GPS data.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        fix_type                  : GPS fix type. (type:uint8_t, values:GPS_FIX_TYPE)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        eph                       : GPS HDOP horizontal dilution of position (unitless). If unknown, set to: UINT16_MAX (type:uint16_t)
        epv                       : GPS VDOP vertical dilution of position (unitless). If unknown, set to: UINT16_MAX (type:uint16_t)
        vel                       : GPS ground speed. If unknown, set to: UINT16_MAX [cm/s] (type:uint16_t)
        cog                       : Course over ground (NOT heading, but direction of movement): 0.0..359.99 degrees. If unknown, set to: UINT16_MAX [cdeg] (type:uint16_t)
        satellites_visible        : Number of satellites visible. If unknown, set to 255 (type:uint8_t)
        dgps_numch                : Number of DGPS satellites (type:uint8_t)
        dgps_age                  : Age of DGPS info [ms] (type:uint32_t)
        yaw                       : Yaw in earth frame from north. Use 0 if this GPS does not provide yaw. Use UINT16_MAX if this GPS is configured to provide yaw and is currently unable to provide it. Use 36000 for north. [cdeg] (type:uint16_t)
        alt_ellipsoid             : Altitude (above WGS84, EGM96 ellipsoid). Positive for up. [mm] (type:int32_t)
        h_acc                     : Position uncertainty. [mm] (type:uint32_t)
        v_acc                     : Altitude uncertainty. [mm] (type:uint32_t)
        vel_acc                   : Speed uncertainty. [mm/s] (type:uint32_t)
        hdg_acc                   : Heading / track uncertainty [degE5] (type:uint32_t)

        """
        self.send(self.gps2_raw_encode(time_usec, fix_type, lat, lon, alt, eph, epv, vel, cog, satellites_visible, dgps_numch, dgps_age, yaw, alt_ellipsoid, h_acc, v_acc, vel_acc, hdg_acc), force_mavlink1=force_mavlink1)

## power_status_encode
    def power_status_encode(self, Vcc: int, Vservo: int, flags: int) -> MAVLink_power_status_message:
        """
        Power supply status

        Vcc                       : 5V rail voltage. [mV] (type:uint16_t)
        Vservo                    : Servo rail voltage. [mV] (type:uint16_t)
        flags                     : Bitmap of power supply status flags. (type:uint16_t, values:MAV_POWER_STATUS)

        """
        return MAVLink_power_status_message(Vcc, Vservo, flags)

## power_status_send
    def power_status_send(self, Vcc: int, Vservo: int, flags: int, force_mavlink1: bool = False) -> None:
        """
        Power supply status

        Vcc                       : 5V rail voltage. [mV] (type:uint16_t)
        Vservo                    : Servo rail voltage. [mV] (type:uint16_t)
        flags                     : Bitmap of power supply status flags. (type:uint16_t, values:MAV_POWER_STATUS)

        """
        self.send(self.power_status_encode(Vcc, Vservo, flags), force_mavlink1=force_mavlink1)

## serial_control_encode
    def serial_control_encode(self, device: int, flags: int, timeout: int, baudrate: int, count: int, data: Sequence[int]) -> MAVLink_serial_control_message:
        """
        Control a serial port. This can be used for raw access to an onboard
        serial peripheral such as a GPS or telemetry radio. It is
        designed to make it possible to update the devices firmware
        via MAVLink messages or change the devices settings. A message
        with zero bytes can be used to change just the baudrate.

        device                    : Serial control device type. (type:uint8_t, values:SERIAL_CONTROL_DEV)
        flags                     : Bitmap of serial control flags. (type:uint8_t, values:SERIAL_CONTROL_FLAG)
        timeout                   : Timeout for reply data [ms] (type:uint16_t)
        baudrate                  : Baudrate of transfer. Zero means no change. [bits/s] (type:uint32_t)
        count                     : how many bytes in this transfer [bytes] (type:uint8_t)
        data                      : serial data (type:uint8_t)

        """
        return MAVLink_serial_control_message(device, flags, timeout, baudrate, count, data)

## serial_control_send
    def serial_control_send(self, device: int, flags: int, timeout: int, baudrate: int, count: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Control a serial port. This can be used for raw access to an onboard
        serial peripheral such as a GPS or telemetry radio. It is
        designed to make it possible to update the devices firmware
        via MAVLink messages or change the devices settings. A message
        with zero bytes can be used to change just the baudrate.

        device                    : Serial control device type. (type:uint8_t, values:SERIAL_CONTROL_DEV)
        flags                     : Bitmap of serial control flags. (type:uint8_t, values:SERIAL_CONTROL_FLAG)
        timeout                   : Timeout for reply data [ms] (type:uint16_t)
        baudrate                  : Baudrate of transfer. Zero means no change. [bits/s] (type:uint32_t)
        count                     : how many bytes in this transfer [bytes] (type:uint8_t)
        data                      : serial data (type:uint8_t)

        """
        self.send(self.serial_control_encode(device, flags, timeout, baudrate, count, data), force_mavlink1=force_mavlink1)

## gps_rtk_encode
    def gps_rtk_encode(self, time_last_baseline_ms: int, rtk_receiver_id: int, wn: int, tow: int, rtk_health: int, rtk_rate: int, nsats: int, baseline_coords_type: int, baseline_a_mm: int, baseline_b_mm: int, baseline_c_mm: int, accuracy: int, iar_num_hypotheses: int) -> MAVLink_gps_rtk_message:
        """
        RTK GPS data. Gives information on the relative baseline calculation
        the GPS is reporting

        time_last_baseline_ms        : Time since boot of last baseline message received. [ms] (type:uint32_t)
        rtk_receiver_id           : Identification of connected RTK receiver. (type:uint8_t)
        wn                        : GPS Week Number of last baseline (type:uint16_t)
        tow                       : GPS Time of Week of last baseline [ms] (type:uint32_t)
        rtk_health                : GPS-specific health report for RTK data. (type:uint8_t)
        rtk_rate                  : Rate of baseline messages being received by GPS [Hz] (type:uint8_t)
        nsats                     : Current number of sats used for RTK calculation. (type:uint8_t)
        baseline_coords_type        : Coordinate system of baseline (type:uint8_t, values:RTK_BASELINE_COORDINATE_SYSTEM)
        baseline_a_mm             : Current baseline in ECEF x or NED north component. [mm] (type:int32_t)
        baseline_b_mm             : Current baseline in ECEF y or NED east component. [mm] (type:int32_t)
        baseline_c_mm             : Current baseline in ECEF z or NED down component. [mm] (type:int32_t)
        accuracy                  : Current estimate of baseline accuracy. (type:uint32_t)
        iar_num_hypotheses        : Current number of integer ambiguity hypotheses. (type:int32_t)

        """
        return MAVLink_gps_rtk_message(time_last_baseline_ms, rtk_receiver_id, wn, tow, rtk_health, rtk_rate, nsats, baseline_coords_type, baseline_a_mm, baseline_b_mm, baseline_c_mm, accuracy, iar_num_hypotheses)

## gps_rtk_send
    def gps_rtk_send(self, time_last_baseline_ms: int, rtk_receiver_id: int, wn: int, tow: int, rtk_health: int, rtk_rate: int, nsats: int, baseline_coords_type: int, baseline_a_mm: int, baseline_b_mm: int, baseline_c_mm: int, accuracy: int, iar_num_hypotheses: int, force_mavlink1: bool = False) -> None:
        """
        RTK GPS data. Gives information on the relative baseline calculation
        the GPS is reporting

        time_last_baseline_ms        : Time since boot of last baseline message received. [ms] (type:uint32_t)
        rtk_receiver_id           : Identification of connected RTK receiver. (type:uint8_t)
        wn                        : GPS Week Number of last baseline (type:uint16_t)
        tow                       : GPS Time of Week of last baseline [ms] (type:uint32_t)
        rtk_health                : GPS-specific health report for RTK data. (type:uint8_t)
        rtk_rate                  : Rate of baseline messages being received by GPS [Hz] (type:uint8_t)
        nsats                     : Current number of sats used for RTK calculation. (type:uint8_t)
        baseline_coords_type        : Coordinate system of baseline (type:uint8_t, values:RTK_BASELINE_COORDINATE_SYSTEM)
        baseline_a_mm             : Current baseline in ECEF x or NED north component. [mm] (type:int32_t)
        baseline_b_mm             : Current baseline in ECEF y or NED east component. [mm] (type:int32_t)
        baseline_c_mm             : Current baseline in ECEF z or NED down component. [mm] (type:int32_t)
        accuracy                  : Current estimate of baseline accuracy. (type:uint32_t)
        iar_num_hypotheses        : Current number of integer ambiguity hypotheses. (type:int32_t)

        """
        self.send(self.gps_rtk_encode(time_last_baseline_ms, rtk_receiver_id, wn, tow, rtk_health, rtk_rate, nsats, baseline_coords_type, baseline_a_mm, baseline_b_mm, baseline_c_mm, accuracy, iar_num_hypotheses), force_mavlink1=force_mavlink1)

## gps2_rtk_encode
    def gps2_rtk_encode(self, time_last_baseline_ms: int, rtk_receiver_id: int, wn: int, tow: int, rtk_health: int, rtk_rate: int, nsats: int, baseline_coords_type: int, baseline_a_mm: int, baseline_b_mm: int, baseline_c_mm: int, accuracy: int, iar_num_hypotheses: int) -> MAVLink_gps2_rtk_message:
        """
        RTK GPS data. Gives information on the relative baseline calculation
        the GPS is reporting

        time_last_baseline_ms        : Time since boot of last baseline message received. [ms] (type:uint32_t)
        rtk_receiver_id           : Identification of connected RTK receiver. (type:uint8_t)
        wn                        : GPS Week Number of last baseline (type:uint16_t)
        tow                       : GPS Time of Week of last baseline [ms] (type:uint32_t)
        rtk_health                : GPS-specific health report for RTK data. (type:uint8_t)
        rtk_rate                  : Rate of baseline messages being received by GPS [Hz] (type:uint8_t)
        nsats                     : Current number of sats used for RTK calculation. (type:uint8_t)
        baseline_coords_type        : Coordinate system of baseline (type:uint8_t, values:RTK_BASELINE_COORDINATE_SYSTEM)
        baseline_a_mm             : Current baseline in ECEF x or NED north component. [mm] (type:int32_t)
        baseline_b_mm             : Current baseline in ECEF y or NED east component. [mm] (type:int32_t)
        baseline_c_mm             : Current baseline in ECEF z or NED down component. [mm] (type:int32_t)
        accuracy                  : Current estimate of baseline accuracy. (type:uint32_t)
        iar_num_hypotheses        : Current number of integer ambiguity hypotheses. (type:int32_t)

        """
        return MAVLink_gps2_rtk_message(time_last_baseline_ms, rtk_receiver_id, wn, tow, rtk_health, rtk_rate, nsats, baseline_coords_type, baseline_a_mm, baseline_b_mm, baseline_c_mm, accuracy, iar_num_hypotheses)

## gps2_rtk_send
    def gps2_rtk_send(self, time_last_baseline_ms: int, rtk_receiver_id: int, wn: int, tow: int, rtk_health: int, rtk_rate: int, nsats: int, baseline_coords_type: int, baseline_a_mm: int, baseline_b_mm: int, baseline_c_mm: int, accuracy: int, iar_num_hypotheses: int, force_mavlink1: bool = False) -> None:
        """
        RTK GPS data. Gives information on the relative baseline calculation
        the GPS is reporting

        time_last_baseline_ms        : Time since boot of last baseline message received. [ms] (type:uint32_t)
        rtk_receiver_id           : Identification of connected RTK receiver. (type:uint8_t)
        wn                        : GPS Week Number of last baseline (type:uint16_t)
        tow                       : GPS Time of Week of last baseline [ms] (type:uint32_t)
        rtk_health                : GPS-specific health report for RTK data. (type:uint8_t)
        rtk_rate                  : Rate of baseline messages being received by GPS [Hz] (type:uint8_t)
        nsats                     : Current number of sats used for RTK calculation. (type:uint8_t)
        baseline_coords_type        : Coordinate system of baseline (type:uint8_t, values:RTK_BASELINE_COORDINATE_SYSTEM)
        baseline_a_mm             : Current baseline in ECEF x or NED north component. [mm] (type:int32_t)
        baseline_b_mm             : Current baseline in ECEF y or NED east component. [mm] (type:int32_t)
        baseline_c_mm             : Current baseline in ECEF z or NED down component. [mm] (type:int32_t)
        accuracy                  : Current estimate of baseline accuracy. (type:uint32_t)
        iar_num_hypotheses        : Current number of integer ambiguity hypotheses. (type:int32_t)

        """
        self.send(self.gps2_rtk_encode(time_last_baseline_ms, rtk_receiver_id, wn, tow, rtk_health, rtk_rate, nsats, baseline_coords_type, baseline_a_mm, baseline_b_mm, baseline_c_mm, accuracy, iar_num_hypotheses), force_mavlink1=force_mavlink1)

## scaled_imu3_encode
    def scaled_imu3_encode(self, time_boot_ms: int, xacc: int, yacc: int, zacc: int, xgyro: int, ygyro: int, zgyro: int, xmag: int, ymag: int, zmag: int, temperature: int = 0) -> MAVLink_scaled_imu3_message:
        """
        The RAW IMU readings for 3rd 9DOF sensor setup. This message should
        contain the scaled values to the described units

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)
        xgyro                     : Angular speed around X axis [mrad/s] (type:int16_t)
        ygyro                     : Angular speed around Y axis [mrad/s] (type:int16_t)
        zgyro                     : Angular speed around Z axis [mrad/s] (type:int16_t)
        xmag                      : X Magnetic field [mgauss] (type:int16_t)
        ymag                      : Y Magnetic field [mgauss] (type:int16_t)
        zmag                      : Z Magnetic field [mgauss] (type:int16_t)
        temperature               : Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). [cdegC] (type:int16_t)

        """
        return MAVLink_scaled_imu3_message(time_boot_ms, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, temperature)

## scaled_imu3_send
    def scaled_imu3_send(self, time_boot_ms: int, xacc: int, yacc: int, zacc: int, xgyro: int, ygyro: int, zgyro: int, xmag: int, ymag: int, zmag: int, temperature: int = 0, force_mavlink1: bool = False) -> None:
        """
        The RAW IMU readings for 3rd 9DOF sensor setup. This message should
        contain the scaled values to the described units

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        xacc                      : X acceleration [mG] (type:int16_t)
        yacc                      : Y acceleration [mG] (type:int16_t)
        zacc                      : Z acceleration [mG] (type:int16_t)
        xgyro                     : Angular speed around X axis [mrad/s] (type:int16_t)
        ygyro                     : Angular speed around Y axis [mrad/s] (type:int16_t)
        zgyro                     : Angular speed around Z axis [mrad/s] (type:int16_t)
        xmag                      : X Magnetic field [mgauss] (type:int16_t)
        ymag                      : Y Magnetic field [mgauss] (type:int16_t)
        zmag                      : Z Magnetic field [mgauss] (type:int16_t)
        temperature               : Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). [cdegC] (type:int16_t)

        """
        self.send(self.scaled_imu3_encode(time_boot_ms, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, temperature), force_mavlink1=force_mavlink1)

## data_transmission_handshake_encode
    def data_transmission_handshake_encode(self, type: int, size: int, width: int, height: int, packets: int, payload: int, jpg_quality: int) -> MAVLink_data_transmission_handshake_message:
        """
        Handshake message to initiate, control and stop image streaming when
        using the Image Transmission Protocol:
        https://mavlink.io/en/services/image_transmission.html.

        type                      : Type of requested/acknowledged data. (type:uint8_t, values:MAVLINK_DATA_STREAM_TYPE)
        size                      : total data size (set on ACK only). [bytes] (type:uint32_t)
        width                     : Width of a matrix or image. (type:uint16_t)
        height                    : Height of a matrix or image. (type:uint16_t)
        packets                   : Number of packets being sent (set on ACK only). (type:uint16_t)
        payload                   : Payload size per packet (normally 253 byte, see DATA field size in message ENCAPSULATED_DATA) (set on ACK only). [bytes] (type:uint8_t)
        jpg_quality               : JPEG quality. Values: [1-100]. [%] (type:uint8_t)

        """
        return MAVLink_data_transmission_handshake_message(type, size, width, height, packets, payload, jpg_quality)

## data_transmission_handshake_send
    def data_transmission_handshake_send(self, type: int, size: int, width: int, height: int, packets: int, payload: int, jpg_quality: int, force_mavlink1: bool = False) -> None:
        """
        Handshake message to initiate, control and stop image streaming when
        using the Image Transmission Protocol:
        https://mavlink.io/en/services/image_transmission.html.

        type                      : Type of requested/acknowledged data. (type:uint8_t, values:MAVLINK_DATA_STREAM_TYPE)
        size                      : total data size (set on ACK only). [bytes] (type:uint32_t)
        width                     : Width of a matrix or image. (type:uint16_t)
        height                    : Height of a matrix or image. (type:uint16_t)
        packets                   : Number of packets being sent (set on ACK only). (type:uint16_t)
        payload                   : Payload size per packet (normally 253 byte, see DATA field size in message ENCAPSULATED_DATA) (set on ACK only). [bytes] (type:uint8_t)
        jpg_quality               : JPEG quality. Values: [1-100]. [%] (type:uint8_t)

        """
        self.send(self.data_transmission_handshake_encode(type, size, width, height, packets, payload, jpg_quality), force_mavlink1=force_mavlink1)

## encapsulated_data_encode
    def encapsulated_data_encode(self, seqnr: int, data: Sequence[int]) -> MAVLink_encapsulated_data_message:
        """
        Data packet for images sent using the Image Transmission Protocol:
        https://mavlink.io/en/services/image_transmission.html.

        seqnr                     : sequence number (starting with 0 on every transmission) (type:uint16_t)
        data                      : image data bytes (type:uint8_t)

        """
        return MAVLink_encapsulated_data_message(seqnr, data)

## encapsulated_data_send
    def encapsulated_data_send(self, seqnr: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Data packet for images sent using the Image Transmission Protocol:
        https://mavlink.io/en/services/image_transmission.html.

        seqnr                     : sequence number (starting with 0 on every transmission) (type:uint16_t)
        data                      : image data bytes (type:uint8_t)

        """
        self.send(self.encapsulated_data_encode(seqnr, data), force_mavlink1=force_mavlink1)

## distance_sensor_encode
    def distance_sensor_encode(self, time_boot_ms: int, min_distance: int, max_distance: int, current_distance: int, type: int, id: int, orientation: int, covariance: int, horizontal_fov: float = 0, vertical_fov: float = 0, quaternion: Sequence[float] = (0, 0, 0, 0), signal_quality: int = 0) -> MAVLink_distance_sensor_message:
        """
        Distance sensor information for an onboard rangefinder.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        min_distance              : Minimum distance the sensor can measure [cm] (type:uint16_t)
        max_distance              : Maximum distance the sensor can measure [cm] (type:uint16_t)
        current_distance          : Current distance reading [cm] (type:uint16_t)
        type                      : Type of distance sensor. (type:uint8_t, values:MAV_DISTANCE_SENSOR)
        id                        : Onboard ID of the sensor (type:uint8_t)
        orientation               : Direction the sensor faces. downward-facing: ROTATION_PITCH_270, upward-facing: ROTATION_PITCH_90, backward-facing: ROTATION_PITCH_180, forward-facing: ROTATION_NONE, left-facing: ROTATION_YAW_90, right-facing: ROTATION_YAW_270 (type:uint8_t, values:MAV_SENSOR_ORIENTATION)
        covariance                : Measurement variance. Max standard deviation is 6cm. UINT8_MAX if unknown. [cm^2] (type:uint8_t)
        horizontal_fov            : Horizontal Field of View (angle) where the distance measurement is valid and the field of view is known. Otherwise this is set to 0. [rad] (type:float)
        vertical_fov              : Vertical Field of View (angle) where the distance measurement is valid and the field of view is known. Otherwise this is set to 0. [rad] (type:float)
        quaternion                : Quaternion of the sensor orientation in vehicle body frame (w, x, y, z order, zero-rotation is 1, 0, 0, 0). Zero-rotation is along the vehicle body x-axis. This field is required if the orientation is set to MAV_SENSOR_ROTATION_CUSTOM. Set it to 0 if invalid." (type:float)
        signal_quality            : Signal quality of the sensor. Specific to each sensor type, representing the relation of the signal strength with the target reflectivity, distance, size or aspect, but normalised as a percentage. 0 = unknown/unset signal quality, 1 = invalid signal, 100 = perfect signal. [%] (type:uint8_t)

        """
        return MAVLink_distance_sensor_message(time_boot_ms, min_distance, max_distance, current_distance, type, id, orientation, covariance, horizontal_fov, vertical_fov, quaternion, signal_quality)

## distance_sensor_send
    def distance_sensor_send(self, time_boot_ms: int, min_distance: int, max_distance: int, current_distance: int, type: int, id: int, orientation: int, covariance: int, horizontal_fov: float = 0, vertical_fov: float = 0, quaternion: Sequence[float] = (0, 0, 0, 0), signal_quality: int = 0, force_mavlink1: bool = False) -> None:
        """
        Distance sensor information for an onboard rangefinder.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        min_distance              : Minimum distance the sensor can measure [cm] (type:uint16_t)
        max_distance              : Maximum distance the sensor can measure [cm] (type:uint16_t)
        current_distance          : Current distance reading [cm] (type:uint16_t)
        type                      : Type of distance sensor. (type:uint8_t, values:MAV_DISTANCE_SENSOR)
        id                        : Onboard ID of the sensor (type:uint8_t)
        orientation               : Direction the sensor faces. downward-facing: ROTATION_PITCH_270, upward-facing: ROTATION_PITCH_90, backward-facing: ROTATION_PITCH_180, forward-facing: ROTATION_NONE, left-facing: ROTATION_YAW_90, right-facing: ROTATION_YAW_270 (type:uint8_t, values:MAV_SENSOR_ORIENTATION)
        covariance                : Measurement variance. Max standard deviation is 6cm. UINT8_MAX if unknown. [cm^2] (type:uint8_t)
        horizontal_fov            : Horizontal Field of View (angle) where the distance measurement is valid and the field of view is known. Otherwise this is set to 0. [rad] (type:float)
        vertical_fov              : Vertical Field of View (angle) where the distance measurement is valid and the field of view is known. Otherwise this is set to 0. [rad] (type:float)
        quaternion                : Quaternion of the sensor orientation in vehicle body frame (w, x, y, z order, zero-rotation is 1, 0, 0, 0). Zero-rotation is along the vehicle body x-axis. This field is required if the orientation is set to MAV_SENSOR_ROTATION_CUSTOM. Set it to 0 if invalid." (type:float)
        signal_quality            : Signal quality of the sensor. Specific to each sensor type, representing the relation of the signal strength with the target reflectivity, distance, size or aspect, but normalised as a percentage. 0 = unknown/unset signal quality, 1 = invalid signal, 100 = perfect signal. [%] (type:uint8_t)

        """
        self.send(self.distance_sensor_encode(time_boot_ms, min_distance, max_distance, current_distance, type, id, orientation, covariance, horizontal_fov, vertical_fov, quaternion, signal_quality), force_mavlink1=force_mavlink1)

## terrain_request_encode
    def terrain_request_encode(self, lat: int, lon: int, grid_spacing: int, mask: int) -> MAVLink_terrain_request_message:
        """
        Request for terrain data and terrain status. See terrain protocol
        docs: https://mavlink.io/en/services/terrain.html

        lat                       : Latitude of SW corner of first grid [degE7] (type:int32_t)
        lon                       : Longitude of SW corner of first grid [degE7] (type:int32_t)
        grid_spacing              : Grid spacing [m] (type:uint16_t)
        mask                      : Bitmask of requested 4x4 grids (row major 8x7 array of grids, 56 bits) (type:uint64_t)

        """
        return MAVLink_terrain_request_message(lat, lon, grid_spacing, mask)

## terrain_request_send
    def terrain_request_send(self, lat: int, lon: int, grid_spacing: int, mask: int, force_mavlink1: bool = False) -> None:
        """
        Request for terrain data and terrain status. See terrain protocol
        docs: https://mavlink.io/en/services/terrain.html

        lat                       : Latitude of SW corner of first grid [degE7] (type:int32_t)
        lon                       : Longitude of SW corner of first grid [degE7] (type:int32_t)
        grid_spacing              : Grid spacing [m] (type:uint16_t)
        mask                      : Bitmask of requested 4x4 grids (row major 8x7 array of grids, 56 bits) (type:uint64_t)

        """
        self.send(self.terrain_request_encode(lat, lon, grid_spacing, mask), force_mavlink1=force_mavlink1)

## terrain_data_encode
    def terrain_data_encode(self, lat: int, lon: int, grid_spacing: int, gridbit: int, data: Sequence[int]) -> MAVLink_terrain_data_message:
        """
        Terrain data sent from GCS. The lat/lon and grid_spacing must be the
        same as a lat/lon from a TERRAIN_REQUEST. See terrain protocol
        docs: https://mavlink.io/en/services/terrain.html

        lat                       : Latitude of SW corner of first grid [degE7] (type:int32_t)
        lon                       : Longitude of SW corner of first grid [degE7] (type:int32_t)
        grid_spacing              : Grid spacing [m] (type:uint16_t)
        gridbit                   : bit within the terrain request mask (type:uint8_t)
        data                      : Terrain data MSL [m] (type:int16_t)

        """
        return MAVLink_terrain_data_message(lat, lon, grid_spacing, gridbit, data)

## terrain_data_send
    def terrain_data_send(self, lat: int, lon: int, grid_spacing: int, gridbit: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Terrain data sent from GCS. The lat/lon and grid_spacing must be the
        same as a lat/lon from a TERRAIN_REQUEST. See terrain protocol
        docs: https://mavlink.io/en/services/terrain.html

        lat                       : Latitude of SW corner of first grid [degE7] (type:int32_t)
        lon                       : Longitude of SW corner of first grid [degE7] (type:int32_t)
        grid_spacing              : Grid spacing [m] (type:uint16_t)
        gridbit                   : bit within the terrain request mask (type:uint8_t)
        data                      : Terrain data MSL [m] (type:int16_t)

        """
        self.send(self.terrain_data_encode(lat, lon, grid_spacing, gridbit, data), force_mavlink1=force_mavlink1)

## terrain_check_encode
    def terrain_check_encode(self, lat: int, lon: int) -> MAVLink_terrain_check_message:
        """
        Request that the vehicle report terrain height at the given location
        (expected response is a TERRAIN_REPORT). Used by GCS to check
        if vehicle has all terrain data needed for a mission.

        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)

        """
        return MAVLink_terrain_check_message(lat, lon)

## terrain_check_send
    def terrain_check_send(self, lat: int, lon: int, force_mavlink1: bool = False) -> None:
        """
        Request that the vehicle report terrain height at the given location
        (expected response is a TERRAIN_REPORT). Used by GCS to check
        if vehicle has all terrain data needed for a mission.

        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)

        """
        self.send(self.terrain_check_encode(lat, lon), force_mavlink1=force_mavlink1)

## terrain_report_encode
    def terrain_report_encode(self, lat: int, lon: int, spacing: int, terrain_height: float, current_height: float, pending: int, loaded: int) -> MAVLink_terrain_report_message:
        """
        Streamed from drone to report progress of terrain map download
        (initiated by TERRAIN_REQUEST), or sent as a response to a
        TERRAIN_CHECK request. See terrain protocol docs:
        https://mavlink.io/en/services/terrain.html

        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        spacing                   : grid spacing (zero if terrain at this location unavailable) (type:uint16_t)
        terrain_height            : Terrain height MSL [m] (type:float)
        current_height            : Current vehicle height above lat/lon terrain height [m] (type:float)
        pending                   : Number of 4x4 terrain blocks waiting to be received or read from disk (type:uint16_t)
        loaded                    : Number of 4x4 terrain blocks in memory (type:uint16_t)

        """
        return MAVLink_terrain_report_message(lat, lon, spacing, terrain_height, current_height, pending, loaded)

## terrain_report_send
    def terrain_report_send(self, lat: int, lon: int, spacing: int, terrain_height: float, current_height: float, pending: int, loaded: int, force_mavlink1: bool = False) -> None:
        """
        Streamed from drone to report progress of terrain map download
        (initiated by TERRAIN_REQUEST), or sent as a response to a
        TERRAIN_CHECK request. See terrain protocol docs:
        https://mavlink.io/en/services/terrain.html

        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        spacing                   : grid spacing (zero if terrain at this location unavailable) (type:uint16_t)
        terrain_height            : Terrain height MSL [m] (type:float)
        current_height            : Current vehicle height above lat/lon terrain height [m] (type:float)
        pending                   : Number of 4x4 terrain blocks waiting to be received or read from disk (type:uint16_t)
        loaded                    : Number of 4x4 terrain blocks in memory (type:uint16_t)

        """
        self.send(self.terrain_report_encode(lat, lon, spacing, terrain_height, current_height, pending, loaded), force_mavlink1=force_mavlink1)

## scaled_pressure2_encode
    def scaled_pressure2_encode(self, time_boot_ms: int, press_abs: float, press_diff: float, temperature: int, temperature_press_diff: int = 0) -> MAVLink_scaled_pressure2_message:
        """
        Barometer readings for 2nd barometer

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        press_abs                 : Absolute pressure [hPa] (type:float)
        press_diff                : Differential pressure [hPa] (type:float)
        temperature               : Absolute pressure temperature [cdegC] (type:int16_t)
        temperature_press_diff        : Differential pressure temperature (0, if not available). Report values of 0 (or 1) as 1 cdegC. [cdegC] (type:int16_t)

        """
        return MAVLink_scaled_pressure2_message(time_boot_ms, press_abs, press_diff, temperature, temperature_press_diff)

## scaled_pressure2_send
    def scaled_pressure2_send(self, time_boot_ms: int, press_abs: float, press_diff: float, temperature: int, temperature_press_diff: int = 0, force_mavlink1: bool = False) -> None:
        """
        Barometer readings for 2nd barometer

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        press_abs                 : Absolute pressure [hPa] (type:float)
        press_diff                : Differential pressure [hPa] (type:float)
        temperature               : Absolute pressure temperature [cdegC] (type:int16_t)
        temperature_press_diff        : Differential pressure temperature (0, if not available). Report values of 0 (or 1) as 1 cdegC. [cdegC] (type:int16_t)

        """
        self.send(self.scaled_pressure2_encode(time_boot_ms, press_abs, press_diff, temperature, temperature_press_diff), force_mavlink1=force_mavlink1)

## att_pos_mocap_encode
    def att_pos_mocap_encode(self, time_usec: int, q: Sequence[float], x: float, y: float, z: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)) -> MAVLink_att_pos_mocap_message:
        """
        Motion capture attitude and position

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        q                         : Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        x                         : X position (NED) [m] (type:float)
        y                         : Y position (NED) [m] (type:float)
        z                         : Z position (NED) [m] (type:float)
        covariance                : Row-major representation of a pose 6x6 cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        return MAVLink_att_pos_mocap_message(time_usec, q, x, y, z, covariance)

## att_pos_mocap_send
    def att_pos_mocap_send(self, time_usec: int, q: Sequence[float], x: float, y: float, z: float, covariance: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), force_mavlink1: bool = False) -> None:
        """
        Motion capture attitude and position

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        q                         : Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        x                         : X position (NED) [m] (type:float)
        y                         : Y position (NED) [m] (type:float)
        z                         : Z position (NED) [m] (type:float)
        covariance                : Row-major representation of a pose 6x6 cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)

        """
        self.send(self.att_pos_mocap_encode(time_usec, q, x, y, z, covariance), force_mavlink1=force_mavlink1)

## set_actuator_control_target_encode
    def set_actuator_control_target_encode(self, time_usec: int, group_mlx: int, target_system: int, target_component: int, controls: Sequence[float]) -> MAVLink_set_actuator_control_target_message:
        """
        Set the vehicle attitude and body angular rates.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        group_mlx                 : Actuator group. The "_mlx" indicates this is a multi-instance message and a MAVLink parser should use this field to difference between instances. (type:uint8_t)
        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        controls                  : Actuator controls. Normed to -1..+1 where 0 is neutral position. Throttle for single rotation direction motors is 0..1, negative range for reverse direction. Standard mapping for attitude controls (group 0): (index 0-7): roll, pitch, yaw, throttle, flaps, spoilers, airbrakes, landing gear. Load a pass-through mixer to repurpose them as generic outputs. (type:float)

        """
        return MAVLink_set_actuator_control_target_message(time_usec, group_mlx, target_system, target_component, controls)

## set_actuator_control_target_send
    def set_actuator_control_target_send(self, time_usec: int, group_mlx: int, target_system: int, target_component: int, controls: Sequence[float], force_mavlink1: bool = False) -> None:
        """
        Set the vehicle attitude and body angular rates.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        group_mlx                 : Actuator group. The "_mlx" indicates this is a multi-instance message and a MAVLink parser should use this field to difference between instances. (type:uint8_t)
        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        controls                  : Actuator controls. Normed to -1..+1 where 0 is neutral position. Throttle for single rotation direction motors is 0..1, negative range for reverse direction. Standard mapping for attitude controls (group 0): (index 0-7): roll, pitch, yaw, throttle, flaps, spoilers, airbrakes, landing gear. Load a pass-through mixer to repurpose them as generic outputs. (type:float)

        """
        self.send(self.set_actuator_control_target_encode(time_usec, group_mlx, target_system, target_component, controls), force_mavlink1=force_mavlink1)

## actuator_control_target_encode
    def actuator_control_target_encode(self, time_usec: int, group_mlx: int, controls: Sequence[float]) -> MAVLink_actuator_control_target_message:
        """
        Set the vehicle attitude and body angular rates.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        group_mlx                 : Actuator group. The "_mlx" indicates this is a multi-instance message and a MAVLink parser should use this field to difference between instances. (type:uint8_t)
        controls                  : Actuator controls. Normed to -1..+1 where 0 is neutral position. Throttle for single rotation direction motors is 0..1, negative range for reverse direction. Standard mapping for attitude controls (group 0): (index 0-7): roll, pitch, yaw, throttle, flaps, spoilers, airbrakes, landing gear. Load a pass-through mixer to repurpose them as generic outputs. (type:float)

        """
        return MAVLink_actuator_control_target_message(time_usec, group_mlx, controls)

## actuator_control_target_send
    def actuator_control_target_send(self, time_usec: int, group_mlx: int, controls: Sequence[float], force_mavlink1: bool = False) -> None:
        """
        Set the vehicle attitude and body angular rates.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        group_mlx                 : Actuator group. The "_mlx" indicates this is a multi-instance message and a MAVLink parser should use this field to difference between instances. (type:uint8_t)
        controls                  : Actuator controls. Normed to -1..+1 where 0 is neutral position. Throttle for single rotation direction motors is 0..1, negative range for reverse direction. Standard mapping for attitude controls (group 0): (index 0-7): roll, pitch, yaw, throttle, flaps, spoilers, airbrakes, landing gear. Load a pass-through mixer to repurpose them as generic outputs. (type:float)

        """
        self.send(self.actuator_control_target_encode(time_usec, group_mlx, controls), force_mavlink1=force_mavlink1)

## altitude_encode
    def altitude_encode(self, time_usec: int, altitude_monotonic: float, altitude_amsl: float, altitude_local: float, altitude_relative: float, altitude_terrain: float, bottom_clearance: float) -> MAVLink_altitude_message:
        """
        The current system altitude.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        altitude_monotonic        : This altitude measure is initialized on system boot and monotonic (it is never reset, but represents the local altitude change). The only guarantee on this field is that it will never be reset and is consistent within a flight. The recommended value for this field is the uncorrected barometric altitude at boot time. This altitude will also drift and vary between flights. [m] (type:float)
        altitude_amsl             : This altitude measure is strictly above mean sea level and might be non-monotonic (it might reset on events like GPS lock or when a new QNH value is set). It should be the altitude to which global altitude waypoints are compared to. Note that it is *not* the GPS altitude, however, most GPS modules already output MSL by default and not the WGS84 altitude. [m] (type:float)
        altitude_local            : This is the local altitude in the local coordinate frame. It is not the altitude above home, but in reference to the coordinate origin (0, 0, 0). It is up-positive. [m] (type:float)
        altitude_relative         : This is the altitude above the home position. It resets on each change of the current home position. [m] (type:float)
        altitude_terrain          : This is the altitude above terrain. It might be fed by a terrain database or an altimeter. Values smaller than -1000 should be interpreted as unknown. [m] (type:float)
        bottom_clearance          : This is not the altitude, but the clear space below the system according to the fused clearance estimate. It generally should max out at the maximum range of e.g. the laser altimeter. It is generally a moving target. A negative value indicates no measurement available. [m] (type:float)

        """
        return MAVLink_altitude_message(time_usec, altitude_monotonic, altitude_amsl, altitude_local, altitude_relative, altitude_terrain, bottom_clearance)

## altitude_send
    def altitude_send(self, time_usec: int, altitude_monotonic: float, altitude_amsl: float, altitude_local: float, altitude_relative: float, altitude_terrain: float, bottom_clearance: float, force_mavlink1: bool = False) -> None:
        """
        The current system altitude.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        altitude_monotonic        : This altitude measure is initialized on system boot and monotonic (it is never reset, but represents the local altitude change). The only guarantee on this field is that it will never be reset and is consistent within a flight. The recommended value for this field is the uncorrected barometric altitude at boot time. This altitude will also drift and vary between flights. [m] (type:float)
        altitude_amsl             : This altitude measure is strictly above mean sea level and might be non-monotonic (it might reset on events like GPS lock or when a new QNH value is set). It should be the altitude to which global altitude waypoints are compared to. Note that it is *not* the GPS altitude, however, most GPS modules already output MSL by default and not the WGS84 altitude. [m] (type:float)
        altitude_local            : This is the local altitude in the local coordinate frame. It is not the altitude above home, but in reference to the coordinate origin (0, 0, 0). It is up-positive. [m] (type:float)
        altitude_relative         : This is the altitude above the home position. It resets on each change of the current home position. [m] (type:float)
        altitude_terrain          : This is the altitude above terrain. It might be fed by a terrain database or an altimeter. Values smaller than -1000 should be interpreted as unknown. [m] (type:float)
        bottom_clearance          : This is not the altitude, but the clear space below the system according to the fused clearance estimate. It generally should max out at the maximum range of e.g. the laser altimeter. It is generally a moving target. A negative value indicates no measurement available. [m] (type:float)

        """
        self.send(self.altitude_encode(time_usec, altitude_monotonic, altitude_amsl, altitude_local, altitude_relative, altitude_terrain, bottom_clearance), force_mavlink1=force_mavlink1)

## resource_request_encode
    def resource_request_encode(self, request_id: int, uri_type: int, uri: Sequence[int], transfer_type: int, storage: Sequence[int]) -> MAVLink_resource_request_message:
        """
        The autopilot is requesting a resource (file, binary, other type of
        data)

        request_id                : Request ID. This ID should be reused when sending back URI contents (type:uint8_t)
        uri_type                  : The type of requested URI. 0 = a file via URL. 1 = a UAVCAN binary (type:uint8_t)
        uri                       : The requested unique resource identifier (URI). It is not necessarily a straight domain name (depends on the URI type enum) (type:uint8_t)
        transfer_type             : The way the autopilot wants to receive the URI. 0 = MAVLink FTP. 1 = binary stream. (type:uint8_t)
        storage                   : The storage path the autopilot wants the URI to be stored in. Will only be valid if the transfer_type has a storage associated (e.g. MAVLink FTP). (type:uint8_t)

        """
        return MAVLink_resource_request_message(request_id, uri_type, uri, transfer_type, storage)

## resource_request_send
    def resource_request_send(self, request_id: int, uri_type: int, uri: Sequence[int], transfer_type: int, storage: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        The autopilot is requesting a resource (file, binary, other type of
        data)

        request_id                : Request ID. This ID should be reused when sending back URI contents (type:uint8_t)
        uri_type                  : The type of requested URI. 0 = a file via URL. 1 = a UAVCAN binary (type:uint8_t)
        uri                       : The requested unique resource identifier (URI). It is not necessarily a straight domain name (depends on the URI type enum) (type:uint8_t)
        transfer_type             : The way the autopilot wants to receive the URI. 0 = MAVLink FTP. 1 = binary stream. (type:uint8_t)
        storage                   : The storage path the autopilot wants the URI to be stored in. Will only be valid if the transfer_type has a storage associated (e.g. MAVLink FTP). (type:uint8_t)

        """
        self.send(self.resource_request_encode(request_id, uri_type, uri, transfer_type, storage), force_mavlink1=force_mavlink1)

## scaled_pressure3_encode
    def scaled_pressure3_encode(self, time_boot_ms: int, press_abs: float, press_diff: float, temperature: int, temperature_press_diff: int = 0) -> MAVLink_scaled_pressure3_message:
        """
        Barometer readings for 3rd barometer

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        press_abs                 : Absolute pressure [hPa] (type:float)
        press_diff                : Differential pressure [hPa] (type:float)
        temperature               : Absolute pressure temperature [cdegC] (type:int16_t)
        temperature_press_diff        : Differential pressure temperature (0, if not available). Report values of 0 (or 1) as 1 cdegC. [cdegC] (type:int16_t)

        """
        return MAVLink_scaled_pressure3_message(time_boot_ms, press_abs, press_diff, temperature, temperature_press_diff)

## scaled_pressure3_send
    def scaled_pressure3_send(self, time_boot_ms: int, press_abs: float, press_diff: float, temperature: int, temperature_press_diff: int = 0, force_mavlink1: bool = False) -> None:
        """
        Barometer readings for 3rd barometer

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        press_abs                 : Absolute pressure [hPa] (type:float)
        press_diff                : Differential pressure [hPa] (type:float)
        temperature               : Absolute pressure temperature [cdegC] (type:int16_t)
        temperature_press_diff        : Differential pressure temperature (0, if not available). Report values of 0 (or 1) as 1 cdegC. [cdegC] (type:int16_t)

        """
        self.send(self.scaled_pressure3_encode(time_boot_ms, press_abs, press_diff, temperature, temperature_press_diff), force_mavlink1=force_mavlink1)

## follow_target_encode
    def follow_target_encode(self, timestamp: int, est_capabilities: int, lat: int, lon: int, alt: float, vel: Sequence[float], acc: Sequence[float], attitude_q: Sequence[float], rates: Sequence[float], position_cov: Sequence[float], custom_state: int) -> MAVLink_follow_target_message:
        """
        Current motion information from a designated system

        timestamp                 : Timestamp (time since system boot). [ms] (type:uint64_t)
        est_capabilities          : bit positions for tracker reporting capabilities (POS = 0, VEL = 1, ACCEL = 2, ATT + RATES = 3) (type:uint8_t)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (MSL) [m] (type:float)
        vel                       : target velocity (0,0,0) for unknown [m/s] (type:float)
        acc                       : linear target acceleration (0,0,0) for unknown [m/s/s] (type:float)
        attitude_q                : (1 0 0 0 for unknown) (type:float)
        rates                     : (0 0 0 for unknown) (type:float)
        position_cov              : eph epv (type:float)
        custom_state              : button states or switches of a tracker device (type:uint64_t)

        """
        return MAVLink_follow_target_message(timestamp, est_capabilities, lat, lon, alt, vel, acc, attitude_q, rates, position_cov, custom_state)

## follow_target_send
    def follow_target_send(self, timestamp: int, est_capabilities: int, lat: int, lon: int, alt: float, vel: Sequence[float], acc: Sequence[float], attitude_q: Sequence[float], rates: Sequence[float], position_cov: Sequence[float], custom_state: int, force_mavlink1: bool = False) -> None:
        """
        Current motion information from a designated system

        timestamp                 : Timestamp (time since system boot). [ms] (type:uint64_t)
        est_capabilities          : bit positions for tracker reporting capabilities (POS = 0, VEL = 1, ACCEL = 2, ATT + RATES = 3) (type:uint8_t)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (MSL) [m] (type:float)
        vel                       : target velocity (0,0,0) for unknown [m/s] (type:float)
        acc                       : linear target acceleration (0,0,0) for unknown [m/s/s] (type:float)
        attitude_q                : (1 0 0 0 for unknown) (type:float)
        rates                     : (0 0 0 for unknown) (type:float)
        position_cov              : eph epv (type:float)
        custom_state              : button states or switches of a tracker device (type:uint64_t)

        """
        self.send(self.follow_target_encode(timestamp, est_capabilities, lat, lon, alt, vel, acc, attitude_q, rates, position_cov, custom_state), force_mavlink1=force_mavlink1)

## control_system_state_encode
    def control_system_state_encode(self, time_usec: int, x_acc: float, y_acc: float, z_acc: float, x_vel: float, y_vel: float, z_vel: float, x_pos: float, y_pos: float, z_pos: float, airspeed: float, vel_variance: Sequence[float], pos_variance: Sequence[float], q: Sequence[float], roll_rate: float, pitch_rate: float, yaw_rate: float) -> MAVLink_control_system_state_message:
        """
        The smoothed, monotonic system state used to feed the control loops of
        the system.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        x_acc                     : X acceleration in body frame [m/s/s] (type:float)
        y_acc                     : Y acceleration in body frame [m/s/s] (type:float)
        z_acc                     : Z acceleration in body frame [m/s/s] (type:float)
        x_vel                     : X velocity in body frame [m/s] (type:float)
        y_vel                     : Y velocity in body frame [m/s] (type:float)
        z_vel                     : Z velocity in body frame [m/s] (type:float)
        x_pos                     : X position in local frame [m] (type:float)
        y_pos                     : Y position in local frame [m] (type:float)
        z_pos                     : Z position in local frame [m] (type:float)
        airspeed                  : Airspeed, set to -1 if unknown [m/s] (type:float)
        vel_variance              : Variance of body velocity estimate (type:float)
        pos_variance              : Variance in local position (type:float)
        q                         : The attitude, represented as Quaternion (type:float)
        roll_rate                 : Angular rate in roll axis [rad/s] (type:float)
        pitch_rate                : Angular rate in pitch axis [rad/s] (type:float)
        yaw_rate                  : Angular rate in yaw axis [rad/s] (type:float)

        """
        return MAVLink_control_system_state_message(time_usec, x_acc, y_acc, z_acc, x_vel, y_vel, z_vel, x_pos, y_pos, z_pos, airspeed, vel_variance, pos_variance, q, roll_rate, pitch_rate, yaw_rate)

## control_system_state_send
    def control_system_state_send(self, time_usec: int, x_acc: float, y_acc: float, z_acc: float, x_vel: float, y_vel: float, z_vel: float, x_pos: float, y_pos: float, z_pos: float, airspeed: float, vel_variance: Sequence[float], pos_variance: Sequence[float], q: Sequence[float], roll_rate: float, pitch_rate: float, yaw_rate: float, force_mavlink1: bool = False) -> None:
        """
        The smoothed, monotonic system state used to feed the control loops of
        the system.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        x_acc                     : X acceleration in body frame [m/s/s] (type:float)
        y_acc                     : Y acceleration in body frame [m/s/s] (type:float)
        z_acc                     : Z acceleration in body frame [m/s/s] (type:float)
        x_vel                     : X velocity in body frame [m/s] (type:float)
        y_vel                     : Y velocity in body frame [m/s] (type:float)
        z_vel                     : Z velocity in body frame [m/s] (type:float)
        x_pos                     : X position in local frame [m] (type:float)
        y_pos                     : Y position in local frame [m] (type:float)
        z_pos                     : Z position in local frame [m] (type:float)
        airspeed                  : Airspeed, set to -1 if unknown [m/s] (type:float)
        vel_variance              : Variance of body velocity estimate (type:float)
        pos_variance              : Variance in local position (type:float)
        q                         : The attitude, represented as Quaternion (type:float)
        roll_rate                 : Angular rate in roll axis [rad/s] (type:float)
        pitch_rate                : Angular rate in pitch axis [rad/s] (type:float)
        yaw_rate                  : Angular rate in yaw axis [rad/s] (type:float)

        """
        self.send(self.control_system_state_encode(time_usec, x_acc, y_acc, z_acc, x_vel, y_vel, z_vel, x_pos, y_pos, z_pos, airspeed, vel_variance, pos_variance, q, roll_rate, pitch_rate, yaw_rate), force_mavlink1=force_mavlink1)

## battery_status_encode
    def battery_status_encode(self, id: int, battery_function: int, type: int, temperature: int, voltages: Sequence[int], current_battery: int, current_consumed: int, energy_consumed: int, battery_remaining: int, time_remaining: int = 0, charge_state: int = 0, voltages_ext: Sequence[int] = (0, 0, 0, 0), mode: int = 0, fault_bitmask: int = 0) -> MAVLink_battery_status_message:
        """
        Battery information

        id                        : Battery ID (type:uint8_t)
        battery_function          : Function of the battery (type:uint8_t, values:MAV_BATTERY_FUNCTION)
        type                      : Type (chemistry) of the battery (type:uint8_t, values:MAV_BATTERY_TYPE)
        temperature               : Temperature of the battery. INT16_MAX for unknown temperature. [cdegC] (type:int16_t)
        voltages                  : Battery voltage of cells 1 to 10 (see voltages_ext for cells 11-14). Cells in this field above the valid cell count for this battery should have the UINT16_MAX value. If individual cell voltages are unknown or not measured for this battery, then the overall battery voltage should be filled in cell 0, with all others set to UINT16_MAX. If the voltage of the battery is greater than (UINT16_MAX - 1), then cell 0 should be set to (UINT16_MAX - 1), and cell 1 to the remaining voltage. This can be extended to multiple cells if the total voltage is greater than 2 * (UINT16_MAX - 1). [mV] (type:uint16_t)
        current_battery           : Battery current, -1: autopilot does not measure the current [cA] (type:int16_t)
        current_consumed          : Consumed charge, -1: autopilot does not provide consumption estimate [mAh] (type:int32_t)
        energy_consumed           : Consumed energy, -1: autopilot does not provide energy consumption estimate [hJ] (type:int32_t)
        battery_remaining         : Remaining battery energy. Values: [0-100], -1: autopilot does not estimate the remaining battery. [%] (type:int8_t)
        time_remaining            : Remaining battery time, 0: autopilot does not provide remaining battery time estimate [s] (type:int32_t)
        charge_state              : State for extent of discharge, provided by autopilot for warning or external reactions (type:uint8_t, values:MAV_BATTERY_CHARGE_STATE)
        voltages_ext              : Battery voltages for cells 11 to 14. Cells above the valid cell count for this battery should have a value of 0, where zero indicates not supported (note, this is different than for the voltages field and allows empty byte truncation). If the measured value is 0 then 1 should be sent instead. [mV] (type:uint16_t)
        mode                      : Battery mode. Default (0) is that battery mode reporting is not supported or battery is in normal-use mode. (type:uint8_t, values:MAV_BATTERY_MODE)
        fault_bitmask             : Fault/health indications. These should be set when charge_state is MAV_BATTERY_CHARGE_STATE_FAILED or MAV_BATTERY_CHARGE_STATE_UNHEALTHY (if not, fault reporting is not supported). (type:uint32_t, values:MAV_BATTERY_FAULT)

        """
        return MAVLink_battery_status_message(id, battery_function, type, temperature, voltages, current_battery, current_consumed, energy_consumed, battery_remaining, time_remaining, charge_state, voltages_ext, mode, fault_bitmask)

## battery_status_send
    def battery_status_send(self, id: int, battery_function: int, type: int, temperature: int, voltages: Sequence[int], current_battery: int, current_consumed: int, energy_consumed: int, battery_remaining: int, time_remaining: int = 0, charge_state: int = 0, voltages_ext: Sequence[int] = (0, 0, 0, 0), mode: int = 0, fault_bitmask: int = 0, force_mavlink1: bool = False) -> None:
        """
        Battery information

        id                        : Battery ID (type:uint8_t)
        battery_function          : Function of the battery (type:uint8_t, values:MAV_BATTERY_FUNCTION)
        type                      : Type (chemistry) of the battery (type:uint8_t, values:MAV_BATTERY_TYPE)
        temperature               : Temperature of the battery. INT16_MAX for unknown temperature. [cdegC] (type:int16_t)
        voltages                  : Battery voltage of cells 1 to 10 (see voltages_ext for cells 11-14). Cells in this field above the valid cell count for this battery should have the UINT16_MAX value. If individual cell voltages are unknown or not measured for this battery, then the overall battery voltage should be filled in cell 0, with all others set to UINT16_MAX. If the voltage of the battery is greater than (UINT16_MAX - 1), then cell 0 should be set to (UINT16_MAX - 1), and cell 1 to the remaining voltage. This can be extended to multiple cells if the total voltage is greater than 2 * (UINT16_MAX - 1). [mV] (type:uint16_t)
        current_battery           : Battery current, -1: autopilot does not measure the current [cA] (type:int16_t)
        current_consumed          : Consumed charge, -1: autopilot does not provide consumption estimate [mAh] (type:int32_t)
        energy_consumed           : Consumed energy, -1: autopilot does not provide energy consumption estimate [hJ] (type:int32_t)
        battery_remaining         : Remaining battery energy. Values: [0-100], -1: autopilot does not estimate the remaining battery. [%] (type:int8_t)
        time_remaining            : Remaining battery time, 0: autopilot does not provide remaining battery time estimate [s] (type:int32_t)
        charge_state              : State for extent of discharge, provided by autopilot for warning or external reactions (type:uint8_t, values:MAV_BATTERY_CHARGE_STATE)
        voltages_ext              : Battery voltages for cells 11 to 14. Cells above the valid cell count for this battery should have a value of 0, where zero indicates not supported (note, this is different than for the voltages field and allows empty byte truncation). If the measured value is 0 then 1 should be sent instead. [mV] (type:uint16_t)
        mode                      : Battery mode. Default (0) is that battery mode reporting is not supported or battery is in normal-use mode. (type:uint8_t, values:MAV_BATTERY_MODE)
        fault_bitmask             : Fault/health indications. These should be set when charge_state is MAV_BATTERY_CHARGE_STATE_FAILED or MAV_BATTERY_CHARGE_STATE_UNHEALTHY (if not, fault reporting is not supported). (type:uint32_t, values:MAV_BATTERY_FAULT)

        """
        self.send(self.battery_status_encode(id, battery_function, type, temperature, voltages, current_battery, current_consumed, energy_consumed, battery_remaining, time_remaining, charge_state, voltages_ext, mode, fault_bitmask), force_mavlink1=force_mavlink1)

## autopilot_version_encode
    def autopilot_version_encode(self, capabilities: int, flight_sw_version: int, middleware_sw_version: int, os_sw_version: int, board_version: int, flight_custom_version: Sequence[int], middleware_custom_version: Sequence[int], os_custom_version: Sequence[int], vendor_id: int, product_id: int, uid: int, uid2: Sequence[int] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)) -> MAVLink_autopilot_version_message:
        """
        Version and capability of autopilot software. This should be emitted
        in response to a request with MAV_CMD_REQUEST_MESSAGE.

        capabilities              : Bitmap of capabilities (type:uint64_t, values:MAV_PROTOCOL_CAPABILITY)
        flight_sw_version         : Firmware version number.
        The field must be encoded as 4 bytes, where each byte (shown from MSB to LSB) is part of a semantic version: (major) (minor) (patch) (FIRMWARE_VERSION_TYPE). (type:uint32_t)
        middleware_sw_version        : Middleware version number (type:uint32_t)
        os_sw_version             : Operating system version number (type:uint32_t)
        board_version             : HW / board version (last 8 bits should be silicon ID, if any). The first 16 bits of this field specify https://github.com/PX4/PX4-Bootloader/blob/master/board_types.txt (and extended extensively in https://github.com/ardupilot/ardupilot/blob/master/Tools/AP_Bootloader/board_types.txt) (type:uint32_t)
        flight_custom_version        : Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. (type:uint8_t)
        middleware_custom_version        : Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. (type:uint8_t)
        os_custom_version         : Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. (type:uint8_t)
        vendor_id                 : ID of the board vendor (type:uint16_t)
        product_id                : ID of the product (type:uint16_t)
        uid                       : UID if provided by hardware (see uid2) (type:uint64_t)
        uid2                      : UID if provided by hardware (supersedes the uid field. If this is non-zero, use this field, otherwise use uid) (type:uint8_t)

        """
        return MAVLink_autopilot_version_message(capabilities, flight_sw_version, middleware_sw_version, os_sw_version, board_version, flight_custom_version, middleware_custom_version, os_custom_version, vendor_id, product_id, uid, uid2)

## autopilot_version_send
    def autopilot_version_send(self, capabilities: int, flight_sw_version: int, middleware_sw_version: int, os_sw_version: int, board_version: int, flight_custom_version: Sequence[int], middleware_custom_version: Sequence[int], os_custom_version: Sequence[int], vendor_id: int, product_id: int, uid: int, uid2: Sequence[int] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), force_mavlink1: bool = False) -> None:
        """
        Version and capability of autopilot software. This should be emitted
        in response to a request with MAV_CMD_REQUEST_MESSAGE.

        capabilities              : Bitmap of capabilities (type:uint64_t, values:MAV_PROTOCOL_CAPABILITY)
        flight_sw_version         : Firmware version number.
        The field must be encoded as 4 bytes, where each byte (shown from MSB to LSB) is part of a semantic version: (major) (minor) (patch) (FIRMWARE_VERSION_TYPE). (type:uint32_t)
        middleware_sw_version        : Middleware version number (type:uint32_t)
        os_sw_version             : Operating system version number (type:uint32_t)
        board_version             : HW / board version (last 8 bits should be silicon ID, if any). The first 16 bits of this field specify https://github.com/PX4/PX4-Bootloader/blob/master/board_types.txt (and extended extensively in https://github.com/ardupilot/ardupilot/blob/master/Tools/AP_Bootloader/board_types.txt) (type:uint32_t)
        flight_custom_version        : Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. (type:uint8_t)
        middleware_custom_version        : Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. (type:uint8_t)
        os_custom_version         : Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. (type:uint8_t)
        vendor_id                 : ID of the board vendor (type:uint16_t)
        product_id                : ID of the product (type:uint16_t)
        uid                       : UID if provided by hardware (see uid2) (type:uint64_t)
        uid2                      : UID if provided by hardware (supersedes the uid field. If this is non-zero, use this field, otherwise use uid) (type:uint8_t)

        """
        self.send(self.autopilot_version_encode(capabilities, flight_sw_version, middleware_sw_version, os_sw_version, board_version, flight_custom_version, middleware_custom_version, os_custom_version, vendor_id, product_id, uid, uid2), force_mavlink1=force_mavlink1)

## landing_target_encode
    def landing_target_encode(self, time_usec: int, target_num: int, frame: int, angle_x: float, angle_y: float, distance: float, size_x: float, size_y: float, x: float = 0, y: float = 0, z: float = 0, q: Sequence[float] = (0, 0, 0, 0), type: int = 0, position_valid: int = 0) -> MAVLink_landing_target_message:
        """
        The location of a landing target. See:
        https://mavlink.io/en/services/landing_target.html

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        target_num                : The ID of the target if multiple targets are present (type:uint8_t)
        frame                     : Coordinate frame used for following fields. (type:uint8_t, values:MAV_FRAME)
        angle_x                   : X-axis angular offset of the target from the center of the image [rad] (type:float)
        angle_y                   : Y-axis angular offset of the target from the center of the image [rad] (type:float)
        distance                  : Distance to the target from the vehicle [m] (type:float)
        size_x                    : Size of target along x-axis [rad] (type:float)
        size_y                    : Size of target along y-axis [rad] (type:float)
        x                         : X Position of the landing target in MAV_FRAME [m] (type:float)
        y                         : Y Position of the landing target in MAV_FRAME [m] (type:float)
        z                         : Z Position of the landing target in MAV_FRAME [m] (type:float)
        q                         : Quaternion of landing target orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        type                      : Type of landing target (type:uint8_t, values:LANDING_TARGET_TYPE)
        position_valid            : Position fields (x, y, z, q, type) contain valid target position information (MAV_BOOL_FALSE: invalid values). Values not equal to 0 or 1 are invalid. (type:uint8_t, values:MAV_BOOL)

        """
        return MAVLink_landing_target_message(time_usec, target_num, frame, angle_x, angle_y, distance, size_x, size_y, x, y, z, q, type, position_valid)

## landing_target_send
    def landing_target_send(self, time_usec: int, target_num: int, frame: int, angle_x: float, angle_y: float, distance: float, size_x: float, size_y: float, x: float = 0, y: float = 0, z: float = 0, q: Sequence[float] = (0, 0, 0, 0), type: int = 0, position_valid: int = 0, force_mavlink1: bool = False) -> None:
        """
        The location of a landing target. See:
        https://mavlink.io/en/services/landing_target.html

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        target_num                : The ID of the target if multiple targets are present (type:uint8_t)
        frame                     : Coordinate frame used for following fields. (type:uint8_t, values:MAV_FRAME)
        angle_x                   : X-axis angular offset of the target from the center of the image [rad] (type:float)
        angle_y                   : Y-axis angular offset of the target from the center of the image [rad] (type:float)
        distance                  : Distance to the target from the vehicle [m] (type:float)
        size_x                    : Size of target along x-axis [rad] (type:float)
        size_y                    : Size of target along y-axis [rad] (type:float)
        x                         : X Position of the landing target in MAV_FRAME [m] (type:float)
        y                         : Y Position of the landing target in MAV_FRAME [m] (type:float)
        z                         : Z Position of the landing target in MAV_FRAME [m] (type:float)
        q                         : Quaternion of landing target orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        type                      : Type of landing target (type:uint8_t, values:LANDING_TARGET_TYPE)
        position_valid            : Position fields (x, y, z, q, type) contain valid target position information (MAV_BOOL_FALSE: invalid values). Values not equal to 0 or 1 are invalid. (type:uint8_t, values:MAV_BOOL)

        """
        self.send(self.landing_target_encode(time_usec, target_num, frame, angle_x, angle_y, distance, size_x, size_y, x, y, z, q, type, position_valid), force_mavlink1=force_mavlink1)

## fence_status_encode
    def fence_status_encode(self, breach_status: int, breach_count: int, breach_type: int, breach_time: int, breach_mitigation: int = 0) -> MAVLink_fence_status_message:
        """
        Status of geo-fencing. Sent in extended status stream when fencing
        enabled.

        breach_status             : Breach status (0 if currently inside fence, 1 if outside). (type:uint8_t)
        breach_count              : Number of fence breaches. (type:uint16_t)
        breach_type               : Last breach type. (type:uint8_t, values:FENCE_BREACH)
        breach_time               : Time (since boot) of last breach. [ms] (type:uint32_t)
        breach_mitigation         : Active action to prevent fence breach (type:uint8_t, values:FENCE_MITIGATE)

        """
        return MAVLink_fence_status_message(breach_status, breach_count, breach_type, breach_time, breach_mitigation)

## fence_status_send
    def fence_status_send(self, breach_status: int, breach_count: int, breach_type: int, breach_time: int, breach_mitigation: int = 0, force_mavlink1: bool = False) -> None:
        """
        Status of geo-fencing. Sent in extended status stream when fencing
        enabled.

        breach_status             : Breach status (0 if currently inside fence, 1 if outside). (type:uint8_t)
        breach_count              : Number of fence breaches. (type:uint16_t)
        breach_type               : Last breach type. (type:uint8_t, values:FENCE_BREACH)
        breach_time               : Time (since boot) of last breach. [ms] (type:uint32_t)
        breach_mitigation         : Active action to prevent fence breach (type:uint8_t, values:FENCE_MITIGATE)

        """
        self.send(self.fence_status_encode(breach_status, breach_count, breach_type, breach_time, breach_mitigation), force_mavlink1=force_mavlink1)

## mag_cal_report_encode
    def mag_cal_report_encode(self, compass_id: int, cal_mask: int, cal_status: int, autosaved: int, fitness: float, ofs_x: float, ofs_y: float, ofs_z: float, diag_x: float, diag_y: float, diag_z: float, offdiag_x: float, offdiag_y: float, offdiag_z: float, orientation_confidence: float = 0, old_orientation: int = 0, new_orientation: int = 0, scale_factor: float = 0) -> MAVLink_mag_cal_report_message:
        """
        Reports results of completed compass calibration. Sent until
        MAG_CAL_ACK received.

        compass_id                : Compass being calibrated. (type:uint8_t)
        cal_mask                  : Bitmask of compasses being calibrated. (type:uint8_t)
        cal_status                : Calibration Status. (type:uint8_t, values:MAG_CAL_STATUS)
        autosaved                 : 0=requires a MAV_CMD_DO_ACCEPT_MAG_CAL, 1=saved to parameters. (type:uint8_t)
        fitness                   : RMS milligauss residuals. [mgauss] (type:float)
        ofs_x                     : X offset. (type:float)
        ofs_y                     : Y offset. (type:float)
        ofs_z                     : Z offset. (type:float)
        diag_x                    : X diagonal (matrix 11). (type:float)
        diag_y                    : Y diagonal (matrix 22). (type:float)
        diag_z                    : Z diagonal (matrix 33). (type:float)
        offdiag_x                 : X off-diagonal (matrix 12 and 21). (type:float)
        offdiag_y                 : Y off-diagonal (matrix 13 and 31). (type:float)
        offdiag_z                 : Z off-diagonal (matrix 32 and 23). (type:float)
        orientation_confidence        : Confidence in orientation (higher is better). (type:float)
        old_orientation           : orientation before calibration. (type:uint8_t, values:MAV_SENSOR_ORIENTATION)
        new_orientation           : orientation after calibration. (type:uint8_t, values:MAV_SENSOR_ORIENTATION)
        scale_factor              : field radius correction factor (type:float)

        """
        return MAVLink_mag_cal_report_message(compass_id, cal_mask, cal_status, autosaved, fitness, ofs_x, ofs_y, ofs_z, diag_x, diag_y, diag_z, offdiag_x, offdiag_y, offdiag_z, orientation_confidence, old_orientation, new_orientation, scale_factor)

## mag_cal_report_send
    def mag_cal_report_send(self, compass_id: int, cal_mask: int, cal_status: int, autosaved: int, fitness: float, ofs_x: float, ofs_y: float, ofs_z: float, diag_x: float, diag_y: float, diag_z: float, offdiag_x: float, offdiag_y: float, offdiag_z: float, orientation_confidence: float = 0, old_orientation: int = 0, new_orientation: int = 0, scale_factor: float = 0, force_mavlink1: bool = False) -> None:
        """
        Reports results of completed compass calibration. Sent until
        MAG_CAL_ACK received.

        compass_id                : Compass being calibrated. (type:uint8_t)
        cal_mask                  : Bitmask of compasses being calibrated. (type:uint8_t)
        cal_status                : Calibration Status. (type:uint8_t, values:MAG_CAL_STATUS)
        autosaved                 : 0=requires a MAV_CMD_DO_ACCEPT_MAG_CAL, 1=saved to parameters. (type:uint8_t)
        fitness                   : RMS milligauss residuals. [mgauss] (type:float)
        ofs_x                     : X offset. (type:float)
        ofs_y                     : Y offset. (type:float)
        ofs_z                     : Z offset. (type:float)
        diag_x                    : X diagonal (matrix 11). (type:float)
        diag_y                    : Y diagonal (matrix 22). (type:float)
        diag_z                    : Z diagonal (matrix 33). (type:float)
        offdiag_x                 : X off-diagonal (matrix 12 and 21). (type:float)
        offdiag_y                 : Y off-diagonal (matrix 13 and 31). (type:float)
        offdiag_z                 : Z off-diagonal (matrix 32 and 23). (type:float)
        orientation_confidence        : Confidence in orientation (higher is better). (type:float)
        old_orientation           : orientation before calibration. (type:uint8_t, values:MAV_SENSOR_ORIENTATION)
        new_orientation           : orientation after calibration. (type:uint8_t, values:MAV_SENSOR_ORIENTATION)
        scale_factor              : field radius correction factor (type:float)

        """
        self.send(self.mag_cal_report_encode(compass_id, cal_mask, cal_status, autosaved, fitness, ofs_x, ofs_y, ofs_z, diag_x, diag_y, diag_z, offdiag_x, offdiag_y, offdiag_z, orientation_confidence, old_orientation, new_orientation, scale_factor), force_mavlink1=force_mavlink1)

## efi_status_encode
    def efi_status_encode(self, health: int, ecu_index: float, rpm: float, fuel_consumed: float, fuel_flow: float, engine_load: float, throttle_position: float, spark_dwell_time: float, barometric_pressure: float, intake_manifold_pressure: float, intake_manifold_temperature: float, cylinder_head_temperature: float, ignition_timing: float, injection_time: float, exhaust_gas_temperature: float, throttle_out: float, pt_compensation: float, ignition_voltage: float = 0, fuel_pressure: float = 0) -> MAVLink_efi_status_message:
        """
        EFI status output

        health                    : EFI health status (type:uint8_t)
        ecu_index                 : ECU index (type:float)
        rpm                       : RPM (type:float)
        fuel_consumed             : Fuel consumed [cm^3] (type:float)
        fuel_flow                 : Fuel flow rate [cm^3/min] (type:float)
        engine_load               : Engine load [%] (type:float)
        throttle_position         : Throttle position [%] (type:float)
        spark_dwell_time          : Spark dwell time [ms] (type:float)
        barometric_pressure        : Barometric pressure [kPa] (type:float)
        intake_manifold_pressure        : Intake manifold pressure( [kPa] (type:float)
        intake_manifold_temperature        : Intake manifold temperature [degC] (type:float)
        cylinder_head_temperature        : Cylinder head temperature [degC] (type:float)
        ignition_timing           : Ignition timing (Crank angle degrees) [deg] (type:float)
        injection_time            : Injection time [ms] (type:float)
        exhaust_gas_temperature        : Exhaust gas temperature [degC] (type:float)
        throttle_out              : Output throttle [%] (type:float)
        pt_compensation           : Pressure/temperature compensation (type:float)
        ignition_voltage          : Supply voltage to EFI sparking system.  Zero in this value means "unknown", so if the supply voltage really is zero volts use 0.0001 instead. [V] (type:float)
        fuel_pressure             : Fuel pressure. Zero in this value means "unknown", so if the fuel pressure really is zero kPa use 0.0001 instead. [kPa] (type:float)

        """
        return MAVLink_efi_status_message(health, ecu_index, rpm, fuel_consumed, fuel_flow, engine_load, throttle_position, spark_dwell_time, barometric_pressure, intake_manifold_pressure, intake_manifold_temperature, cylinder_head_temperature, ignition_timing, injection_time, exhaust_gas_temperature, throttle_out, pt_compensation, ignition_voltage, fuel_pressure)

## efi_status_send
    def efi_status_send(self, health: int, ecu_index: float, rpm: float, fuel_consumed: float, fuel_flow: float, engine_load: float, throttle_position: float, spark_dwell_time: float, barometric_pressure: float, intake_manifold_pressure: float, intake_manifold_temperature: float, cylinder_head_temperature: float, ignition_timing: float, injection_time: float, exhaust_gas_temperature: float, throttle_out: float, pt_compensation: float, ignition_voltage: float = 0, fuel_pressure: float = 0, force_mavlink1: bool = False) -> None:
        """
        EFI status output

        health                    : EFI health status (type:uint8_t)
        ecu_index                 : ECU index (type:float)
        rpm                       : RPM (type:float)
        fuel_consumed             : Fuel consumed [cm^3] (type:float)
        fuel_flow                 : Fuel flow rate [cm^3/min] (type:float)
        engine_load               : Engine load [%] (type:float)
        throttle_position         : Throttle position [%] (type:float)
        spark_dwell_time          : Spark dwell time [ms] (type:float)
        barometric_pressure        : Barometric pressure [kPa] (type:float)
        intake_manifold_pressure        : Intake manifold pressure( [kPa] (type:float)
        intake_manifold_temperature        : Intake manifold temperature [degC] (type:float)
        cylinder_head_temperature        : Cylinder head temperature [degC] (type:float)
        ignition_timing           : Ignition timing (Crank angle degrees) [deg] (type:float)
        injection_time            : Injection time [ms] (type:float)
        exhaust_gas_temperature        : Exhaust gas temperature [degC] (type:float)
        throttle_out              : Output throttle [%] (type:float)
        pt_compensation           : Pressure/temperature compensation (type:float)
        ignition_voltage          : Supply voltage to EFI sparking system.  Zero in this value means "unknown", so if the supply voltage really is zero volts use 0.0001 instead. [V] (type:float)
        fuel_pressure             : Fuel pressure. Zero in this value means "unknown", so if the fuel pressure really is zero kPa use 0.0001 instead. [kPa] (type:float)

        """
        self.send(self.efi_status_encode(health, ecu_index, rpm, fuel_consumed, fuel_flow, engine_load, throttle_position, spark_dwell_time, barometric_pressure, intake_manifold_pressure, intake_manifold_temperature, cylinder_head_temperature, ignition_timing, injection_time, exhaust_gas_temperature, throttle_out, pt_compensation, ignition_voltage, fuel_pressure), force_mavlink1=force_mavlink1)

## estimator_status_encode
    def estimator_status_encode(self, time_usec: int, flags: int, vel_ratio: float, pos_horiz_ratio: float, pos_vert_ratio: float, mag_ratio: float, hagl_ratio: float, tas_ratio: float, pos_horiz_accuracy: float, pos_vert_accuracy: float) -> MAVLink_estimator_status_message:
        """
        Estimator status message including flags, innovation test ratios and
        estimated accuracies. The flags message is an integer bitmask
        containing information on which EKF outputs are valid. See the
        ESTIMATOR_STATUS_FLAGS enum definition for further
        information. The innovation test ratios show the magnitude of
        the sensor innovation divided by the innovation check
        threshold. Under normal operation the innovation test ratios
        should be below 0.5 with occasional values up to 1.0. Values
        greater than 1.0 should be rare under normal operation and
        indicate that a measurement has been rejected by the filter.
        The user should be notified if an innovation test ratio
        greater than 1.0 is recorded. Notifications for values in the
        range between 0.5 and 1.0 should be optional and controllable
        by the user.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        flags                     : Bitmap indicating which EKF outputs are valid. (type:uint16_t, values:ESTIMATOR_STATUS_FLAGS)
        vel_ratio                 : Velocity innovation test ratio (type:float)
        pos_horiz_ratio           : Horizontal position innovation test ratio (type:float)
        pos_vert_ratio            : Vertical position innovation test ratio (type:float)
        mag_ratio                 : Magnetometer innovation test ratio (type:float)
        hagl_ratio                : Height above terrain innovation test ratio (type:float)
        tas_ratio                 : True airspeed innovation test ratio (type:float)
        pos_horiz_accuracy        : Horizontal position 1-STD accuracy relative to the EKF local origin [m] (type:float)
        pos_vert_accuracy         : Vertical position 1-STD accuracy relative to the EKF local origin [m] (type:float)

        """
        return MAVLink_estimator_status_message(time_usec, flags, vel_ratio, pos_horiz_ratio, pos_vert_ratio, mag_ratio, hagl_ratio, tas_ratio, pos_horiz_accuracy, pos_vert_accuracy)

## estimator_status_send
    def estimator_status_send(self, time_usec: int, flags: int, vel_ratio: float, pos_horiz_ratio: float, pos_vert_ratio: float, mag_ratio: float, hagl_ratio: float, tas_ratio: float, pos_horiz_accuracy: float, pos_vert_accuracy: float, force_mavlink1: bool = False) -> None:
        """
        Estimator status message including flags, innovation test ratios and
        estimated accuracies. The flags message is an integer bitmask
        containing information on which EKF outputs are valid. See the
        ESTIMATOR_STATUS_FLAGS enum definition for further
        information. The innovation test ratios show the magnitude of
        the sensor innovation divided by the innovation check
        threshold. Under normal operation the innovation test ratios
        should be below 0.5 with occasional values up to 1.0. Values
        greater than 1.0 should be rare under normal operation and
        indicate that a measurement has been rejected by the filter.
        The user should be notified if an innovation test ratio
        greater than 1.0 is recorded. Notifications for values in the
        range between 0.5 and 1.0 should be optional and controllable
        by the user.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        flags                     : Bitmap indicating which EKF outputs are valid. (type:uint16_t, values:ESTIMATOR_STATUS_FLAGS)
        vel_ratio                 : Velocity innovation test ratio (type:float)
        pos_horiz_ratio           : Horizontal position innovation test ratio (type:float)
        pos_vert_ratio            : Vertical position innovation test ratio (type:float)
        mag_ratio                 : Magnetometer innovation test ratio (type:float)
        hagl_ratio                : Height above terrain innovation test ratio (type:float)
        tas_ratio                 : True airspeed innovation test ratio (type:float)
        pos_horiz_accuracy        : Horizontal position 1-STD accuracy relative to the EKF local origin [m] (type:float)
        pos_vert_accuracy         : Vertical position 1-STD accuracy relative to the EKF local origin [m] (type:float)

        """
        self.send(self.estimator_status_encode(time_usec, flags, vel_ratio, pos_horiz_ratio, pos_vert_ratio, mag_ratio, hagl_ratio, tas_ratio, pos_horiz_accuracy, pos_vert_accuracy), force_mavlink1=force_mavlink1)

## wind_cov_encode
    def wind_cov_encode(self, time_usec: int, wind_x: float, wind_y: float, wind_z: float, var_horiz: float, var_vert: float, wind_alt: float, horiz_accuracy: float, vert_accuracy: float) -> MAVLink_wind_cov_message:
        """
        Wind covariance estimate from vehicle.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        wind_x                    : Wind in X (NED) direction [m/s] (type:float)
        wind_y                    : Wind in Y (NED) direction [m/s] (type:float)
        wind_z                    : Wind in Z (NED) direction [m/s] (type:float)
        var_horiz                 : Variability of the wind in XY. RMS of a 1 Hz lowpassed wind estimate. [m/s] (type:float)
        var_vert                  : Variability of the wind in Z. RMS of a 1 Hz lowpassed wind estimate. [m/s] (type:float)
        wind_alt                  : Altitude (MSL) that this measurement was taken at [m] (type:float)
        horiz_accuracy            : Horizontal speed 1-STD accuracy [m] (type:float)
        vert_accuracy             : Vertical speed 1-STD accuracy [m] (type:float)

        """
        return MAVLink_wind_cov_message(time_usec, wind_x, wind_y, wind_z, var_horiz, var_vert, wind_alt, horiz_accuracy, vert_accuracy)

## wind_cov_send
    def wind_cov_send(self, time_usec: int, wind_x: float, wind_y: float, wind_z: float, var_horiz: float, var_vert: float, wind_alt: float, horiz_accuracy: float, vert_accuracy: float, force_mavlink1: bool = False) -> None:
        """
        Wind covariance estimate from vehicle.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        wind_x                    : Wind in X (NED) direction [m/s] (type:float)
        wind_y                    : Wind in Y (NED) direction [m/s] (type:float)
        wind_z                    : Wind in Z (NED) direction [m/s] (type:float)
        var_horiz                 : Variability of the wind in XY. RMS of a 1 Hz lowpassed wind estimate. [m/s] (type:float)
        var_vert                  : Variability of the wind in Z. RMS of a 1 Hz lowpassed wind estimate. [m/s] (type:float)
        wind_alt                  : Altitude (MSL) that this measurement was taken at [m] (type:float)
        horiz_accuracy            : Horizontal speed 1-STD accuracy [m] (type:float)
        vert_accuracy             : Vertical speed 1-STD accuracy [m] (type:float)

        """
        self.send(self.wind_cov_encode(time_usec, wind_x, wind_y, wind_z, var_horiz, var_vert, wind_alt, horiz_accuracy, vert_accuracy), force_mavlink1=force_mavlink1)

## gps_input_encode
    def gps_input_encode(self, time_usec: int, gps_id: int, ignore_flags: int, time_week_ms: int, time_week: int, fix_type: int, lat: int, lon: int, alt: float, hdop: float, vdop: float, vn: float, ve: float, vd: float, speed_accuracy: float, horiz_accuracy: float, vert_accuracy: float, satellites_visible: int, yaw: int = 0) -> MAVLink_gps_input_message:
        """
        GPS sensor input message.  This is a raw sensor value sent by the GPS.
        This is NOT the global position estimate of the system.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        gps_id                    : ID of the GPS for multiple GPS inputs (type:uint8_t)
        ignore_flags              : Bitmap indicating which GPS input flags fields to ignore.  All other fields must be provided. (type:uint16_t, values:GPS_INPUT_IGNORE_FLAGS)
        time_week_ms              : GPS time (from start of GPS week) [ms] (type:uint32_t)
        time_week                 : GPS week number (type:uint16_t)
        fix_type                  : 0-1: no fix, 2: 2D fix, 3: 3D fix. 4: 3D with DGPS. 5: 3D with RTK (type:uint8_t)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Positive for up. [m] (type:float)
        hdop                      : GPS HDOP horizontal dilution of position (unitless). If unknown, set to: UINT16_MAX (type:float)
        vdop                      : GPS VDOP vertical dilution of position (unitless). If unknown, set to: UINT16_MAX (type:float)
        vn                        : GPS velocity in north direction in earth-fixed NED frame [m/s] (type:float)
        ve                        : GPS velocity in east direction in earth-fixed NED frame [m/s] (type:float)
        vd                        : GPS velocity in down direction in earth-fixed NED frame [m/s] (type:float)
        speed_accuracy            : GPS speed accuracy [m/s] (type:float)
        horiz_accuracy            : GPS horizontal accuracy [m] (type:float)
        vert_accuracy             : GPS vertical accuracy [m] (type:float)
        satellites_visible        : Number of satellites visible. (type:uint8_t)
        yaw                       : Yaw of vehicle relative to Earth's North, zero means not available, use 36000 for north [cdeg] (type:uint16_t)

        """
        return MAVLink_gps_input_message(time_usec, gps_id, ignore_flags, time_week_ms, time_week, fix_type, lat, lon, alt, hdop, vdop, vn, ve, vd, speed_accuracy, horiz_accuracy, vert_accuracy, satellites_visible, yaw)

## gps_input_send
    def gps_input_send(self, time_usec: int, gps_id: int, ignore_flags: int, time_week_ms: int, time_week: int, fix_type: int, lat: int, lon: int, alt: float, hdop: float, vdop: float, vn: float, ve: float, vd: float, speed_accuracy: float, horiz_accuracy: float, vert_accuracy: float, satellites_visible: int, yaw: int = 0, force_mavlink1: bool = False) -> None:
        """
        GPS sensor input message.  This is a raw sensor value sent by the GPS.
        This is NOT the global position estimate of the system.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        gps_id                    : ID of the GPS for multiple GPS inputs (type:uint8_t)
        ignore_flags              : Bitmap indicating which GPS input flags fields to ignore.  All other fields must be provided. (type:uint16_t, values:GPS_INPUT_IGNORE_FLAGS)
        time_week_ms              : GPS time (from start of GPS week) [ms] (type:uint32_t)
        time_week                 : GPS week number (type:uint16_t)
        fix_type                  : 0-1: no fix, 2: 2D fix, 3: 3D fix. 4: 3D with DGPS. 5: 3D with RTK (type:uint8_t)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (MSL). Positive for up. [m] (type:float)
        hdop                      : GPS HDOP horizontal dilution of position (unitless). If unknown, set to: UINT16_MAX (type:float)
        vdop                      : GPS VDOP vertical dilution of position (unitless). If unknown, set to: UINT16_MAX (type:float)
        vn                        : GPS velocity in north direction in earth-fixed NED frame [m/s] (type:float)
        ve                        : GPS velocity in east direction in earth-fixed NED frame [m/s] (type:float)
        vd                        : GPS velocity in down direction in earth-fixed NED frame [m/s] (type:float)
        speed_accuracy            : GPS speed accuracy [m/s] (type:float)
        horiz_accuracy            : GPS horizontal accuracy [m] (type:float)
        vert_accuracy             : GPS vertical accuracy [m] (type:float)
        satellites_visible        : Number of satellites visible. (type:uint8_t)
        yaw                       : Yaw of vehicle relative to Earth's North, zero means not available, use 36000 for north [cdeg] (type:uint16_t)

        """
        self.send(self.gps_input_encode(time_usec, gps_id, ignore_flags, time_week_ms, time_week, fix_type, lat, lon, alt, hdop, vdop, vn, ve, vd, speed_accuracy, horiz_accuracy, vert_accuracy, satellites_visible, yaw), force_mavlink1=force_mavlink1)

## gps_rtcm_data_encode
    def gps_rtcm_data_encode(self, flags: int, len: int, data: Sequence[int]) -> MAVLink_gps_rtcm_data_message:
        """
        RTCM message for injecting into the onboard GPS (used for DGPS)

        flags                     : LSB: 1 means message is fragmented, next 2 bits are the fragment ID, the remaining 5 bits are used for the sequence ID. Messages are only to be flushed to the GPS when the entire message has been reconstructed on the autopilot. The fragment ID specifies which order the fragments should be assembled into a buffer, while the sequence ID is used to detect a mismatch between different buffers. The buffer is considered fully reconstructed when either all 4 fragments are present, or all the fragments before the first fragment with a non full payload is received. This management is used to ensure that normal GPS operation doesn't corrupt RTCM data, and to recover from a unreliable transport delivery order. (type:uint8_t)
        len                       : data length [bytes] (type:uint8_t)
        data                      : RTCM message (may be fragmented) (type:uint8_t)

        """
        return MAVLink_gps_rtcm_data_message(flags, len, data)

## gps_rtcm_data_send
    def gps_rtcm_data_send(self, flags: int, len: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        RTCM message for injecting into the onboard GPS (used for DGPS)

        flags                     : LSB: 1 means message is fragmented, next 2 bits are the fragment ID, the remaining 5 bits are used for the sequence ID. Messages are only to be flushed to the GPS when the entire message has been reconstructed on the autopilot. The fragment ID specifies which order the fragments should be assembled into a buffer, while the sequence ID is used to detect a mismatch between different buffers. The buffer is considered fully reconstructed when either all 4 fragments are present, or all the fragments before the first fragment with a non full payload is received. This management is used to ensure that normal GPS operation doesn't corrupt RTCM data, and to recover from a unreliable transport delivery order. (type:uint8_t)
        len                       : data length [bytes] (type:uint8_t)
        data                      : RTCM message (may be fragmented) (type:uint8_t)

        """
        self.send(self.gps_rtcm_data_encode(flags, len, data), force_mavlink1=force_mavlink1)

## high_latency_encode
    def high_latency_encode(self, base_mode: int, custom_mode: int, landed_state: int, roll: int, pitch: int, heading: int, throttle: int, heading_sp: int, latitude: int, longitude: int, altitude_amsl: int, altitude_sp: int, airspeed: int, airspeed_sp: int, groundspeed: int, climb_rate: int, gps_nsat: int, gps_fix_type: int, battery_remaining: int, temperature: int, temperature_air: int, failsafe: int, wp_num: int, wp_distance: int) -> MAVLink_high_latency_message:
        """
        Message appropriate for high latency connections like Iridium

        base_mode                 : Bitmap of enabled system modes. (type:uint8_t, values:MAV_MODE_FLAG)
        custom_mode               : A bitfield for use for autopilot-specific flags. (type:uint32_t)
        landed_state              : The landed state. Is set to MAV_LANDED_STATE_UNDEFINED if landed state is unknown. (type:uint8_t, values:MAV_LANDED_STATE)
        roll                      : roll [cdeg] (type:int16_t)
        pitch                     : pitch [cdeg] (type:int16_t)
        heading                   : heading [cdeg] (type:uint16_t)
        throttle                  : throttle (percentage) [%] (type:int8_t)
        heading_sp                : heading setpoint [cdeg] (type:int16_t)
        latitude                  : Latitude [degE7] (type:int32_t)
        longitude                 : Longitude [degE7] (type:int32_t)
        altitude_amsl             : Altitude above mean sea level [m] (type:int16_t)
        altitude_sp               : Altitude setpoint relative to the home position [m] (type:int16_t)
        airspeed                  : airspeed [m/s] (type:uint8_t)
        airspeed_sp               : airspeed setpoint [m/s] (type:uint8_t)
        groundspeed               : groundspeed [m/s] (type:uint8_t)
        climb_rate                : climb rate [m/s] (type:int8_t)
        gps_nsat                  : Number of satellites visible. If unknown, set to UINT8_MAX (type:uint8_t)
        gps_fix_type              : GPS Fix type. (type:uint8_t, values:GPS_FIX_TYPE)
        battery_remaining         : Remaining battery (percentage) [%] (type:uint8_t)
        temperature               : Autopilot temperature (degrees C) [degC] (type:int8_t)
        temperature_air           : Air temperature (degrees C) from airspeed sensor [degC] (type:int8_t)
        failsafe                  : failsafe (each bit represents a failsafe where 0=ok, 1=failsafe active (bit0:RC, bit1:batt, bit2:GPS, bit3:GCS, bit4:fence) (type:uint8_t)
        wp_num                    : current waypoint number (type:uint8_t)
        wp_distance               : distance to target [m] (type:uint16_t)

        """
        return MAVLink_high_latency_message(base_mode, custom_mode, landed_state, roll, pitch, heading, throttle, heading_sp, latitude, longitude, altitude_amsl, altitude_sp, airspeed, airspeed_sp, groundspeed, climb_rate, gps_nsat, gps_fix_type, battery_remaining, temperature, temperature_air, failsafe, wp_num, wp_distance)

## high_latency_send
    def high_latency_send(self, base_mode: int, custom_mode: int, landed_state: int, roll: int, pitch: int, heading: int, throttle: int, heading_sp: int, latitude: int, longitude: int, altitude_amsl: int, altitude_sp: int, airspeed: int, airspeed_sp: int, groundspeed: int, climb_rate: int, gps_nsat: int, gps_fix_type: int, battery_remaining: int, temperature: int, temperature_air: int, failsafe: int, wp_num: int, wp_distance: int, force_mavlink1: bool = False) -> None:
        """
        Message appropriate for high latency connections like Iridium

        base_mode                 : Bitmap of enabled system modes. (type:uint8_t, values:MAV_MODE_FLAG)
        custom_mode               : A bitfield for use for autopilot-specific flags. (type:uint32_t)
        landed_state              : The landed state. Is set to MAV_LANDED_STATE_UNDEFINED if landed state is unknown. (type:uint8_t, values:MAV_LANDED_STATE)
        roll                      : roll [cdeg] (type:int16_t)
        pitch                     : pitch [cdeg] (type:int16_t)
        heading                   : heading [cdeg] (type:uint16_t)
        throttle                  : throttle (percentage) [%] (type:int8_t)
        heading_sp                : heading setpoint [cdeg] (type:int16_t)
        latitude                  : Latitude [degE7] (type:int32_t)
        longitude                 : Longitude [degE7] (type:int32_t)
        altitude_amsl             : Altitude above mean sea level [m] (type:int16_t)
        altitude_sp               : Altitude setpoint relative to the home position [m] (type:int16_t)
        airspeed                  : airspeed [m/s] (type:uint8_t)
        airspeed_sp               : airspeed setpoint [m/s] (type:uint8_t)
        groundspeed               : groundspeed [m/s] (type:uint8_t)
        climb_rate                : climb rate [m/s] (type:int8_t)
        gps_nsat                  : Number of satellites visible. If unknown, set to UINT8_MAX (type:uint8_t)
        gps_fix_type              : GPS Fix type. (type:uint8_t, values:GPS_FIX_TYPE)
        battery_remaining         : Remaining battery (percentage) [%] (type:uint8_t)
        temperature               : Autopilot temperature (degrees C) [degC] (type:int8_t)
        temperature_air           : Air temperature (degrees C) from airspeed sensor [degC] (type:int8_t)
        failsafe                  : failsafe (each bit represents a failsafe where 0=ok, 1=failsafe active (bit0:RC, bit1:batt, bit2:GPS, bit3:GCS, bit4:fence) (type:uint8_t)
        wp_num                    : current waypoint number (type:uint8_t)
        wp_distance               : distance to target [m] (type:uint16_t)

        """
        self.send(self.high_latency_encode(base_mode, custom_mode, landed_state, roll, pitch, heading, throttle, heading_sp, latitude, longitude, altitude_amsl, altitude_sp, airspeed, airspeed_sp, groundspeed, climb_rate, gps_nsat, gps_fix_type, battery_remaining, temperature, temperature_air, failsafe, wp_num, wp_distance), force_mavlink1=force_mavlink1)

## high_latency2_encode
    def high_latency2_encode(self, timestamp: int, type: int, autopilot: int, custom_mode: int, latitude: int, longitude: int, altitude: int, target_altitude: int, heading: int, target_heading: int, target_distance: int, throttle: int, airspeed: int, airspeed_sp: int, groundspeed: int, windspeed: int, wind_heading: int, eph: int, epv: int, temperature_air: int, climb_rate: int, battery: int, wp_num: int, failure_flags: int, custom0: int, custom1: int, custom2: int) -> MAVLink_high_latency2_message:
        """
        Message appropriate for high latency connections like Iridium (version
        2)

        timestamp                 : Timestamp (milliseconds since boot or Unix epoch) [ms] (type:uint32_t)
        type                      : Type of the MAV (quadrotor, helicopter, etc.) (type:uint8_t, values:MAV_TYPE)
        autopilot                 : Autopilot type / class. Use MAV_AUTOPILOT_INVALID for components that are not flight controllers. (type:uint8_t, values:MAV_AUTOPILOT)
        custom_mode               : A bitfield for use for autopilot-specific flags (2 byte version). (type:uint16_t)
        latitude                  : Latitude [degE7] (type:int32_t)
        longitude                 : Longitude [degE7] (type:int32_t)
        altitude                  : Altitude above mean sea level [m] (type:int16_t)
        target_altitude           : Altitude setpoint [m] (type:int16_t)
        heading                   : Heading [deg/2] (type:uint8_t)
        target_heading            : Heading setpoint [deg/2] (type:uint8_t)
        target_distance           : Distance to target waypoint or position [dam] (type:uint16_t)
        throttle                  : Throttle [%] (type:uint8_t)
        airspeed                  : Airspeed [m/s*5] (type:uint8_t)
        airspeed_sp               : Airspeed setpoint [m/s*5] (type:uint8_t)
        groundspeed               : Groundspeed [m/s*5] (type:uint8_t)
        windspeed                 : Windspeed [m/s*5] (type:uint8_t)
        wind_heading              : Wind heading [deg/2] (type:uint8_t)
        eph                       : Maximum error horizontal position since last message [dm] (type:uint8_t)
        epv                       : Maximum error vertical position since last message [dm] (type:uint8_t)
        temperature_air           : Air temperature from airspeed sensor [degC] (type:int8_t)
        climb_rate                : Maximum climb rate magnitude since last message [dm/s] (type:int8_t)
        battery                   : Battery level (-1 if field not provided). [%] (type:int8_t)
        wp_num                    : Current waypoint number (type:uint16_t)
        failure_flags             : Bitmap of failure flags. (type:uint16_t, values:HL_FAILURE_FLAG)
        custom0                   : Field for custom payload. (type:int8_t)
        custom1                   : Field for custom payload. (type:int8_t)
        custom2                   : Field for custom payload. (type:int8_t)

        """
        return MAVLink_high_latency2_message(timestamp, type, autopilot, custom_mode, latitude, longitude, altitude, target_altitude, heading, target_heading, target_distance, throttle, airspeed, airspeed_sp, groundspeed, windspeed, wind_heading, eph, epv, temperature_air, climb_rate, battery, wp_num, failure_flags, custom0, custom1, custom2)

## high_latency2_send
    def high_latency2_send(self, timestamp: int, type: int, autopilot: int, custom_mode: int, latitude: int, longitude: int, altitude: int, target_altitude: int, heading: int, target_heading: int, target_distance: int, throttle: int, airspeed: int, airspeed_sp: int, groundspeed: int, windspeed: int, wind_heading: int, eph: int, epv: int, temperature_air: int, climb_rate: int, battery: int, wp_num: int, failure_flags: int, custom0: int, custom1: int, custom2: int, force_mavlink1: bool = False) -> None:
        """
        Message appropriate for high latency connections like Iridium (version
        2)

        timestamp                 : Timestamp (milliseconds since boot or Unix epoch) [ms] (type:uint32_t)
        type                      : Type of the MAV (quadrotor, helicopter, etc.) (type:uint8_t, values:MAV_TYPE)
        autopilot                 : Autopilot type / class. Use MAV_AUTOPILOT_INVALID for components that are not flight controllers. (type:uint8_t, values:MAV_AUTOPILOT)
        custom_mode               : A bitfield for use for autopilot-specific flags (2 byte version). (type:uint16_t)
        latitude                  : Latitude [degE7] (type:int32_t)
        longitude                 : Longitude [degE7] (type:int32_t)
        altitude                  : Altitude above mean sea level [m] (type:int16_t)
        target_altitude           : Altitude setpoint [m] (type:int16_t)
        heading                   : Heading [deg/2] (type:uint8_t)
        target_heading            : Heading setpoint [deg/2] (type:uint8_t)
        target_distance           : Distance to target waypoint or position [dam] (type:uint16_t)
        throttle                  : Throttle [%] (type:uint8_t)
        airspeed                  : Airspeed [m/s*5] (type:uint8_t)
        airspeed_sp               : Airspeed setpoint [m/s*5] (type:uint8_t)
        groundspeed               : Groundspeed [m/s*5] (type:uint8_t)
        windspeed                 : Windspeed [m/s*5] (type:uint8_t)
        wind_heading              : Wind heading [deg/2] (type:uint8_t)
        eph                       : Maximum error horizontal position since last message [dm] (type:uint8_t)
        epv                       : Maximum error vertical position since last message [dm] (type:uint8_t)
        temperature_air           : Air temperature from airspeed sensor [degC] (type:int8_t)
        climb_rate                : Maximum climb rate magnitude since last message [dm/s] (type:int8_t)
        battery                   : Battery level (-1 if field not provided). [%] (type:int8_t)
        wp_num                    : Current waypoint number (type:uint16_t)
        failure_flags             : Bitmap of failure flags. (type:uint16_t, values:HL_FAILURE_FLAG)
        custom0                   : Field for custom payload. (type:int8_t)
        custom1                   : Field for custom payload. (type:int8_t)
        custom2                   : Field for custom payload. (type:int8_t)

        """
        self.send(self.high_latency2_encode(timestamp, type, autopilot, custom_mode, latitude, longitude, altitude, target_altitude, heading, target_heading, target_distance, throttle, airspeed, airspeed_sp, groundspeed, windspeed, wind_heading, eph, epv, temperature_air, climb_rate, battery, wp_num, failure_flags, custom0, custom1, custom2), force_mavlink1=force_mavlink1)

## vibration_encode
    def vibration_encode(self, time_usec: int, vibration_x: float, vibration_y: float, vibration_z: float, clipping_0: int, clipping_1: int, clipping_2: int) -> MAVLink_vibration_message:
        """
        Vibration levels and accelerometer clipping

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        vibration_x               : Vibration levels on X-axis (type:float)
        vibration_y               : Vibration levels on Y-axis (type:float)
        vibration_z               : Vibration levels on Z-axis (type:float)
        clipping_0                : first accelerometer clipping count (type:uint32_t)
        clipping_1                : second accelerometer clipping count (type:uint32_t)
        clipping_2                : third accelerometer clipping count (type:uint32_t)

        """
        return MAVLink_vibration_message(time_usec, vibration_x, vibration_y, vibration_z, clipping_0, clipping_1, clipping_2)

## vibration_send
    def vibration_send(self, time_usec: int, vibration_x: float, vibration_y: float, vibration_z: float, clipping_0: int, clipping_1: int, clipping_2: int, force_mavlink1: bool = False) -> None:
        """
        Vibration levels and accelerometer clipping

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        vibration_x               : Vibration levels on X-axis (type:float)
        vibration_y               : Vibration levels on Y-axis (type:float)
        vibration_z               : Vibration levels on Z-axis (type:float)
        clipping_0                : first accelerometer clipping count (type:uint32_t)
        clipping_1                : second accelerometer clipping count (type:uint32_t)
        clipping_2                : third accelerometer clipping count (type:uint32_t)

        """
        self.send(self.vibration_encode(time_usec, vibration_x, vibration_y, vibration_z, clipping_0, clipping_1, clipping_2), force_mavlink1=force_mavlink1)

## home_position_encode
    def home_position_encode(self, latitude: int, longitude: int, altitude: int, x: float, y: float, z: float, q: Sequence[float], approach_x: float, approach_y: float, approach_z: float, time_usec: int = 0) -> MAVLink_home_position_message:
        """
        This message can be requested by sending the MAV_CMD_GET_HOME_POSITION
        command. The position the system will return to and land on.
        The position is set automatically by the system during the
        takeoff in case it was not explicitly set by the operator
        before or after. The global and local positions encode the
        position in the respective coordinate frames, while the q
        parameter encodes the orientation of the surface. Under normal
        conditions it describes the heading and terrain slope, which
        can be used by the aircraft to adjust the approach. The
        approach 3D vector describes the point to which the system
        should fly in normal flight mode and then perform a landing
        sequence along the vector.

        latitude                  : Latitude (WGS84) [degE7] (type:int32_t)
        longitude                 : Longitude (WGS84) [degE7] (type:int32_t)
        altitude                  : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        x                         : Local X position of this position in the local coordinate frame [m] (type:float)
        y                         : Local Y position of this position in the local coordinate frame [m] (type:float)
        z                         : Local Z position of this position in the local coordinate frame [m] (type:float)
        q                         : World to surface normal and heading transformation of the takeoff position. Used to indicate the heading and slope of the ground (type:float)
        approach_x                : Local X position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        approach_y                : Local Y position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        approach_z                : Local Z position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)

        """
        return MAVLink_home_position_message(latitude, longitude, altitude, x, y, z, q, approach_x, approach_y, approach_z, time_usec)

## home_position_send
    def home_position_send(self, latitude: int, longitude: int, altitude: int, x: float, y: float, z: float, q: Sequence[float], approach_x: float, approach_y: float, approach_z: float, time_usec: int = 0, force_mavlink1: bool = False) -> None:
        """
        This message can be requested by sending the MAV_CMD_GET_HOME_POSITION
        command. The position the system will return to and land on.
        The position is set automatically by the system during the
        takeoff in case it was not explicitly set by the operator
        before or after. The global and local positions encode the
        position in the respective coordinate frames, while the q
        parameter encodes the orientation of the surface. Under normal
        conditions it describes the heading and terrain slope, which
        can be used by the aircraft to adjust the approach. The
        approach 3D vector describes the point to which the system
        should fly in normal flight mode and then perform a landing
        sequence along the vector.

        latitude                  : Latitude (WGS84) [degE7] (type:int32_t)
        longitude                 : Longitude (WGS84) [degE7] (type:int32_t)
        altitude                  : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        x                         : Local X position of this position in the local coordinate frame [m] (type:float)
        y                         : Local Y position of this position in the local coordinate frame [m] (type:float)
        z                         : Local Z position of this position in the local coordinate frame [m] (type:float)
        q                         : World to surface normal and heading transformation of the takeoff position. Used to indicate the heading and slope of the ground (type:float)
        approach_x                : Local X position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        approach_y                : Local Y position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        approach_z                : Local Z position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)

        """
        self.send(self.home_position_encode(latitude, longitude, altitude, x, y, z, q, approach_x, approach_y, approach_z, time_usec), force_mavlink1=force_mavlink1)

## set_home_position_encode
    def set_home_position_encode(self, target_system: int, latitude: int, longitude: int, altitude: int, x: float, y: float, z: float, q: Sequence[float], approach_x: float, approach_y: float, approach_z: float, time_usec: int = 0) -> MAVLink_set_home_position_message:
        """
        The position the system will return to and land on. The position is
        set automatically by the system during the takeoff in case it
        was not explicitly set by the operator before or after. The
        global and local positions encode the position in the
        respective coordinate frames, while the q parameter encodes
        the orientation of the surface. Under normal conditions it
        describes the heading and terrain slope, which can be used by
        the aircraft to adjust the approach. The approach 3D vector
        describes the point to which the system should fly in normal
        flight mode and then perform a landing sequence along the
        vector.

        target_system             : System ID. (type:uint8_t)
        latitude                  : Latitude (WGS84) [degE7] (type:int32_t)
        longitude                 : Longitude (WGS84) [degE7] (type:int32_t)
        altitude                  : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        x                         : Local X position of this position in the local coordinate frame [m] (type:float)
        y                         : Local Y position of this position in the local coordinate frame [m] (type:float)
        z                         : Local Z position of this position in the local coordinate frame [m] (type:float)
        q                         : World to surface normal and heading transformation of the takeoff position. Used to indicate the heading and slope of the ground (type:float)
        approach_x                : Local X position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        approach_y                : Local Y position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        approach_z                : Local Z position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)

        """
        return MAVLink_set_home_position_message(target_system, latitude, longitude, altitude, x, y, z, q, approach_x, approach_y, approach_z, time_usec)

## set_home_position_send
    def set_home_position_send(self, target_system: int, latitude: int, longitude: int, altitude: int, x: float, y: float, z: float, q: Sequence[float], approach_x: float, approach_y: float, approach_z: float, time_usec: int = 0, force_mavlink1: bool = False) -> None:
        """
        The position the system will return to and land on. The position is
        set automatically by the system during the takeoff in case it
        was not explicitly set by the operator before or after. The
        global and local positions encode the position in the
        respective coordinate frames, while the q parameter encodes
        the orientation of the surface. Under normal conditions it
        describes the heading and terrain slope, which can be used by
        the aircraft to adjust the approach. The approach 3D vector
        describes the point to which the system should fly in normal
        flight mode and then perform a landing sequence along the
        vector.

        target_system             : System ID. (type:uint8_t)
        latitude                  : Latitude (WGS84) [degE7] (type:int32_t)
        longitude                 : Longitude (WGS84) [degE7] (type:int32_t)
        altitude                  : Altitude (MSL). Positive for up. [mm] (type:int32_t)
        x                         : Local X position of this position in the local coordinate frame [m] (type:float)
        y                         : Local Y position of this position in the local coordinate frame [m] (type:float)
        z                         : Local Z position of this position in the local coordinate frame [m] (type:float)
        q                         : World to surface normal and heading transformation of the takeoff position. Used to indicate the heading and slope of the ground (type:float)
        approach_x                : Local X position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        approach_y                : Local Y position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        approach_z                : Local Z position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. [m] (type:float)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)

        """
        self.send(self.set_home_position_encode(target_system, latitude, longitude, altitude, x, y, z, q, approach_x, approach_y, approach_z, time_usec), force_mavlink1=force_mavlink1)

## message_interval_encode
    def message_interval_encode(self, message_id: int, interval_us: int) -> MAVLink_message_interval_message:
        """
        The interval between messages for a particular MAVLink message ID.
        This message is sent in response to the
        MAV_CMD_REQUEST_MESSAGE command with param1=244 (this message)
        and param2=message_id (the id of the message for which the
        interval is required).         It may also be sent in response
        to MAV_CMD_GET_MESSAGE_INTERVAL.         This interface
        replaces DATA_STREAM.

        message_id                : The ID of the requested MAVLink message. v1.0 is limited to 254 messages. (type:uint16_t)
        interval_us               : The interval between two messages. A value of -1 indicates this stream is disabled, 0 indicates it is not available, > 0 indicates the interval at which it is sent. [us] (type:int32_t)

        """
        return MAVLink_message_interval_message(message_id, interval_us)

## message_interval_send
    def message_interval_send(self, message_id: int, interval_us: int, force_mavlink1: bool = False) -> None:
        """
        The interval between messages for a particular MAVLink message ID.
        This message is sent in response to the
        MAV_CMD_REQUEST_MESSAGE command with param1=244 (this message)
        and param2=message_id (the id of the message for which the
        interval is required).         It may also be sent in response
        to MAV_CMD_GET_MESSAGE_INTERVAL.         This interface
        replaces DATA_STREAM.

        message_id                : The ID of the requested MAVLink message. v1.0 is limited to 254 messages. (type:uint16_t)
        interval_us               : The interval between two messages. A value of -1 indicates this stream is disabled, 0 indicates it is not available, > 0 indicates the interval at which it is sent. [us] (type:int32_t)

        """
        self.send(self.message_interval_encode(message_id, interval_us), force_mavlink1=force_mavlink1)

## extended_sys_state_encode
    def extended_sys_state_encode(self, vtol_state: int, landed_state: int) -> MAVLink_extended_sys_state_message:
        """
        Provides state for additional features

        vtol_state                : The VTOL state if applicable. Is set to MAV_VTOL_STATE_UNDEFINED if UAV is not in VTOL configuration. (type:uint8_t, values:MAV_VTOL_STATE)
        landed_state              : The landed state. Is set to MAV_LANDED_STATE_UNDEFINED if landed state is unknown. (type:uint8_t, values:MAV_LANDED_STATE)

        """
        return MAVLink_extended_sys_state_message(vtol_state, landed_state)

## extended_sys_state_send
    def extended_sys_state_send(self, vtol_state: int, landed_state: int, force_mavlink1: bool = False) -> None:
        """
        Provides state for additional features

        vtol_state                : The VTOL state if applicable. Is set to MAV_VTOL_STATE_UNDEFINED if UAV is not in VTOL configuration. (type:uint8_t, values:MAV_VTOL_STATE)
        landed_state              : The landed state. Is set to MAV_LANDED_STATE_UNDEFINED if landed state is unknown. (type:uint8_t, values:MAV_LANDED_STATE)

        """
        self.send(self.extended_sys_state_encode(vtol_state, landed_state), force_mavlink1=force_mavlink1)

## adsb_vehicle_encode
    def adsb_vehicle_encode(self, ICAO_address: int, lat: int, lon: int, altitude_type: int, altitude: int, heading: int, hor_velocity: int, ver_velocity: int, callsign: bytes, emitter_type: int, tslc: int, flags: int, squawk: int) -> MAVLink_adsb_vehicle_message:
        """
        The location and information of an ADSB vehicle

        ICAO_address              : ICAO address (type:uint32_t)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        altitude_type             : ADSB altitude type. (type:uint8_t, values:ADSB_ALTITUDE_TYPE)
        altitude                  : Altitude(ASL) [mm] (type:int32_t)
        heading                   : Course over ground [cdeg] (type:uint16_t)
        hor_velocity              : The horizontal velocity [cm/s] (type:uint16_t)
        ver_velocity              : The vertical velocity. Positive is up [cm/s] (type:int16_t)
        callsign                  : The callsign, 8+null (type:char)
        emitter_type              : ADSB emitter type. (type:uint8_t, values:ADSB_EMITTER_TYPE)
        tslc                      : Time since last communication in seconds [s] (type:uint8_t)
        flags                     : Bitmap to indicate various statuses including valid data fields (type:uint16_t, values:ADSB_FLAGS)
        squawk                    : Squawk code (type:uint16_t)

        """
        return MAVLink_adsb_vehicle_message(ICAO_address, lat, lon, altitude_type, altitude, heading, hor_velocity, ver_velocity, callsign, emitter_type, tslc, flags, squawk)

## adsb_vehicle_send
    def adsb_vehicle_send(self, ICAO_address: int, lat: int, lon: int, altitude_type: int, altitude: int, heading: int, hor_velocity: int, ver_velocity: int, callsign: bytes, emitter_type: int, tslc: int, flags: int, squawk: int, force_mavlink1: bool = False) -> None:
        """
        The location and information of an ADSB vehicle

        ICAO_address              : ICAO address (type:uint32_t)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        altitude_type             : ADSB altitude type. (type:uint8_t, values:ADSB_ALTITUDE_TYPE)
        altitude                  : Altitude(ASL) [mm] (type:int32_t)
        heading                   : Course over ground [cdeg] (type:uint16_t)
        hor_velocity              : The horizontal velocity [cm/s] (type:uint16_t)
        ver_velocity              : The vertical velocity. Positive is up [cm/s] (type:int16_t)
        callsign                  : The callsign, 8+null (type:char)
        emitter_type              : ADSB emitter type. (type:uint8_t, values:ADSB_EMITTER_TYPE)
        tslc                      : Time since last communication in seconds [s] (type:uint8_t)
        flags                     : Bitmap to indicate various statuses including valid data fields (type:uint16_t, values:ADSB_FLAGS)
        squawk                    : Squawk code (type:uint16_t)

        """
        self.send(self.adsb_vehicle_encode(ICAO_address, lat, lon, altitude_type, altitude, heading, hor_velocity, ver_velocity, callsign, emitter_type, tslc, flags, squawk), force_mavlink1=force_mavlink1)

## collision_encode
    def collision_encode(self, src: int, id: int, action: int, threat_level: int, time_to_minimum_delta: float, altitude_minimum_delta: float, horizontal_minimum_delta: float) -> MAVLink_collision_message:
        """
        Information about a potential collision

        src                       : Collision data source (type:uint8_t, values:MAV_COLLISION_SRC)
        id                        : Unique identifier, domain based on src field (type:uint32_t)
        action                    : Action that is being taken to avoid this collision (type:uint8_t, values:MAV_COLLISION_ACTION)
        threat_level              : How concerned the aircraft is about this collision (type:uint8_t, values:MAV_COLLISION_THREAT_LEVEL)
        time_to_minimum_delta        : Estimated time until collision occurs [s] (type:float)
        altitude_minimum_delta        : Closest vertical distance between vehicle and object [m] (type:float)
        horizontal_minimum_delta        : Closest horizontal distance between vehicle and object [m] (type:float)

        """
        return MAVLink_collision_message(src, id, action, threat_level, time_to_minimum_delta, altitude_minimum_delta, horizontal_minimum_delta)

## collision_send
    def collision_send(self, src: int, id: int, action: int, threat_level: int, time_to_minimum_delta: float, altitude_minimum_delta: float, horizontal_minimum_delta: float, force_mavlink1: bool = False) -> None:
        """
        Information about a potential collision

        src                       : Collision data source (type:uint8_t, values:MAV_COLLISION_SRC)
        id                        : Unique identifier, domain based on src field (type:uint32_t)
        action                    : Action that is being taken to avoid this collision (type:uint8_t, values:MAV_COLLISION_ACTION)
        threat_level              : How concerned the aircraft is about this collision (type:uint8_t, values:MAV_COLLISION_THREAT_LEVEL)
        time_to_minimum_delta        : Estimated time until collision occurs [s] (type:float)
        altitude_minimum_delta        : Closest vertical distance between vehicle and object [m] (type:float)
        horizontal_minimum_delta        : Closest horizontal distance between vehicle and object [m] (type:float)

        """
        self.send(self.collision_encode(src, id, action, threat_level, time_to_minimum_delta, altitude_minimum_delta, horizontal_minimum_delta), force_mavlink1=force_mavlink1)

## v2_extension_encode
    def v2_extension_encode(self, target_network: int, target_system: int, target_component: int, message_type: int, payload: Sequence[int]) -> MAVLink_v2_extension_message:
        """
        Message implementing parts of the V2 payload specs in V1 frames for
        transitional support.

        target_network            : Network ID (0 for broadcast) (type:uint8_t)
        target_system             : System ID (0 for broadcast) (type:uint8_t)
        target_component          : Component ID (0 for broadcast) (type:uint8_t)
        message_type              : A code that identifies the software component that understands this message (analogous to USB device classes or mime type strings). If this code is less than 32768, it is considered a 'registered' protocol extension and the corresponding entry should be added to https://github.com/mavlink/mavlink/definition_files/extension_message_ids.xml. Software creators can register blocks of message IDs as needed (useful for GCS specific metadata, etc...). Message_types greater than 32767 are considered local experiments and should not be checked in to any widely distributed codebase. (type:uint16_t)
        payload                   : Variable length payload. The length must be encoded in the payload as part of the message_type protocol, e.g. by including the length as payload data, or by terminating the payload data with a non-zero marker. This is required in order to reconstruct zero-terminated payloads that are (or otherwise would be) trimmed by MAVLink 2 empty-byte truncation. The entire content of the payload block is opaque unless you understand the encoding message_type. The particular encoding used can be extension specific and might not always be documented as part of the MAVLink specification. (type:uint8_t)

        """
        return MAVLink_v2_extension_message(target_network, target_system, target_component, message_type, payload)

## v2_extension_send
    def v2_extension_send(self, target_network: int, target_system: int, target_component: int, message_type: int, payload: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Message implementing parts of the V2 payload specs in V1 frames for
        transitional support.

        target_network            : Network ID (0 for broadcast) (type:uint8_t)
        target_system             : System ID (0 for broadcast) (type:uint8_t)
        target_component          : Component ID (0 for broadcast) (type:uint8_t)
        message_type              : A code that identifies the software component that understands this message (analogous to USB device classes or mime type strings). If this code is less than 32768, it is considered a 'registered' protocol extension and the corresponding entry should be added to https://github.com/mavlink/mavlink/definition_files/extension_message_ids.xml. Software creators can register blocks of message IDs as needed (useful for GCS specific metadata, etc...). Message_types greater than 32767 are considered local experiments and should not be checked in to any widely distributed codebase. (type:uint16_t)
        payload                   : Variable length payload. The length must be encoded in the payload as part of the message_type protocol, e.g. by including the length as payload data, or by terminating the payload data with a non-zero marker. This is required in order to reconstruct zero-terminated payloads that are (or otherwise would be) trimmed by MAVLink 2 empty-byte truncation. The entire content of the payload block is opaque unless you understand the encoding message_type. The particular encoding used can be extension specific and might not always be documented as part of the MAVLink specification. (type:uint8_t)

        """
        self.send(self.v2_extension_encode(target_network, target_system, target_component, message_type, payload), force_mavlink1=force_mavlink1)

## memory_vect_encode
    def memory_vect_encode(self, address: int, ver: int, type: int, value: Sequence[int]) -> MAVLink_memory_vect_message:
        """
        Send raw controller memory. The use of this message is discouraged for
        normal packets, but a quite efficient way for testing new
        messages and getting experimental debug output.

        address                   : Starting address of the debug variables (type:uint16_t)
        ver                       : Version code of the type variable. 0=unknown, type ignored and assumed int16_t. 1=as below (type:uint8_t)
        type                      : Type code of the memory variables. for ver = 1: 0=16 x int16_t, 1=16 x uint16_t, 2=16 x Q15, 3=16 x 1Q14 (type:uint8_t)
        value                     : Memory contents at specified address (type:int8_t)

        """
        return MAVLink_memory_vect_message(address, ver, type, value)

## memory_vect_send
    def memory_vect_send(self, address: int, ver: int, type: int, value: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Send raw controller memory. The use of this message is discouraged for
        normal packets, but a quite efficient way for testing new
        messages and getting experimental debug output.

        address                   : Starting address of the debug variables (type:uint16_t)
        ver                       : Version code of the type variable. 0=unknown, type ignored and assumed int16_t. 1=as below (type:uint8_t)
        type                      : Type code of the memory variables. for ver = 1: 0=16 x int16_t, 1=16 x uint16_t, 2=16 x Q15, 3=16 x 1Q14 (type:uint8_t)
        value                     : Memory contents at specified address (type:int8_t)

        """
        self.send(self.memory_vect_encode(address, ver, type, value), force_mavlink1=force_mavlink1)

## debug_vect_encode
    def debug_vect_encode(self, name: bytes, time_usec: int, x: float, y: float, z: float) -> MAVLink_debug_vect_message:
        """
        To debug something using a named 3D vector.

        name                      : Name (type:char)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        x                         : x (type:float)
        y                         : y (type:float)
        z                         : z (type:float)

        """
        return MAVLink_debug_vect_message(name, time_usec, x, y, z)

## debug_vect_send
    def debug_vect_send(self, name: bytes, time_usec: int, x: float, y: float, z: float, force_mavlink1: bool = False) -> None:
        """
        To debug something using a named 3D vector.

        name                      : Name (type:char)
        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        x                         : x (type:float)
        y                         : y (type:float)
        z                         : z (type:float)

        """
        self.send(self.debug_vect_encode(name, time_usec, x, y, z), force_mavlink1=force_mavlink1)

## named_value_float_encode
    def named_value_float_encode(self, time_boot_ms: int, name: bytes, value: float) -> MAVLink_named_value_float_message:
        """
        Send a key-value pair as float. The use of this message is discouraged
        for normal packets, but a quite efficient way for testing new
        messages and getting experimental debug output.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        name                      : Name of the debug variable (type:char)
        value                     : Floating point value (type:float)

        """
        return MAVLink_named_value_float_message(time_boot_ms, name, value)

## named_value_float_send
    def named_value_float_send(self, time_boot_ms: int, name: bytes, value: float, force_mavlink1: bool = False) -> None:
        """
        Send a key-value pair as float. The use of this message is discouraged
        for normal packets, but a quite efficient way for testing new
        messages and getting experimental debug output.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        name                      : Name of the debug variable (type:char)
        value                     : Floating point value (type:float)

        """
        self.send(self.named_value_float_encode(time_boot_ms, name, value), force_mavlink1=force_mavlink1)

## named_value_int_encode
    def named_value_int_encode(self, time_boot_ms: int, name: bytes, value: int) -> MAVLink_named_value_int_message:
        """
        Send a key-value pair as integer. The use of this message is
        discouraged for normal packets, but a quite efficient way for
        testing new messages and getting experimental debug output.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        name                      : Name of the debug variable (type:char)
        value                     : Signed integer value (type:int32_t)

        """
        return MAVLink_named_value_int_message(time_boot_ms, name, value)

## named_value_int_send
    def named_value_int_send(self, time_boot_ms: int, name: bytes, value: int, force_mavlink1: bool = False) -> None:
        """
        Send a key-value pair as integer. The use of this message is
        discouraged for normal packets, but a quite efficient way for
        testing new messages and getting experimental debug output.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        name                      : Name of the debug variable (type:char)
        value                     : Signed integer value (type:int32_t)

        """
        self.send(self.named_value_int_encode(time_boot_ms, name, value), force_mavlink1=force_mavlink1)

## statustext_encode
    def statustext_encode(self, severity: int, text: bytes, id: int = 0, chunk_seq: int = 0) -> MAVLink_statustext_message:
        """
        Status text message. These messages are printed in yellow in the COMM
        console of QGroundControl. WARNING: They consume quite some
        bandwidth, so use only for important status and error
        messages. If implemented wisely, these messages are buffered
        on the MCU and sent only at a limited rate (e.g. 10 Hz).

        severity                  : Severity of status. Relies on the definitions within RFC-5424. (type:uint8_t, values:MAV_SEVERITY)
        text                      : Status text message, without null termination character (type:char)
        id                        : Unique (opaque) identifier for this statustext message.  May be used to reassemble a logical long-statustext message from a sequence of chunks.  A value of zero indicates this is the only chunk in the sequence and the message can be emitted immediately. (type:uint16_t)
        chunk_seq                 : This chunk's sequence number; indexing is from zero.  Any null character in the text field is taken to mean this was the last chunk. (type:uint8_t)

        """
        return MAVLink_statustext_message(severity, text, id, chunk_seq)

## statustext_send
    def statustext_send(self, severity: int, text: bytes, id: int = 0, chunk_seq: int = 0, force_mavlink1: bool = False) -> None:
        """
        Status text message. These messages are printed in yellow in the COMM
        console of QGroundControl. WARNING: They consume quite some
        bandwidth, so use only for important status and error
        messages. If implemented wisely, these messages are buffered
        on the MCU and sent only at a limited rate (e.g. 10 Hz).

        severity                  : Severity of status. Relies on the definitions within RFC-5424. (type:uint8_t, values:MAV_SEVERITY)
        text                      : Status text message, without null termination character (type:char)
        id                        : Unique (opaque) identifier for this statustext message.  May be used to reassemble a logical long-statustext message from a sequence of chunks.  A value of zero indicates this is the only chunk in the sequence and the message can be emitted immediately. (type:uint16_t)
        chunk_seq                 : This chunk's sequence number; indexing is from zero.  Any null character in the text field is taken to mean this was the last chunk. (type:uint8_t)

        """
        self.send(self.statustext_encode(severity, text, id, chunk_seq), force_mavlink1=force_mavlink1)

## debug_encode
    def debug_encode(self, time_boot_ms: int, ind: int, value: float) -> MAVLink_debug_message:
        """
        Send a debug value. The index is used to discriminate between values.
        These values show up in the plot of QGroundControl as DEBUG N.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        ind                       : index of debug variable (type:uint8_t)
        value                     : DEBUG value (type:float)

        """
        return MAVLink_debug_message(time_boot_ms, ind, value)

## debug_send
    def debug_send(self, time_boot_ms: int, ind: int, value: float, force_mavlink1: bool = False) -> None:
        """
        Send a debug value. The index is used to discriminate between values.
        These values show up in the plot of QGroundControl as DEBUG N.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        ind                       : index of debug variable (type:uint8_t)
        value                     : DEBUG value (type:float)

        """
        self.send(self.debug_encode(time_boot_ms, ind, value), force_mavlink1=force_mavlink1)

## setup_signing_encode
    def setup_signing_encode(self, target_system: int, target_component: int, secret_key: Sequence[int], initial_timestamp: int) -> MAVLink_setup_signing_message:
        """
        Setup a MAVLink2 signing key. If called with secret_key of all zero
        and zero initial_timestamp will disable signing

        target_system             : system id of the target (type:uint8_t)
        target_component          : component ID of the target (type:uint8_t)
        secret_key                : signing key (type:uint8_t)
        initial_timestamp         : initial timestamp (type:uint64_t)

        """
        return MAVLink_setup_signing_message(target_system, target_component, secret_key, initial_timestamp)

## setup_signing_send
    def setup_signing_send(self, target_system: int, target_component: int, secret_key: Sequence[int], initial_timestamp: int, force_mavlink1: bool = False) -> None:
        """
        Setup a MAVLink2 signing key. If called with secret_key of all zero
        and zero initial_timestamp will disable signing

        target_system             : system id of the target (type:uint8_t)
        target_component          : component ID of the target (type:uint8_t)
        secret_key                : signing key (type:uint8_t)
        initial_timestamp         : initial timestamp (type:uint64_t)

        """
        self.send(self.setup_signing_encode(target_system, target_component, secret_key, initial_timestamp), force_mavlink1=force_mavlink1)

## button_change_encode
    def button_change_encode(self, time_boot_ms: int, last_change_ms: int, state: int) -> MAVLink_button_change_message:
        """
        Report button state change.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        last_change_ms            : Time of last change of button state. [ms] (type:uint32_t)
        state                     : Bitmap for state of buttons. (type:uint8_t)

        """
        return MAVLink_button_change_message(time_boot_ms, last_change_ms, state)

## button_change_send
    def button_change_send(self, time_boot_ms: int, last_change_ms: int, state: int, force_mavlink1: bool = False) -> None:
        """
        Report button state change.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        last_change_ms            : Time of last change of button state. [ms] (type:uint32_t)
        state                     : Bitmap for state of buttons. (type:uint8_t)

        """
        self.send(self.button_change_encode(time_boot_ms, last_change_ms, state), force_mavlink1=force_mavlink1)

## play_tune_encode
    def play_tune_encode(self, target_system: int, target_component: int, tune: bytes, tune2: bytes = b"") -> MAVLink_play_tune_message:
        """
        Control vehicle tone generation (buzzer).

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        tune                      : tune in board specific format (type:char)
        tune2                     : tune extension (appended to tune) (type:char)

        """
        return MAVLink_play_tune_message(target_system, target_component, tune, tune2)

## play_tune_send
    def play_tune_send(self, target_system: int, target_component: int, tune: bytes, tune2: bytes = b"", force_mavlink1: bool = False) -> None:
        """
        Control vehicle tone generation (buzzer).

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        tune                      : tune in board specific format (type:char)
        tune2                     : tune extension (appended to tune) (type:char)

        """
        self.send(self.play_tune_encode(target_system, target_component, tune, tune2), force_mavlink1=force_mavlink1)

## camera_information_encode
    def camera_information_encode(self, time_boot_ms: int, vendor_name: Sequence[int], model_name: Sequence[int], firmware_version: int, focal_length: float, sensor_size_h: float, sensor_size_v: float, resolution_h: int, resolution_v: int, lens_id: int, flags: int, cam_definition_version: int, cam_definition_uri: bytes, gimbal_device_id: int = 0) -> MAVLink_camera_information_message:
        """
        Information about a camera. Can be requested with a
        MAV_CMD_REQUEST_MESSAGE command.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        vendor_name               : Name of the camera vendor (type:uint8_t)
        model_name                : Name of the camera model (type:uint8_t)
        firmware_version          : Version of the camera firmware, encoded as: (Dev & 0xff) << 24 | (Patch & 0xff) << 16 | (Minor & 0xff) << 8 | (Major & 0xff). Use 0 if not known. (type:uint32_t)
        focal_length              : Focal length. Use NaN if not known. [mm] (type:float)
        sensor_size_h             : Image sensor size horizontal. Use NaN if not known. [mm] (type:float)
        sensor_size_v             : Image sensor size vertical. Use NaN if not known. [mm] (type:float)
        resolution_h              : Horizontal image resolution. Use 0 if not known. [pix] (type:uint16_t)
        resolution_v              : Vertical image resolution. Use 0 if not known. [pix] (type:uint16_t)
        lens_id                   : Reserved for a lens ID.  Use 0 if not known. (type:uint8_t)
        flags                     : Bitmap of camera capability flags. (type:uint32_t, values:CAMERA_CAP_FLAGS)
        cam_definition_version        : Camera definition version (iteration).  Use 0 if not known. (type:uint16_t)
        cam_definition_uri        : Camera definition URI (if any, otherwise only basic functions will be available). HTTP- (http://) and MAVLink FTP- (mavlinkftp://) formatted URIs are allowed (and both must be supported by any GCS that implements the Camera Protocol). The definition file may be xz compressed, which will be indicated by the file extension .xml.xz (a GCS that implements the protocol must support decompressing the file). The string needs to be zero terminated.  Use a zero-length string if not known. (type:char)
        gimbal_device_id          : Gimbal id of a gimbal associated with this camera. This is the component id of the gimbal device, or 1-6 for non mavlink gimbals. Use 0 if no gimbal is associated with the camera. (type:uint8_t)

        """
        return MAVLink_camera_information_message(time_boot_ms, vendor_name, model_name, firmware_version, focal_length, sensor_size_h, sensor_size_v, resolution_h, resolution_v, lens_id, flags, cam_definition_version, cam_definition_uri, gimbal_device_id)

## camera_information_send
    def camera_information_send(self, time_boot_ms: int, vendor_name: Sequence[int], model_name: Sequence[int], firmware_version: int, focal_length: float, sensor_size_h: float, sensor_size_v: float, resolution_h: int, resolution_v: int, lens_id: int, flags: int, cam_definition_version: int, cam_definition_uri: bytes, gimbal_device_id: int = 0, force_mavlink1: bool = False) -> None:
        """
        Information about a camera. Can be requested with a
        MAV_CMD_REQUEST_MESSAGE command.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        vendor_name               : Name of the camera vendor (type:uint8_t)
        model_name                : Name of the camera model (type:uint8_t)
        firmware_version          : Version of the camera firmware, encoded as: (Dev & 0xff) << 24 | (Patch & 0xff) << 16 | (Minor & 0xff) << 8 | (Major & 0xff). Use 0 if not known. (type:uint32_t)
        focal_length              : Focal length. Use NaN if not known. [mm] (type:float)
        sensor_size_h             : Image sensor size horizontal. Use NaN if not known. [mm] (type:float)
        sensor_size_v             : Image sensor size vertical. Use NaN if not known. [mm] (type:float)
        resolution_h              : Horizontal image resolution. Use 0 if not known. [pix] (type:uint16_t)
        resolution_v              : Vertical image resolution. Use 0 if not known. [pix] (type:uint16_t)
        lens_id                   : Reserved for a lens ID.  Use 0 if not known. (type:uint8_t)
        flags                     : Bitmap of camera capability flags. (type:uint32_t, values:CAMERA_CAP_FLAGS)
        cam_definition_version        : Camera definition version (iteration).  Use 0 if not known. (type:uint16_t)
        cam_definition_uri        : Camera definition URI (if any, otherwise only basic functions will be available). HTTP- (http://) and MAVLink FTP- (mavlinkftp://) formatted URIs are allowed (and both must be supported by any GCS that implements the Camera Protocol). The definition file may be xz compressed, which will be indicated by the file extension .xml.xz (a GCS that implements the protocol must support decompressing the file). The string needs to be zero terminated.  Use a zero-length string if not known. (type:char)
        gimbal_device_id          : Gimbal id of a gimbal associated with this camera. This is the component id of the gimbal device, or 1-6 for non mavlink gimbals. Use 0 if no gimbal is associated with the camera. (type:uint8_t)

        """
        self.send(self.camera_information_encode(time_boot_ms, vendor_name, model_name, firmware_version, focal_length, sensor_size_h, sensor_size_v, resolution_h, resolution_v, lens_id, flags, cam_definition_version, cam_definition_uri, gimbal_device_id), force_mavlink1=force_mavlink1)

## camera_settings_encode
    def camera_settings_encode(self, time_boot_ms: int, mode_id: int, zoomLevel: float = 0, focusLevel: float = 0) -> MAVLink_camera_settings_message:
        """
        Settings of a camera. Can be requested with a MAV_CMD_REQUEST_MESSAGE
        command.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        mode_id                   : Camera mode (type:uint8_t, values:CAMERA_MODE)
        zoomLevel                 : Current zoom level as a percentage of the full range (0.0 to 100.0, NaN if not known) (type:float)
        focusLevel                : Current focus level as a percentage of the full range (0.0 to 100.0, NaN if not known) (type:float)

        """
        return MAVLink_camera_settings_message(time_boot_ms, mode_id, zoomLevel, focusLevel)

## camera_settings_send
    def camera_settings_send(self, time_boot_ms: int, mode_id: int, zoomLevel: float = 0, focusLevel: float = 0, force_mavlink1: bool = False) -> None:
        """
        Settings of a camera. Can be requested with a MAV_CMD_REQUEST_MESSAGE
        command.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        mode_id                   : Camera mode (type:uint8_t, values:CAMERA_MODE)
        zoomLevel                 : Current zoom level as a percentage of the full range (0.0 to 100.0, NaN if not known) (type:float)
        focusLevel                : Current focus level as a percentage of the full range (0.0 to 100.0, NaN if not known) (type:float)

        """
        self.send(self.camera_settings_encode(time_boot_ms, mode_id, zoomLevel, focusLevel), force_mavlink1=force_mavlink1)

## storage_information_encode
    def storage_information_encode(self, time_boot_ms: int, storage_id: int, storage_count: int, status: int, total_capacity: float, used_capacity: float, available_capacity: float, read_speed: float, write_speed: float, type: int = 0, name: bytes = b"") -> MAVLink_storage_information_message:
        """
        Information about a storage medium. This message is sent in response
        to a request with MAV_CMD_REQUEST_MESSAGE and whenever the
        status of the storage changes (STORAGE_STATUS). Use
        MAV_CMD_REQUEST_MESSAGE.param2 to indicate the index/id of
        requested storage: 0 for all, 1 for first, 2 for second, etc.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        storage_id                : Storage ID (1 for first, 2 for second, etc.) (type:uint8_t)
        storage_count             : Number of storage devices (type:uint8_t)
        status                    : Status of storage (type:uint8_t, values:STORAGE_STATUS)
        total_capacity            : Total capacity. If storage is not ready (STORAGE_STATUS_READY) value will be ignored. [MiB] (type:float)
        used_capacity             : Used capacity. If storage is not ready (STORAGE_STATUS_READY) value will be ignored. [MiB] (type:float)
        available_capacity        : Available storage capacity. If storage is not ready (STORAGE_STATUS_READY) value will be ignored. [MiB] (type:float)
        read_speed                : Read speed. [MiB/s] (type:float)
        write_speed               : Write speed. [MiB/s] (type:float)
        type                      : Type of storage (type:uint8_t, values:STORAGE_TYPE)
        name                      : Textual storage name to be used in UI (microSD 1, Internal Memory, etc.) This is a NULL terminated string. If it is exactly 32 characters long, add a terminating NULL. If this string is empty, the generic type is shown to the user. (type:char)

        """
        return MAVLink_storage_information_message(time_boot_ms, storage_id, storage_count, status, total_capacity, used_capacity, available_capacity, read_speed, write_speed, type, name)

## storage_information_send
    def storage_information_send(self, time_boot_ms: int, storage_id: int, storage_count: int, status: int, total_capacity: float, used_capacity: float, available_capacity: float, read_speed: float, write_speed: float, type: int = 0, name: bytes = b"", force_mavlink1: bool = False) -> None:
        """
        Information about a storage medium. This message is sent in response
        to a request with MAV_CMD_REQUEST_MESSAGE and whenever the
        status of the storage changes (STORAGE_STATUS). Use
        MAV_CMD_REQUEST_MESSAGE.param2 to indicate the index/id of
        requested storage: 0 for all, 1 for first, 2 for second, etc.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        storage_id                : Storage ID (1 for first, 2 for second, etc.) (type:uint8_t)
        storage_count             : Number of storage devices (type:uint8_t)
        status                    : Status of storage (type:uint8_t, values:STORAGE_STATUS)
        total_capacity            : Total capacity. If storage is not ready (STORAGE_STATUS_READY) value will be ignored. [MiB] (type:float)
        used_capacity             : Used capacity. If storage is not ready (STORAGE_STATUS_READY) value will be ignored. [MiB] (type:float)
        available_capacity        : Available storage capacity. If storage is not ready (STORAGE_STATUS_READY) value will be ignored. [MiB] (type:float)
        read_speed                : Read speed. [MiB/s] (type:float)
        write_speed               : Write speed. [MiB/s] (type:float)
        type                      : Type of storage (type:uint8_t, values:STORAGE_TYPE)
        name                      : Textual storage name to be used in UI (microSD 1, Internal Memory, etc.) This is a NULL terminated string. If it is exactly 32 characters long, add a terminating NULL. If this string is empty, the generic type is shown to the user. (type:char)

        """
        self.send(self.storage_information_encode(time_boot_ms, storage_id, storage_count, status, total_capacity, used_capacity, available_capacity, read_speed, write_speed, type, name), force_mavlink1=force_mavlink1)

## camera_capture_status_encode
    def camera_capture_status_encode(self, time_boot_ms: int, image_status: int, video_status: int, image_interval: float, recording_time_ms: int, available_capacity: float, image_count: int = 0) -> MAVLink_camera_capture_status_message:
        """
        Information about the status of a capture. Can be requested with a
        MAV_CMD_REQUEST_MESSAGE command.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        image_status              : Current status of image capturing (0: idle, 1: capture in progress, 2: interval set but idle, 3: interval set and capture in progress) (type:uint8_t)
        video_status              : Current status of video capturing (0: idle, 1: capture in progress) (type:uint8_t)
        image_interval            : Image capture interval [s] (type:float)
        recording_time_ms         : Time since recording started [ms] (type:uint32_t)
        available_capacity        : Available storage capacity. [MiB] (type:float)
        image_count               : Total number of images captured ('forever', or until reset using MAV_CMD_STORAGE_FORMAT). (type:int32_t)

        """
        return MAVLink_camera_capture_status_message(time_boot_ms, image_status, video_status, image_interval, recording_time_ms, available_capacity, image_count)

## camera_capture_status_send
    def camera_capture_status_send(self, time_boot_ms: int, image_status: int, video_status: int, image_interval: float, recording_time_ms: int, available_capacity: float, image_count: int = 0, force_mavlink1: bool = False) -> None:
        """
        Information about the status of a capture. Can be requested with a
        MAV_CMD_REQUEST_MESSAGE command.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        image_status              : Current status of image capturing (0: idle, 1: capture in progress, 2: interval set but idle, 3: interval set and capture in progress) (type:uint8_t)
        video_status              : Current status of video capturing (0: idle, 1: capture in progress) (type:uint8_t)
        image_interval            : Image capture interval [s] (type:float)
        recording_time_ms         : Time since recording started [ms] (type:uint32_t)
        available_capacity        : Available storage capacity. [MiB] (type:float)
        image_count               : Total number of images captured ('forever', or until reset using MAV_CMD_STORAGE_FORMAT). (type:int32_t)

        """
        self.send(self.camera_capture_status_encode(time_boot_ms, image_status, video_status, image_interval, recording_time_ms, available_capacity, image_count), force_mavlink1=force_mavlink1)

## camera_image_captured_encode
    def camera_image_captured_encode(self, time_boot_ms: int, time_utc: int, camera_id: int, lat: int, lon: int, alt: int, relative_alt: int, q: Sequence[float], image_index: int, capture_result: int, file_url: bytes) -> MAVLink_camera_image_captured_message:
        """
        Information about a captured image. This is emitted every time a
        message is captured. It may be re-requested using
        MAV_CMD_REQUEST_MESSAGE, using param2 to indicate the sequence
        number for the missing image.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        time_utc                  : Timestamp (time since UNIX epoch) in UTC. 0 for unknown. [us] (type:uint64_t)
        camera_id                 : Deprecated/unused. Component IDs are used to differentiate multiple cameras. (type:uint8_t)
        lat                       : Latitude where image was taken [degE7] (type:int32_t)
        lon                       : Longitude where capture was taken [degE7] (type:int32_t)
        alt                       : Altitude (MSL) where image was taken [mm] (type:int32_t)
        relative_alt              : Altitude above ground [mm] (type:int32_t)
        q                         : Quaternion of camera orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        image_index               : Zero based index of this image (i.e. a new image will have index CAMERA_CAPTURE_STATUS.image count -1) (type:int32_t)
        capture_result            : Image was captured successfully (MAV_BOOL_TRUE). Values not equal to 0 or 1 are invalid. (type:int8_t, values:MAV_BOOL)
        file_url                  : URL of image taken. Either local storage or http://foo.jpg if camera provides an HTTP interface. (type:char)

        """
        return MAVLink_camera_image_captured_message(time_boot_ms, time_utc, camera_id, lat, lon, alt, relative_alt, q, image_index, capture_result, file_url)

## camera_image_captured_send
    def camera_image_captured_send(self, time_boot_ms: int, time_utc: int, camera_id: int, lat: int, lon: int, alt: int, relative_alt: int, q: Sequence[float], image_index: int, capture_result: int, file_url: bytes, force_mavlink1: bool = False) -> None:
        """
        Information about a captured image. This is emitted every time a
        message is captured. It may be re-requested using
        MAV_CMD_REQUEST_MESSAGE, using param2 to indicate the sequence
        number for the missing image.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        time_utc                  : Timestamp (time since UNIX epoch) in UTC. 0 for unknown. [us] (type:uint64_t)
        camera_id                 : Deprecated/unused. Component IDs are used to differentiate multiple cameras. (type:uint8_t)
        lat                       : Latitude where image was taken [degE7] (type:int32_t)
        lon                       : Longitude where capture was taken [degE7] (type:int32_t)
        alt                       : Altitude (MSL) where image was taken [mm] (type:int32_t)
        relative_alt              : Altitude above ground [mm] (type:int32_t)
        q                         : Quaternion of camera orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        image_index               : Zero based index of this image (i.e. a new image will have index CAMERA_CAPTURE_STATUS.image count -1) (type:int32_t)
        capture_result            : Image was captured successfully (MAV_BOOL_TRUE). Values not equal to 0 or 1 are invalid. (type:int8_t, values:MAV_BOOL)
        file_url                  : URL of image taken. Either local storage or http://foo.jpg if camera provides an HTTP interface. (type:char)

        """
        self.send(self.camera_image_captured_encode(time_boot_ms, time_utc, camera_id, lat, lon, alt, relative_alt, q, image_index, capture_result, file_url), force_mavlink1=force_mavlink1)

## flight_information_encode
    def flight_information_encode(self, time_boot_ms: int, arming_time_utc: int, takeoff_time_utc: int, flight_uuid: int) -> MAVLink_flight_information_message:
        """
        Information about flight since last arming.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        arming_time_utc           : Timestamp at arming (time since UNIX epoch) in UTC, 0 for unknown [us] (type:uint64_t)
        takeoff_time_utc          : Timestamp at takeoff (time since UNIX epoch) in UTC, 0 for unknown [us] (type:uint64_t)
        flight_uuid               : Universally unique identifier (UUID) of flight, should correspond to name of log files (type:uint64_t)

        """
        return MAVLink_flight_information_message(time_boot_ms, arming_time_utc, takeoff_time_utc, flight_uuid)

## flight_information_send
    def flight_information_send(self, time_boot_ms: int, arming_time_utc: int, takeoff_time_utc: int, flight_uuid: int, force_mavlink1: bool = False) -> None:
        """
        Information about flight since last arming.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        arming_time_utc           : Timestamp at arming (time since UNIX epoch) in UTC, 0 for unknown [us] (type:uint64_t)
        takeoff_time_utc          : Timestamp at takeoff (time since UNIX epoch) in UTC, 0 for unknown [us] (type:uint64_t)
        flight_uuid               : Universally unique identifier (UUID) of flight, should correspond to name of log files (type:uint64_t)

        """
        self.send(self.flight_information_encode(time_boot_ms, arming_time_utc, takeoff_time_utc, flight_uuid), force_mavlink1=force_mavlink1)

## mount_orientation_encode
    def mount_orientation_encode(self, time_boot_ms: int, roll: float, pitch: float, yaw: float, yaw_absolute: float = 0) -> MAVLink_mount_orientation_message:
        """
        Orientation of a mount

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        roll                      : Roll in global frame (set to NaN for invalid). [deg] (type:float)
        pitch                     : Pitch in global frame (set to NaN for invalid). [deg] (type:float)
        yaw                       : Yaw relative to vehicle (set to NaN for invalid). [deg] (type:float)
        yaw_absolute              : Yaw in absolute frame relative to Earth's North, north is 0 (set to NaN for invalid). [deg] (type:float)

        """
        return MAVLink_mount_orientation_message(time_boot_ms, roll, pitch, yaw, yaw_absolute)

## mount_orientation_send
    def mount_orientation_send(self, time_boot_ms: int, roll: float, pitch: float, yaw: float, yaw_absolute: float = 0, force_mavlink1: bool = False) -> None:
        """
        Orientation of a mount

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        roll                      : Roll in global frame (set to NaN for invalid). [deg] (type:float)
        pitch                     : Pitch in global frame (set to NaN for invalid). [deg] (type:float)
        yaw                       : Yaw relative to vehicle (set to NaN for invalid). [deg] (type:float)
        yaw_absolute              : Yaw in absolute frame relative to Earth's North, north is 0 (set to NaN for invalid). [deg] (type:float)

        """
        self.send(self.mount_orientation_encode(time_boot_ms, roll, pitch, yaw, yaw_absolute), force_mavlink1=force_mavlink1)

## logging_data_encode
    def logging_data_encode(self, target_system: int, target_component: int, sequence: int, length: int, first_message_offset: int, data: Sequence[int]) -> MAVLink_logging_data_message:
        """
        A message containing logged data (see also MAV_CMD_LOGGING_START)

        target_system             : system ID of the target (type:uint8_t)
        target_component          : component ID of the target (type:uint8_t)
        sequence                  : sequence number (can wrap) (type:uint16_t)
        length                    : data length [bytes] (type:uint8_t)
        first_message_offset        : offset into data where first message starts. This can be used for recovery, when a previous message got lost (set to UINT8_MAX if no start exists). [bytes] (type:uint8_t)
        data                      : logged data (type:uint8_t)

        """
        return MAVLink_logging_data_message(target_system, target_component, sequence, length, first_message_offset, data)

## logging_data_send
    def logging_data_send(self, target_system: int, target_component: int, sequence: int, length: int, first_message_offset: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        A message containing logged data (see also MAV_CMD_LOGGING_START)

        target_system             : system ID of the target (type:uint8_t)
        target_component          : component ID of the target (type:uint8_t)
        sequence                  : sequence number (can wrap) (type:uint16_t)
        length                    : data length [bytes] (type:uint8_t)
        first_message_offset        : offset into data where first message starts. This can be used for recovery, when a previous message got lost (set to UINT8_MAX if no start exists). [bytes] (type:uint8_t)
        data                      : logged data (type:uint8_t)

        """
        self.send(self.logging_data_encode(target_system, target_component, sequence, length, first_message_offset, data), force_mavlink1=force_mavlink1)

## logging_data_acked_encode
    def logging_data_acked_encode(self, target_system: int, target_component: int, sequence: int, length: int, first_message_offset: int, data: Sequence[int]) -> MAVLink_logging_data_acked_message:
        """
        A message containing logged data which requires a LOGGING_ACK to be
        sent back

        target_system             : system ID of the target (type:uint8_t)
        target_component          : component ID of the target (type:uint8_t)
        sequence                  : sequence number (can wrap) (type:uint16_t)
        length                    : data length [bytes] (type:uint8_t)
        first_message_offset        : offset into data where first message starts. This can be used for recovery, when a previous message got lost (set to UINT8_MAX if no start exists). [bytes] (type:uint8_t)
        data                      : logged data (type:uint8_t)

        """
        return MAVLink_logging_data_acked_message(target_system, target_component, sequence, length, first_message_offset, data)

## logging_data_acked_send
    def logging_data_acked_send(self, target_system: int, target_component: int, sequence: int, length: int, first_message_offset: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        A message containing logged data which requires a LOGGING_ACK to be
        sent back

        target_system             : system ID of the target (type:uint8_t)
        target_component          : component ID of the target (type:uint8_t)
        sequence                  : sequence number (can wrap) (type:uint16_t)
        length                    : data length [bytes] (type:uint8_t)
        first_message_offset        : offset into data where first message starts. This can be used for recovery, when a previous message got lost (set to UINT8_MAX if no start exists). [bytes] (type:uint8_t)
        data                      : logged data (type:uint8_t)

        """
        self.send(self.logging_data_acked_encode(target_system, target_component, sequence, length, first_message_offset, data), force_mavlink1=force_mavlink1)

## logging_ack_encode
    def logging_ack_encode(self, target_system: int, target_component: int, sequence: int) -> MAVLink_logging_ack_message:
        """
        An ack for a LOGGING_DATA_ACKED message

        target_system             : system ID of the target (type:uint8_t)
        target_component          : component ID of the target (type:uint8_t)
        sequence                  : sequence number (must match the one in LOGGING_DATA_ACKED) (type:uint16_t)

        """
        return MAVLink_logging_ack_message(target_system, target_component, sequence)

## logging_ack_send
    def logging_ack_send(self, target_system: int, target_component: int, sequence: int, force_mavlink1: bool = False) -> None:
        """
        An ack for a LOGGING_DATA_ACKED message

        target_system             : system ID of the target (type:uint8_t)
        target_component          : component ID of the target (type:uint8_t)
        sequence                  : sequence number (must match the one in LOGGING_DATA_ACKED) (type:uint16_t)

        """
        self.send(self.logging_ack_encode(target_system, target_component, sequence), force_mavlink1=force_mavlink1)

## video_stream_information_encode
    def video_stream_information_encode(self, stream_id: int, count: int, type: int, flags: int, framerate: float, resolution_h: int, resolution_v: int, bitrate: int, rotation: int, hfov: int, name: bytes, uri: bytes, encoding: int = 0) -> MAVLink_video_stream_information_message:
        """
        Information about video stream. It may be requested using
        MAV_CMD_REQUEST_MESSAGE, where param2 indicates the video
        stream id: 0 for all streams, 1 for first, 2 for second, etc.

        stream_id                 : Video Stream ID (1 for first, 2 for second, etc.) (type:uint8_t)
        count                     : Number of streams available. (type:uint8_t)
        type                      : Type of stream. (type:uint8_t, values:VIDEO_STREAM_TYPE)
        flags                     : Bitmap of stream status flags. (type:uint16_t, values:VIDEO_STREAM_STATUS_FLAGS)
        framerate                 : Frame rate. [Hz] (type:float)
        resolution_h              : Horizontal resolution. [pix] (type:uint16_t)
        resolution_v              : Vertical resolution. [pix] (type:uint16_t)
        bitrate                   : Bit rate. [bits/s] (type:uint32_t)
        rotation                  : Video image rotation clockwise. [deg] (type:uint16_t)
        hfov                      : Horizontal Field of view. [deg] (type:uint16_t)
        name                      : Stream name. (type:char)
        uri                       : Video stream URI (TCP or RTSP URI ground station should connect to) or port number (UDP port ground station should listen to). (type:char)
        encoding                  : Encoding of stream. (type:uint8_t, values:VIDEO_STREAM_ENCODING)

        """
        return MAVLink_video_stream_information_message(stream_id, count, type, flags, framerate, resolution_h, resolution_v, bitrate, rotation, hfov, name, uri, encoding)

## video_stream_information_send
    def video_stream_information_send(self, stream_id: int, count: int, type: int, flags: int, framerate: float, resolution_h: int, resolution_v: int, bitrate: int, rotation: int, hfov: int, name: bytes, uri: bytes, encoding: int = 0, force_mavlink1: bool = False) -> None:
        """
        Information about video stream. It may be requested using
        MAV_CMD_REQUEST_MESSAGE, where param2 indicates the video
        stream id: 0 for all streams, 1 for first, 2 for second, etc.

        stream_id                 : Video Stream ID (1 for first, 2 for second, etc.) (type:uint8_t)
        count                     : Number of streams available. (type:uint8_t)
        type                      : Type of stream. (type:uint8_t, values:VIDEO_STREAM_TYPE)
        flags                     : Bitmap of stream status flags. (type:uint16_t, values:VIDEO_STREAM_STATUS_FLAGS)
        framerate                 : Frame rate. [Hz] (type:float)
        resolution_h              : Horizontal resolution. [pix] (type:uint16_t)
        resolution_v              : Vertical resolution. [pix] (type:uint16_t)
        bitrate                   : Bit rate. [bits/s] (type:uint32_t)
        rotation                  : Video image rotation clockwise. [deg] (type:uint16_t)
        hfov                      : Horizontal Field of view. [deg] (type:uint16_t)
        name                      : Stream name. (type:char)
        uri                       : Video stream URI (TCP or RTSP URI ground station should connect to) or port number (UDP port ground station should listen to). (type:char)
        encoding                  : Encoding of stream. (type:uint8_t, values:VIDEO_STREAM_ENCODING)

        """
        self.send(self.video_stream_information_encode(stream_id, count, type, flags, framerate, resolution_h, resolution_v, bitrate, rotation, hfov, name, uri, encoding), force_mavlink1=force_mavlink1)

## video_stream_status_encode
    def video_stream_status_encode(self, stream_id: int, flags: int, framerate: float, resolution_h: int, resolution_v: int, bitrate: int, rotation: int, hfov: int) -> MAVLink_video_stream_status_message:
        """
        Information about the status of a video stream. It may be requested
        using MAV_CMD_REQUEST_MESSAGE.

        stream_id                 : Video Stream ID (1 for first, 2 for second, etc.) (type:uint8_t)
        flags                     : Bitmap of stream status flags (type:uint16_t, values:VIDEO_STREAM_STATUS_FLAGS)
        framerate                 : Frame rate [Hz] (type:float)
        resolution_h              : Horizontal resolution [pix] (type:uint16_t)
        resolution_v              : Vertical resolution [pix] (type:uint16_t)
        bitrate                   : Bit rate [bits/s] (type:uint32_t)
        rotation                  : Video image rotation clockwise [deg] (type:uint16_t)
        hfov                      : Horizontal Field of view [deg] (type:uint16_t)

        """
        return MAVLink_video_stream_status_message(stream_id, flags, framerate, resolution_h, resolution_v, bitrate, rotation, hfov)

## video_stream_status_send
    def video_stream_status_send(self, stream_id: int, flags: int, framerate: float, resolution_h: int, resolution_v: int, bitrate: int, rotation: int, hfov: int, force_mavlink1: bool = False) -> None:
        """
        Information about the status of a video stream. It may be requested
        using MAV_CMD_REQUEST_MESSAGE.

        stream_id                 : Video Stream ID (1 for first, 2 for second, etc.) (type:uint8_t)
        flags                     : Bitmap of stream status flags (type:uint16_t, values:VIDEO_STREAM_STATUS_FLAGS)
        framerate                 : Frame rate [Hz] (type:float)
        resolution_h              : Horizontal resolution [pix] (type:uint16_t)
        resolution_v              : Vertical resolution [pix] (type:uint16_t)
        bitrate                   : Bit rate [bits/s] (type:uint32_t)
        rotation                  : Video image rotation clockwise [deg] (type:uint16_t)
        hfov                      : Horizontal Field of view [deg] (type:uint16_t)

        """
        self.send(self.video_stream_status_encode(stream_id, flags, framerate, resolution_h, resolution_v, bitrate, rotation, hfov), force_mavlink1=force_mavlink1)

## camera_fov_status_encode
    def camera_fov_status_encode(self, time_boot_ms: int, lat_camera: int, lon_camera: int, alt_camera: int, lat_image: int, lon_image: int, alt_image: int, q: Sequence[float], hfov: float, vfov: float) -> MAVLink_camera_fov_status_message:
        """
        Information about the field of view of a camera. Can be requested with
        a MAV_CMD_REQUEST_MESSAGE command.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        lat_camera                : Latitude of camera (INT32_MAX if unknown). [degE7] (type:int32_t)
        lon_camera                : Longitude of camera (INT32_MAX if unknown). [degE7] (type:int32_t)
        alt_camera                : Altitude (MSL) of camera (INT32_MAX if unknown). [mm] (type:int32_t)
        lat_image                 : Latitude of center of image (INT32_MAX if unknown, INT32_MIN if at infinity, not intersecting with horizon). [degE7] (type:int32_t)
        lon_image                 : Longitude of center of image (INT32_MAX if unknown, INT32_MIN if at infinity, not intersecting with horizon). [degE7] (type:int32_t)
        alt_image                 : Altitude (MSL) of center of image (INT32_MAX if unknown, INT32_MIN if at infinity, not intersecting with horizon). [mm] (type:int32_t)
        q                         : Quaternion of camera orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        hfov                      : Horizontal field of view (NaN if unknown). [deg] (type:float)
        vfov                      : Vertical field of view (NaN if unknown). [deg] (type:float)

        """
        return MAVLink_camera_fov_status_message(time_boot_ms, lat_camera, lon_camera, alt_camera, lat_image, lon_image, alt_image, q, hfov, vfov)

## camera_fov_status_send
    def camera_fov_status_send(self, time_boot_ms: int, lat_camera: int, lon_camera: int, alt_camera: int, lat_image: int, lon_image: int, alt_image: int, q: Sequence[float], hfov: float, vfov: float, force_mavlink1: bool = False) -> None:
        """
        Information about the field of view of a camera. Can be requested with
        a MAV_CMD_REQUEST_MESSAGE command.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        lat_camera                : Latitude of camera (INT32_MAX if unknown). [degE7] (type:int32_t)
        lon_camera                : Longitude of camera (INT32_MAX if unknown). [degE7] (type:int32_t)
        alt_camera                : Altitude (MSL) of camera (INT32_MAX if unknown). [mm] (type:int32_t)
        lat_image                 : Latitude of center of image (INT32_MAX if unknown, INT32_MIN if at infinity, not intersecting with horizon). [degE7] (type:int32_t)
        lon_image                 : Longitude of center of image (INT32_MAX if unknown, INT32_MIN if at infinity, not intersecting with horizon). [degE7] (type:int32_t)
        alt_image                 : Altitude (MSL) of center of image (INT32_MAX if unknown, INT32_MIN if at infinity, not intersecting with horizon). [mm] (type:int32_t)
        q                         : Quaternion of camera orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0) (type:float)
        hfov                      : Horizontal field of view (NaN if unknown). [deg] (type:float)
        vfov                      : Vertical field of view (NaN if unknown). [deg] (type:float)

        """
        self.send(self.camera_fov_status_encode(time_boot_ms, lat_camera, lon_camera, alt_camera, lat_image, lon_image, alt_image, q, hfov, vfov), force_mavlink1=force_mavlink1)

## camera_tracking_image_status_encode
    def camera_tracking_image_status_encode(self, tracking_status: int, tracking_mode: int, target_data: int, point_x: float, point_y: float, radius: float, rec_top_x: float, rec_top_y: float, rec_bottom_x: float, rec_bottom_y: float) -> MAVLink_camera_tracking_image_status_message:
        """
        Camera tracking status, sent while in active tracking. Use
        MAV_CMD_SET_MESSAGE_INTERVAL to define message interval.

        tracking_status           : Current tracking status (type:uint8_t, values:CAMERA_TRACKING_STATUS_FLAGS)
        tracking_mode             : Current tracking mode (type:uint8_t, values:CAMERA_TRACKING_MODE)
        target_data               : Defines location of target data (type:uint8_t, values:CAMERA_TRACKING_TARGET_DATA)
        point_x                   : Current tracked point x value if CAMERA_TRACKING_MODE_POINT (normalized 0..1, 0 is left, 1 is right), NAN if unknown (type:float)
        point_y                   : Current tracked point y value if CAMERA_TRACKING_MODE_POINT (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown (type:float)
        radius                    : Current tracked radius if CAMERA_TRACKING_MODE_POINT (normalized 0..1, 0 is image left, 1 is image right), NAN if unknown (type:float)
        rec_top_x                 : Current tracked rectangle top x value if CAMERA_TRACKING_MODE_RECTANGLE (normalized 0..1, 0 is left, 1 is right), NAN if unknown (type:float)
        rec_top_y                 : Current tracked rectangle top y value if CAMERA_TRACKING_MODE_RECTANGLE (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown (type:float)
        rec_bottom_x              : Current tracked rectangle bottom x value if CAMERA_TRACKING_MODE_RECTANGLE (normalized 0..1, 0 is left, 1 is right), NAN if unknown (type:float)
        rec_bottom_y              : Current tracked rectangle bottom y value if CAMERA_TRACKING_MODE_RECTANGLE (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown (type:float)

        """
        return MAVLink_camera_tracking_image_status_message(tracking_status, tracking_mode, target_data, point_x, point_y, radius, rec_top_x, rec_top_y, rec_bottom_x, rec_bottom_y)

## camera_tracking_image_status_send
    def camera_tracking_image_status_send(self, tracking_status: int, tracking_mode: int, target_data: int, point_x: float, point_y: float, radius: float, rec_top_x: float, rec_top_y: float, rec_bottom_x: float, rec_bottom_y: float, force_mavlink1: bool = False) -> None:
        """
        Camera tracking status, sent while in active tracking. Use
        MAV_CMD_SET_MESSAGE_INTERVAL to define message interval.

        tracking_status           : Current tracking status (type:uint8_t, values:CAMERA_TRACKING_STATUS_FLAGS)
        tracking_mode             : Current tracking mode (type:uint8_t, values:CAMERA_TRACKING_MODE)
        target_data               : Defines location of target data (type:uint8_t, values:CAMERA_TRACKING_TARGET_DATA)
        point_x                   : Current tracked point x value if CAMERA_TRACKING_MODE_POINT (normalized 0..1, 0 is left, 1 is right), NAN if unknown (type:float)
        point_y                   : Current tracked point y value if CAMERA_TRACKING_MODE_POINT (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown (type:float)
        radius                    : Current tracked radius if CAMERA_TRACKING_MODE_POINT (normalized 0..1, 0 is image left, 1 is image right), NAN if unknown (type:float)
        rec_top_x                 : Current tracked rectangle top x value if CAMERA_TRACKING_MODE_RECTANGLE (normalized 0..1, 0 is left, 1 is right), NAN if unknown (type:float)
        rec_top_y                 : Current tracked rectangle top y value if CAMERA_TRACKING_MODE_RECTANGLE (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown (type:float)
        rec_bottom_x              : Current tracked rectangle bottom x value if CAMERA_TRACKING_MODE_RECTANGLE (normalized 0..1, 0 is left, 1 is right), NAN if unknown (type:float)
        rec_bottom_y              : Current tracked rectangle bottom y value if CAMERA_TRACKING_MODE_RECTANGLE (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown (type:float)

        """
        self.send(self.camera_tracking_image_status_encode(tracking_status, tracking_mode, target_data, point_x, point_y, radius, rec_top_x, rec_top_y, rec_bottom_x, rec_bottom_y), force_mavlink1=force_mavlink1)

## camera_tracking_geo_status_encode
    def camera_tracking_geo_status_encode(self, tracking_status: int, lat: int, lon: int, alt: float, h_acc: float, v_acc: float, vel_n: float, vel_e: float, vel_d: float, vel_acc: float, dist: float, hdg: float, hdg_acc: float) -> MAVLink_camera_tracking_geo_status_message:
        """
        Camera tracking status, sent while in active tracking. Use
        MAV_CMD_SET_MESSAGE_INTERVAL to define message interval.

        tracking_status           : Current tracking status (type:uint8_t, values:CAMERA_TRACKING_STATUS_FLAGS)
        lat                       : Latitude of tracked object [degE7] (type:int32_t)
        lon                       : Longitude of tracked object [degE7] (type:int32_t)
        alt                       : Altitude of tracked object(AMSL, WGS84) [m] (type:float)
        h_acc                     : Horizontal accuracy. NAN if unknown [m] (type:float)
        v_acc                     : Vertical accuracy. NAN if unknown [m] (type:float)
        vel_n                     : North velocity of tracked object. NAN if unknown [m/s] (type:float)
        vel_e                     : East velocity of tracked object. NAN if unknown [m/s] (type:float)
        vel_d                     : Down velocity of tracked object. NAN if unknown [m/s] (type:float)
        vel_acc                   : Velocity accuracy. NAN if unknown [m/s] (type:float)
        dist                      : Distance between camera and tracked object. NAN if unknown [m] (type:float)
        hdg                       : Heading in radians, in NED. NAN if unknown [rad] (type:float)
        hdg_acc                   : Accuracy of heading, in NED. NAN if unknown [rad] (type:float)

        """
        return MAVLink_camera_tracking_geo_status_message(tracking_status, lat, lon, alt, h_acc, v_acc, vel_n, vel_e, vel_d, vel_acc, dist, hdg, hdg_acc)

## camera_tracking_geo_status_send
    def camera_tracking_geo_status_send(self, tracking_status: int, lat: int, lon: int, alt: float, h_acc: float, v_acc: float, vel_n: float, vel_e: float, vel_d: float, vel_acc: float, dist: float, hdg: float, hdg_acc: float, force_mavlink1: bool = False) -> None:
        """
        Camera tracking status, sent while in active tracking. Use
        MAV_CMD_SET_MESSAGE_INTERVAL to define message interval.

        tracking_status           : Current tracking status (type:uint8_t, values:CAMERA_TRACKING_STATUS_FLAGS)
        lat                       : Latitude of tracked object [degE7] (type:int32_t)
        lon                       : Longitude of tracked object [degE7] (type:int32_t)
        alt                       : Altitude of tracked object(AMSL, WGS84) [m] (type:float)
        h_acc                     : Horizontal accuracy. NAN if unknown [m] (type:float)
        v_acc                     : Vertical accuracy. NAN if unknown [m] (type:float)
        vel_n                     : North velocity of tracked object. NAN if unknown [m/s] (type:float)
        vel_e                     : East velocity of tracked object. NAN if unknown [m/s] (type:float)
        vel_d                     : Down velocity of tracked object. NAN if unknown [m/s] (type:float)
        vel_acc                   : Velocity accuracy. NAN if unknown [m/s] (type:float)
        dist                      : Distance between camera and tracked object. NAN if unknown [m] (type:float)
        hdg                       : Heading in radians, in NED. NAN if unknown [rad] (type:float)
        hdg_acc                   : Accuracy of heading, in NED. NAN if unknown [rad] (type:float)

        """
        self.send(self.camera_tracking_geo_status_encode(tracking_status, lat, lon, alt, h_acc, v_acc, vel_n, vel_e, vel_d, vel_acc, dist, hdg, hdg_acc), force_mavlink1=force_mavlink1)

## camera_thermal_range_encode
    def camera_thermal_range_encode(self, time_boot_ms: int, stream_id: int, camera_device_id: int, max: float, max_point_x: float, max_point_y: float, min: float, min_point_x: float, min_point_y: float) -> MAVLink_camera_thermal_range_message:
        """
        Camera absolute thermal range. This can be streamed when the
        associated `VIDEO_STREAM_STATUS.flag` bit
        `VIDEO_STREAM_STATUS_FLAGS_THERMAL_RANGE_ENABLED` is set, but
        a GCS may choose to only request it for the current active
        stream. Use MAV_CMD_SET_MESSAGE_INTERVAL to define message
        interval (param3 indicates the stream id of the current
        camera, or 0 for all streams, param4 indicates the target
        camera_device_id for autopilot-attached cameras or 0 for
        MAVLink cameras).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        stream_id                 : Video Stream ID (1 for first, 2 for second, etc.) (type:uint8_t)
        camera_device_id          : Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). (type:uint8_t)
        max                       : Temperature max. [degC] (type:float)
        max_point_x               : Temperature max point x value (normalized 0..1, 0 is left, 1 is right), NAN if unknown. (type:float)
        max_point_y               : Temperature max point y value (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown. (type:float)
        min                       : Temperature min. [degC] (type:float)
        min_point_x               : Temperature min point x value (normalized 0..1, 0 is left, 1 is right), NAN if unknown. (type:float)
        min_point_y               : Temperature min point y value (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown. (type:float)

        """
        return MAVLink_camera_thermal_range_message(time_boot_ms, stream_id, camera_device_id, max, max_point_x, max_point_y, min, min_point_x, min_point_y)

## camera_thermal_range_send
    def camera_thermal_range_send(self, time_boot_ms: int, stream_id: int, camera_device_id: int, max: float, max_point_x: float, max_point_y: float, min: float, min_point_x: float, min_point_y: float, force_mavlink1: bool = False) -> None:
        """
        Camera absolute thermal range. This can be streamed when the
        associated `VIDEO_STREAM_STATUS.flag` bit
        `VIDEO_STREAM_STATUS_FLAGS_THERMAL_RANGE_ENABLED` is set, but
        a GCS may choose to only request it for the current active
        stream. Use MAV_CMD_SET_MESSAGE_INTERVAL to define message
        interval (param3 indicates the stream id of the current
        camera, or 0 for all streams, param4 indicates the target
        camera_device_id for autopilot-attached cameras or 0 for
        MAVLink cameras).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        stream_id                 : Video Stream ID (1 for first, 2 for second, etc.) (type:uint8_t)
        camera_device_id          : Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). (type:uint8_t)
        max                       : Temperature max. [degC] (type:float)
        max_point_x               : Temperature max point x value (normalized 0..1, 0 is left, 1 is right), NAN if unknown. (type:float)
        max_point_y               : Temperature max point y value (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown. (type:float)
        min                       : Temperature min. [degC] (type:float)
        min_point_x               : Temperature min point x value (normalized 0..1, 0 is left, 1 is right), NAN if unknown. (type:float)
        min_point_y               : Temperature min point y value (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown. (type:float)

        """
        self.send(self.camera_thermal_range_encode(time_boot_ms, stream_id, camera_device_id, max, max_point_x, max_point_y, min, min_point_x, min_point_y), force_mavlink1=force_mavlink1)

## gimbal_manager_information_encode
    def gimbal_manager_information_encode(self, time_boot_ms: int, cap_flags: int, gimbal_device_id: int, roll_min: float, roll_max: float, pitch_min: float, pitch_max: float, yaw_min: float, yaw_max: float) -> MAVLink_gimbal_manager_information_message:
        """
        Information about a high level gimbal manager. This message should be
        requested by a ground station using MAV_CMD_REQUEST_MESSAGE.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        cap_flags                 : Bitmap of gimbal capability flags. (type:uint32_t, values:GIMBAL_MANAGER_CAP_FLAGS)
        gimbal_device_id          : Gimbal device ID that this gimbal manager is responsible for. Component ID of gimbal device (or 1-6 for non-MAVLink gimbal). (type:uint8_t)
        roll_min                  : Minimum hardware roll angle (positive: rolling to the right, negative: rolling to the left) [rad] (type:float)
        roll_max                  : Maximum hardware roll angle (positive: rolling to the right, negative: rolling to the left) [rad] (type:float)
        pitch_min                 : Minimum pitch angle (positive: up, negative: down) [rad] (type:float)
        pitch_max                 : Maximum pitch angle (positive: up, negative: down) [rad] (type:float)
        yaw_min                   : Minimum yaw angle (positive: to the right, negative: to the left) [rad] (type:float)
        yaw_max                   : Maximum yaw angle (positive: to the right, negative: to the left) [rad] (type:float)

        """
        return MAVLink_gimbal_manager_information_message(time_boot_ms, cap_flags, gimbal_device_id, roll_min, roll_max, pitch_min, pitch_max, yaw_min, yaw_max)

## gimbal_manager_information_send
    def gimbal_manager_information_send(self, time_boot_ms: int, cap_flags: int, gimbal_device_id: int, roll_min: float, roll_max: float, pitch_min: float, pitch_max: float, yaw_min: float, yaw_max: float, force_mavlink1: bool = False) -> None:
        """
        Information about a high level gimbal manager. This message should be
        requested by a ground station using MAV_CMD_REQUEST_MESSAGE.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        cap_flags                 : Bitmap of gimbal capability flags. (type:uint32_t, values:GIMBAL_MANAGER_CAP_FLAGS)
        gimbal_device_id          : Gimbal device ID that this gimbal manager is responsible for. Component ID of gimbal device (or 1-6 for non-MAVLink gimbal). (type:uint8_t)
        roll_min                  : Minimum hardware roll angle (positive: rolling to the right, negative: rolling to the left) [rad] (type:float)
        roll_max                  : Maximum hardware roll angle (positive: rolling to the right, negative: rolling to the left) [rad] (type:float)
        pitch_min                 : Minimum pitch angle (positive: up, negative: down) [rad] (type:float)
        pitch_max                 : Maximum pitch angle (positive: up, negative: down) [rad] (type:float)
        yaw_min                   : Minimum yaw angle (positive: to the right, negative: to the left) [rad] (type:float)
        yaw_max                   : Maximum yaw angle (positive: to the right, negative: to the left) [rad] (type:float)

        """
        self.send(self.gimbal_manager_information_encode(time_boot_ms, cap_flags, gimbal_device_id, roll_min, roll_max, pitch_min, pitch_max, yaw_min, yaw_max), force_mavlink1=force_mavlink1)

## gimbal_manager_status_encode
    def gimbal_manager_status_encode(self, time_boot_ms: int, flags: int, gimbal_device_id: int, primary_control_sysid: int, primary_control_compid: int, secondary_control_sysid: int, secondary_control_compid: int) -> MAVLink_gimbal_manager_status_message:
        """
        Current status about a high level gimbal manager. This message should
        be broadcast at a low regular rate (e.g. 5Hz).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        flags                     : High level gimbal manager flags currently applied. (type:uint32_t, values:GIMBAL_MANAGER_FLAGS)
        gimbal_device_id          : Gimbal device ID that this gimbal manager is responsible for. Component ID of gimbal device (or 1-6 for non-MAVLink gimbal). (type:uint8_t)
        primary_control_sysid        : System ID of MAVLink component with primary control, 0 for none. (type:uint8_t)
        primary_control_compid        : Component ID of MAVLink component with primary control, 0 for none. (type:uint8_t)
        secondary_control_sysid        : System ID of MAVLink component with secondary control, 0 for none. (type:uint8_t)
        secondary_control_compid        : Component ID of MAVLink component with secondary control, 0 for none. (type:uint8_t)

        """
        return MAVLink_gimbal_manager_status_message(time_boot_ms, flags, gimbal_device_id, primary_control_sysid, primary_control_compid, secondary_control_sysid, secondary_control_compid)

## gimbal_manager_status_send
    def gimbal_manager_status_send(self, time_boot_ms: int, flags: int, gimbal_device_id: int, primary_control_sysid: int, primary_control_compid: int, secondary_control_sysid: int, secondary_control_compid: int, force_mavlink1: bool = False) -> None:
        """
        Current status about a high level gimbal manager. This message should
        be broadcast at a low regular rate (e.g. 5Hz).

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        flags                     : High level gimbal manager flags currently applied. (type:uint32_t, values:GIMBAL_MANAGER_FLAGS)
        gimbal_device_id          : Gimbal device ID that this gimbal manager is responsible for. Component ID of gimbal device (or 1-6 for non-MAVLink gimbal). (type:uint8_t)
        primary_control_sysid        : System ID of MAVLink component with primary control, 0 for none. (type:uint8_t)
        primary_control_compid        : Component ID of MAVLink component with primary control, 0 for none. (type:uint8_t)
        secondary_control_sysid        : System ID of MAVLink component with secondary control, 0 for none. (type:uint8_t)
        secondary_control_compid        : Component ID of MAVLink component with secondary control, 0 for none. (type:uint8_t)

        """
        self.send(self.gimbal_manager_status_encode(time_boot_ms, flags, gimbal_device_id, primary_control_sysid, primary_control_compid, secondary_control_sysid, secondary_control_compid), force_mavlink1=force_mavlink1)

## gimbal_manager_set_attitude_encode
    def gimbal_manager_set_attitude_encode(self, target_system: int, target_component: int, flags: int, gimbal_device_id: int, q: Sequence[float], angular_velocity_x: float, angular_velocity_y: float, angular_velocity_z: float) -> MAVLink_gimbal_manager_set_attitude_message:
        """
        High level message to control a gimbal's attitude. This message is to
        be sent to the gimbal manager (e.g. from a ground station).
        Angles and rates can be set to NaN according to use case.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        flags                     : High level gimbal manager flags to use. (type:uint32_t, values:GIMBAL_MANAGER_FLAGS)
        gimbal_device_id          : Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). (type:uint8_t)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation, the frame is depends on whether the flag GIMBAL_MANAGER_FLAGS_YAW_LOCK is set) (type:float)
        angular_velocity_x        : X component of angular velocity, positive is rolling to the right, NaN to be ignored. [rad/s] (type:float)
        angular_velocity_y        : Y component of angular velocity, positive is pitching up, NaN to be ignored. [rad/s] (type:float)
        angular_velocity_z        : Z component of angular velocity, positive is yawing to the right, NaN to be ignored. [rad/s] (type:float)

        """
        return MAVLink_gimbal_manager_set_attitude_message(target_system, target_component, flags, gimbal_device_id, q, angular_velocity_x, angular_velocity_y, angular_velocity_z)

## gimbal_manager_set_attitude_send
    def gimbal_manager_set_attitude_send(self, target_system: int, target_component: int, flags: int, gimbal_device_id: int, q: Sequence[float], angular_velocity_x: float, angular_velocity_y: float, angular_velocity_z: float, force_mavlink1: bool = False) -> None:
        """
        High level message to control a gimbal's attitude. This message is to
        be sent to the gimbal manager (e.g. from a ground station).
        Angles and rates can be set to NaN according to use case.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        flags                     : High level gimbal manager flags to use. (type:uint32_t, values:GIMBAL_MANAGER_FLAGS)
        gimbal_device_id          : Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). (type:uint8_t)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation, the frame is depends on whether the flag GIMBAL_MANAGER_FLAGS_YAW_LOCK is set) (type:float)
        angular_velocity_x        : X component of angular velocity, positive is rolling to the right, NaN to be ignored. [rad/s] (type:float)
        angular_velocity_y        : Y component of angular velocity, positive is pitching up, NaN to be ignored. [rad/s] (type:float)
        angular_velocity_z        : Z component of angular velocity, positive is yawing to the right, NaN to be ignored. [rad/s] (type:float)

        """
        self.send(self.gimbal_manager_set_attitude_encode(target_system, target_component, flags, gimbal_device_id, q, angular_velocity_x, angular_velocity_y, angular_velocity_z), force_mavlink1=force_mavlink1)

## gimbal_device_information_encode
    def gimbal_device_information_encode(self, time_boot_ms: int, vendor_name: bytes, model_name: bytes, custom_name: bytes, firmware_version: int, hardware_version: int, uid: int, cap_flags: int, custom_cap_flags: int, roll_min: float, roll_max: float, pitch_min: float, pitch_max: float, yaw_min: float, yaw_max: float, gimbal_device_id: int = 0) -> MAVLink_gimbal_device_information_message:
        """
        Information about a low level gimbal. This message should be requested
        by the gimbal manager or a ground station using
        MAV_CMD_REQUEST_MESSAGE. The maximum angles and rates are the
        limits by hardware. However, the limits by software used are
        likely different/smaller and dependent on mode/settings/etc..

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        vendor_name               : Name of the gimbal vendor. (type:char)
        model_name                : Name of the gimbal model. (type:char)
        custom_name               : Custom name of the gimbal given to it by the user. (type:char)
        firmware_version          : Version of the gimbal firmware, encoded as: (Dev & 0xff) << 24 | (Patch & 0xff) << 16 | (Minor & 0xff) << 8 | (Major & 0xff). (type:uint32_t)
        hardware_version          : Version of the gimbal hardware, encoded as: (Dev & 0xff) << 24 | (Patch & 0xff) << 16 | (Minor & 0xff) << 8 | (Major & 0xff). (type:uint32_t)
        uid                       : UID of gimbal hardware (0 if unknown). (type:uint64_t)
        cap_flags                 : Bitmap of gimbal capability flags. (type:uint16_t, values:GIMBAL_DEVICE_CAP_FLAGS)
        custom_cap_flags          : Bitmap for use for gimbal-specific capability flags. (type:uint16_t)
        roll_min                  : Minimum hardware roll angle (positive: rolling to the right, negative: rolling to the left). NAN if unknown. [rad] (type:float)
        roll_max                  : Maximum hardware roll angle (positive: rolling to the right, negative: rolling to the left). NAN if unknown. [rad] (type:float)
        pitch_min                 : Minimum hardware pitch angle (positive: up, negative: down). NAN if unknown. [rad] (type:float)
        pitch_max                 : Maximum hardware pitch angle (positive: up, negative: down). NAN if unknown. [rad] (type:float)
        yaw_min                   : Minimum hardware yaw angle (positive: to the right, negative: to the left). NAN if unknown. [rad] (type:float)
        yaw_max                   : Maximum hardware yaw angle (positive: to the right, negative: to the left). NAN if unknown. [rad] (type:float)
        gimbal_device_id          : This field is to be used if the gimbal manager and the gimbal device are the same component and hence have the same component ID. This field is then set to a number between 1-6. If the component ID is separate, this field is not required and must be set to 0. (type:uint8_t)

        """
        return MAVLink_gimbal_device_information_message(time_boot_ms, vendor_name, model_name, custom_name, firmware_version, hardware_version, uid, cap_flags, custom_cap_flags, roll_min, roll_max, pitch_min, pitch_max, yaw_min, yaw_max, gimbal_device_id)

## gimbal_device_information_send
    def gimbal_device_information_send(self, time_boot_ms: int, vendor_name: bytes, model_name: bytes, custom_name: bytes, firmware_version: int, hardware_version: int, uid: int, cap_flags: int, custom_cap_flags: int, roll_min: float, roll_max: float, pitch_min: float, pitch_max: float, yaw_min: float, yaw_max: float, gimbal_device_id: int = 0, force_mavlink1: bool = False) -> None:
        """
        Information about a low level gimbal. This message should be requested
        by the gimbal manager or a ground station using
        MAV_CMD_REQUEST_MESSAGE. The maximum angles and rates are the
        limits by hardware. However, the limits by software used are
        likely different/smaller and dependent on mode/settings/etc..

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        vendor_name               : Name of the gimbal vendor. (type:char)
        model_name                : Name of the gimbal model. (type:char)
        custom_name               : Custom name of the gimbal given to it by the user. (type:char)
        firmware_version          : Version of the gimbal firmware, encoded as: (Dev & 0xff) << 24 | (Patch & 0xff) << 16 | (Minor & 0xff) << 8 | (Major & 0xff). (type:uint32_t)
        hardware_version          : Version of the gimbal hardware, encoded as: (Dev & 0xff) << 24 | (Patch & 0xff) << 16 | (Minor & 0xff) << 8 | (Major & 0xff). (type:uint32_t)
        uid                       : UID of gimbal hardware (0 if unknown). (type:uint64_t)
        cap_flags                 : Bitmap of gimbal capability flags. (type:uint16_t, values:GIMBAL_DEVICE_CAP_FLAGS)
        custom_cap_flags          : Bitmap for use for gimbal-specific capability flags. (type:uint16_t)
        roll_min                  : Minimum hardware roll angle (positive: rolling to the right, negative: rolling to the left). NAN if unknown. [rad] (type:float)
        roll_max                  : Maximum hardware roll angle (positive: rolling to the right, negative: rolling to the left). NAN if unknown. [rad] (type:float)
        pitch_min                 : Minimum hardware pitch angle (positive: up, negative: down). NAN if unknown. [rad] (type:float)
        pitch_max                 : Maximum hardware pitch angle (positive: up, negative: down). NAN if unknown. [rad] (type:float)
        yaw_min                   : Minimum hardware yaw angle (positive: to the right, negative: to the left). NAN if unknown. [rad] (type:float)
        yaw_max                   : Maximum hardware yaw angle (positive: to the right, negative: to the left). NAN if unknown. [rad] (type:float)
        gimbal_device_id          : This field is to be used if the gimbal manager and the gimbal device are the same component and hence have the same component ID. This field is then set to a number between 1-6. If the component ID is separate, this field is not required and must be set to 0. (type:uint8_t)

        """
        self.send(self.gimbal_device_information_encode(time_boot_ms, vendor_name, model_name, custom_name, firmware_version, hardware_version, uid, cap_flags, custom_cap_flags, roll_min, roll_max, pitch_min, pitch_max, yaw_min, yaw_max, gimbal_device_id), force_mavlink1=force_mavlink1)

## gimbal_device_set_attitude_encode
    def gimbal_device_set_attitude_encode(self, target_system: int, target_component: int, flags: int, q: Sequence[float], angular_velocity_x: float, angular_velocity_y: float, angular_velocity_z: float) -> MAVLink_gimbal_device_set_attitude_message:
        """
        Low level message to control a gimbal device's attitude.
        This message is to be sent from the gimbal manager to the
        gimbal device component.           The quaternion and angular
        velocities can be set to NaN according to use case.
        For the angles encoded in the quaternion and the angular
        velocities holds:           If the flag
        GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME is set, then they are
        relative to the vehicle heading (vehicle frame).           If
        the flag GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME is set, then
        they are relative to absolute North (earth frame).
        If neither of these flags are set, then (for backwards
        compatibility) it holds:           If the flag
        GIMBAL_DEVICE_FLAGS_YAW_LOCK is set, then they are relative to
        absolute North (earth frame),           else they are relative
        to the vehicle heading (vehicle frame).           Setting both
        GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME and
        GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME is not allowed.
        These rules are to ensure backwards compatibility.
        New implementations should always set either
        GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME or
        GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        flags                     : Low level gimbal flags. (type:uint16_t, values:GIMBAL_DEVICE_FLAGS)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation). The frame is described in the message description. Set fields to NaN to be ignored. (type:float)
        angular_velocity_x        : X component of angular velocity (positive: rolling to the right). The frame is described in the message description. NaN to be ignored. [rad/s] (type:float)
        angular_velocity_y        : Y component of angular velocity (positive: pitching up). The frame is described in the message description. NaN to be ignored. [rad/s] (type:float)
        angular_velocity_z        : Z component of angular velocity (positive: yawing to the right). The frame is described in the message description. NaN to be ignored. [rad/s] (type:float)

        """
        return MAVLink_gimbal_device_set_attitude_message(target_system, target_component, flags, q, angular_velocity_x, angular_velocity_y, angular_velocity_z)

## gimbal_device_set_attitude_send
    def gimbal_device_set_attitude_send(self, target_system: int, target_component: int, flags: int, q: Sequence[float], angular_velocity_x: float, angular_velocity_y: float, angular_velocity_z: float, force_mavlink1: bool = False) -> None:
        """
        Low level message to control a gimbal device's attitude.
        This message is to be sent from the gimbal manager to the
        gimbal device component.           The quaternion and angular
        velocities can be set to NaN according to use case.
        For the angles encoded in the quaternion and the angular
        velocities holds:           If the flag
        GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME is set, then they are
        relative to the vehicle heading (vehicle frame).           If
        the flag GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME is set, then
        they are relative to absolute North (earth frame).
        If neither of these flags are set, then (for backwards
        compatibility) it holds:           If the flag
        GIMBAL_DEVICE_FLAGS_YAW_LOCK is set, then they are relative to
        absolute North (earth frame),           else they are relative
        to the vehicle heading (vehicle frame).           Setting both
        GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME and
        GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME is not allowed.
        These rules are to ensure backwards compatibility.
        New implementations should always set either
        GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME or
        GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        flags                     : Low level gimbal flags. (type:uint16_t, values:GIMBAL_DEVICE_FLAGS)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation). The frame is described in the message description. Set fields to NaN to be ignored. (type:float)
        angular_velocity_x        : X component of angular velocity (positive: rolling to the right). The frame is described in the message description. NaN to be ignored. [rad/s] (type:float)
        angular_velocity_y        : Y component of angular velocity (positive: pitching up). The frame is described in the message description. NaN to be ignored. [rad/s] (type:float)
        angular_velocity_z        : Z component of angular velocity (positive: yawing to the right). The frame is described in the message description. NaN to be ignored. [rad/s] (type:float)

        """
        self.send(self.gimbal_device_set_attitude_encode(target_system, target_component, flags, q, angular_velocity_x, angular_velocity_y, angular_velocity_z), force_mavlink1=force_mavlink1)

## gimbal_device_attitude_status_encode
    def gimbal_device_attitude_status_encode(self, target_system: int, target_component: int, time_boot_ms: int, flags: int, q: Sequence[float], angular_velocity_x: float, angular_velocity_y: float, angular_velocity_z: float, failure_flags: int, delta_yaw: float = 0, delta_yaw_velocity: float = 0, gimbal_device_id: int = 0) -> MAVLink_gimbal_device_attitude_status_message:
        """
        Message reporting the status of a gimbal device.           This
        message should be broadcast by a gimbal device component at a
        low regular rate (e.g. 5 Hz).           For the angles encoded
        in the quaternion and the angular velocities holds:
        If the flag GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME is set,
        then they are relative to the vehicle heading (vehicle frame).
        If the flag GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME is set,
        then they are relative to absolute North (earth frame).
        If neither of these flags are set, then (for backwards
        compatibility) it holds:           If the flag
        GIMBAL_DEVICE_FLAGS_YAW_LOCK is set, then they are relative to
        absolute North (earth frame),           else they are relative
        to the vehicle heading (vehicle frame).           Other
        conditions of the flags are not allowed.           The
        quaternion and angular velocities in the other frame can be
        calculated from delta_yaw and delta_yaw_velocity as
        q_earth = q_delta_yaw * q_vehicle and w_earth =
        w_delta_yaw_velocity + w_vehicle (if not NaN).           If
        neither the GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME nor the
        GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME flag is set,
        then (for backwards compatibility) the data in the delta_yaw
        and delta_yaw_velocity fields are to be ignored.           New
        implementations should always set either
        GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME or
        GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME,           and always
        should set delta_yaw and delta_yaw_velocity either to the
        proper value or NaN.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        flags                     : Current gimbal flags set. (type:uint16_t, values:GIMBAL_DEVICE_FLAGS)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation). The frame is described in the message description. (type:float)
        angular_velocity_x        : X component of angular velocity (positive: rolling to the right). The frame is described in the message description. NaN if unknown. [rad/s] (type:float)
        angular_velocity_y        : Y component of angular velocity (positive: pitching up). The frame is described in the message description. NaN if unknown. [rad/s] (type:float)
        angular_velocity_z        : Z component of angular velocity (positive: yawing to the right). The frame is described in the message description. NaN if unknown. [rad/s] (type:float)
        failure_flags             : Failure flags (0 for no failure) (type:uint32_t, values:GIMBAL_DEVICE_ERROR_FLAGS)
        delta_yaw                 : Yaw angle relating the quaternions in earth and body frames (see message description). NaN if unknown. [rad] (type:float)
        delta_yaw_velocity        : Yaw angular velocity relating the angular velocities in earth and body frames (see message description). NaN if unknown. [rad/s] (type:float)
        gimbal_device_id          : This field is to be used if the gimbal manager and the gimbal device are the same component and hence have the same component ID. This field is then set a number between 1-6. If the component ID is separate, this field is not required and must be set to 0. (type:uint8_t)

        """
        return MAVLink_gimbal_device_attitude_status_message(target_system, target_component, time_boot_ms, flags, q, angular_velocity_x, angular_velocity_y, angular_velocity_z, failure_flags, delta_yaw, delta_yaw_velocity, gimbal_device_id)

## gimbal_device_attitude_status_send
    def gimbal_device_attitude_status_send(self, target_system: int, target_component: int, time_boot_ms: int, flags: int, q: Sequence[float], angular_velocity_x: float, angular_velocity_y: float, angular_velocity_z: float, failure_flags: int, delta_yaw: float = 0, delta_yaw_velocity: float = 0, gimbal_device_id: int = 0, force_mavlink1: bool = False) -> None:
        """
        Message reporting the status of a gimbal device.           This
        message should be broadcast by a gimbal device component at a
        low regular rate (e.g. 5 Hz).           For the angles encoded
        in the quaternion and the angular velocities holds:
        If the flag GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME is set,
        then they are relative to the vehicle heading (vehicle frame).
        If the flag GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME is set,
        then they are relative to absolute North (earth frame).
        If neither of these flags are set, then (for backwards
        compatibility) it holds:           If the flag
        GIMBAL_DEVICE_FLAGS_YAW_LOCK is set, then they are relative to
        absolute North (earth frame),           else they are relative
        to the vehicle heading (vehicle frame).           Other
        conditions of the flags are not allowed.           The
        quaternion and angular velocities in the other frame can be
        calculated from delta_yaw and delta_yaw_velocity as
        q_earth = q_delta_yaw * q_vehicle and w_earth =
        w_delta_yaw_velocity + w_vehicle (if not NaN).           If
        neither the GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME nor the
        GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME flag is set,
        then (for backwards compatibility) the data in the delta_yaw
        and delta_yaw_velocity fields are to be ignored.           New
        implementations should always set either
        GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME or
        GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME,           and always
        should set delta_yaw and delta_yaw_velocity either to the
        proper value or NaN.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        flags                     : Current gimbal flags set. (type:uint16_t, values:GIMBAL_DEVICE_FLAGS)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation). The frame is described in the message description. (type:float)
        angular_velocity_x        : X component of angular velocity (positive: rolling to the right). The frame is described in the message description. NaN if unknown. [rad/s] (type:float)
        angular_velocity_y        : Y component of angular velocity (positive: pitching up). The frame is described in the message description. NaN if unknown. [rad/s] (type:float)
        angular_velocity_z        : Z component of angular velocity (positive: yawing to the right). The frame is described in the message description. NaN if unknown. [rad/s] (type:float)
        failure_flags             : Failure flags (0 for no failure) (type:uint32_t, values:GIMBAL_DEVICE_ERROR_FLAGS)
        delta_yaw                 : Yaw angle relating the quaternions in earth and body frames (see message description). NaN if unknown. [rad] (type:float)
        delta_yaw_velocity        : Yaw angular velocity relating the angular velocities in earth and body frames (see message description). NaN if unknown. [rad/s] (type:float)
        gimbal_device_id          : This field is to be used if the gimbal manager and the gimbal device are the same component and hence have the same component ID. This field is then set a number between 1-6. If the component ID is separate, this field is not required and must be set to 0. (type:uint8_t)

        """
        self.send(self.gimbal_device_attitude_status_encode(target_system, target_component, time_boot_ms, flags, q, angular_velocity_x, angular_velocity_y, angular_velocity_z, failure_flags, delta_yaw, delta_yaw_velocity, gimbal_device_id), force_mavlink1=force_mavlink1)

## autopilot_state_for_gimbal_device_encode
    def autopilot_state_for_gimbal_device_encode(self, target_system: int, target_component: int, time_boot_us: int, q: Sequence[float], q_estimated_delay_us: int, vx: float, vy: float, vz: float, v_estimated_delay_us: int, feed_forward_angular_velocity_z: float, estimator_status: int, landed_state: int, angular_velocity_z: float = 0) -> MAVLink_autopilot_state_for_gimbal_device_message:
        """
        Low level message containing autopilot state relevant for a gimbal
        device. This message is to be sent from the autopilot to the
        gimbal device component. The data of this message are for the
        gimbal device's estimator corrections, in particular horizon
        compensation, as well as indicates autopilot control
        intentions, e.g. feed forward angular control in the z-axis.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        time_boot_us              : Timestamp (time since system boot). [us] (type:uint64_t)
        q                         : Quaternion components of autopilot attitude: w, x, y, z (1 0 0 0 is the null-rotation, Hamilton convention). (type:float)
        q_estimated_delay_us        : Estimated delay of the attitude data. 0 if unknown. [us] (type:uint32_t)
        vx                        : X Speed in NED (North, East, Down). NAN if unknown. [m/s] (type:float)
        vy                        : Y Speed in NED (North, East, Down). NAN if unknown. [m/s] (type:float)
        vz                        : Z Speed in NED (North, East, Down). NAN if unknown. [m/s] (type:float)
        v_estimated_delay_us        : Estimated delay of the speed data. 0 if unknown. [us] (type:uint32_t)
        feed_forward_angular_velocity_z        : Feed forward Z component of angular velocity (positive: yawing to the right). NaN to be ignored. This is to indicate if the autopilot is actively yawing. [rad/s] (type:float)
        estimator_status          : Bitmap indicating which estimator outputs are valid. (type:uint16_t, values:ESTIMATOR_STATUS_FLAGS)
        landed_state              : The landed state. Is set to MAV_LANDED_STATE_UNDEFINED if landed state is unknown. (type:uint8_t, values:MAV_LANDED_STATE)
        angular_velocity_z        : Z component of angular velocity in NED (North, East, Down). NaN if unknown. [rad/s] (type:float)

        """
        return MAVLink_autopilot_state_for_gimbal_device_message(target_system, target_component, time_boot_us, q, q_estimated_delay_us, vx, vy, vz, v_estimated_delay_us, feed_forward_angular_velocity_z, estimator_status, landed_state, angular_velocity_z)

## autopilot_state_for_gimbal_device_send
    def autopilot_state_for_gimbal_device_send(self, target_system: int, target_component: int, time_boot_us: int, q: Sequence[float], q_estimated_delay_us: int, vx: float, vy: float, vz: float, v_estimated_delay_us: int, feed_forward_angular_velocity_z: float, estimator_status: int, landed_state: int, angular_velocity_z: float = 0, force_mavlink1: bool = False) -> None:
        """
        Low level message containing autopilot state relevant for a gimbal
        device. This message is to be sent from the autopilot to the
        gimbal device component. The data of this message are for the
        gimbal device's estimator corrections, in particular horizon
        compensation, as well as indicates autopilot control
        intentions, e.g. feed forward angular control in the z-axis.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        time_boot_us              : Timestamp (time since system boot). [us] (type:uint64_t)
        q                         : Quaternion components of autopilot attitude: w, x, y, z (1 0 0 0 is the null-rotation, Hamilton convention). (type:float)
        q_estimated_delay_us        : Estimated delay of the attitude data. 0 if unknown. [us] (type:uint32_t)
        vx                        : X Speed in NED (North, East, Down). NAN if unknown. [m/s] (type:float)
        vy                        : Y Speed in NED (North, East, Down). NAN if unknown. [m/s] (type:float)
        vz                        : Z Speed in NED (North, East, Down). NAN if unknown. [m/s] (type:float)
        v_estimated_delay_us        : Estimated delay of the speed data. 0 if unknown. [us] (type:uint32_t)
        feed_forward_angular_velocity_z        : Feed forward Z component of angular velocity (positive: yawing to the right). NaN to be ignored. This is to indicate if the autopilot is actively yawing. [rad/s] (type:float)
        estimator_status          : Bitmap indicating which estimator outputs are valid. (type:uint16_t, values:ESTIMATOR_STATUS_FLAGS)
        landed_state              : The landed state. Is set to MAV_LANDED_STATE_UNDEFINED if landed state is unknown. (type:uint8_t, values:MAV_LANDED_STATE)
        angular_velocity_z        : Z component of angular velocity in NED (North, East, Down). NaN if unknown. [rad/s] (type:float)

        """
        self.send(self.autopilot_state_for_gimbal_device_encode(target_system, target_component, time_boot_us, q, q_estimated_delay_us, vx, vy, vz, v_estimated_delay_us, feed_forward_angular_velocity_z, estimator_status, landed_state, angular_velocity_z), force_mavlink1=force_mavlink1)

## gimbal_manager_set_pitchyaw_encode
    def gimbal_manager_set_pitchyaw_encode(self, target_system: int, target_component: int, flags: int, gimbal_device_id: int, pitch: float, yaw: float, pitch_rate: float, yaw_rate: float) -> MAVLink_gimbal_manager_set_pitchyaw_message:
        """
        Set gimbal manager pitch and yaw angles (high rate message). This
        message is to be sent to the gimbal manager (e.g. from a
        ground station) and will be ignored by gimbal devices. Angles
        and rates can be set to NaN according to use case. Use
        MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW for low-rate adjustments
        that require confirmation.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        flags                     : High level gimbal manager flags to use. (type:uint32_t, values:GIMBAL_MANAGER_FLAGS)
        gimbal_device_id          : Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). (type:uint8_t)
        pitch                     : Pitch angle (positive: up, negative: down, NaN to be ignored). [rad] (type:float)
        yaw                       : Yaw angle (positive: to the right, negative: to the left, NaN to be ignored). [rad] (type:float)
        pitch_rate                : Pitch angular rate (positive: up, negative: down, NaN to be ignored). [rad/s] (type:float)
        yaw_rate                  : Yaw angular rate (positive: to the right, negative: to the left, NaN to be ignored). [rad/s] (type:float)

        """
        return MAVLink_gimbal_manager_set_pitchyaw_message(target_system, target_component, flags, gimbal_device_id, pitch, yaw, pitch_rate, yaw_rate)

## gimbal_manager_set_pitchyaw_send
    def gimbal_manager_set_pitchyaw_send(self, target_system: int, target_component: int, flags: int, gimbal_device_id: int, pitch: float, yaw: float, pitch_rate: float, yaw_rate: float, force_mavlink1: bool = False) -> None:
        """
        Set gimbal manager pitch and yaw angles (high rate message). This
        message is to be sent to the gimbal manager (e.g. from a
        ground station) and will be ignored by gimbal devices. Angles
        and rates can be set to NaN according to use case. Use
        MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW for low-rate adjustments
        that require confirmation.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        flags                     : High level gimbal manager flags to use. (type:uint32_t, values:GIMBAL_MANAGER_FLAGS)
        gimbal_device_id          : Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). (type:uint8_t)
        pitch                     : Pitch angle (positive: up, negative: down, NaN to be ignored). [rad] (type:float)
        yaw                       : Yaw angle (positive: to the right, negative: to the left, NaN to be ignored). [rad] (type:float)
        pitch_rate                : Pitch angular rate (positive: up, negative: down, NaN to be ignored). [rad/s] (type:float)
        yaw_rate                  : Yaw angular rate (positive: to the right, negative: to the left, NaN to be ignored). [rad/s] (type:float)

        """
        self.send(self.gimbal_manager_set_pitchyaw_encode(target_system, target_component, flags, gimbal_device_id, pitch, yaw, pitch_rate, yaw_rate), force_mavlink1=force_mavlink1)

## gimbal_manager_set_manual_control_encode
    def gimbal_manager_set_manual_control_encode(self, target_system: int, target_component: int, flags: int, gimbal_device_id: int, pitch: float, yaw: float, pitch_rate: float, yaw_rate: float) -> MAVLink_gimbal_manager_set_manual_control_message:
        """
        High level message to control a gimbal manually. The angles or angular
        rates are unitless; the actual rates will depend on internal
        gimbal manager settings/configuration (e.g. set by
        parameters). This message is to be sent to the gimbal manager
        (e.g. from a ground station). Angles and rates can be set to
        NaN according to use case.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        flags                     : High level gimbal manager flags. (type:uint32_t, values:GIMBAL_MANAGER_FLAGS)
        gimbal_device_id          : Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). (type:uint8_t)
        pitch                     : Pitch angle unitless (-1..1, positive: up, negative: down, NaN to be ignored). (type:float)
        yaw                       : Yaw angle unitless (-1..1, positive: to the right, negative: to the left, NaN to be ignored). (type:float)
        pitch_rate                : Pitch angular rate unitless (-1..1, positive: up, negative: down, NaN to be ignored). (type:float)
        yaw_rate                  : Yaw angular rate unitless (-1..1, positive: to the right, negative: to the left, NaN to be ignored). (type:float)

        """
        return MAVLink_gimbal_manager_set_manual_control_message(target_system, target_component, flags, gimbal_device_id, pitch, yaw, pitch_rate, yaw_rate)

## gimbal_manager_set_manual_control_send
    def gimbal_manager_set_manual_control_send(self, target_system: int, target_component: int, flags: int, gimbal_device_id: int, pitch: float, yaw: float, pitch_rate: float, yaw_rate: float, force_mavlink1: bool = False) -> None:
        """
        High level message to control a gimbal manually. The angles or angular
        rates are unitless; the actual rates will depend on internal
        gimbal manager settings/configuration (e.g. set by
        parameters). This message is to be sent to the gimbal manager
        (e.g. from a ground station). Angles and rates can be set to
        NaN according to use case.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        flags                     : High level gimbal manager flags. (type:uint32_t, values:GIMBAL_MANAGER_FLAGS)
        gimbal_device_id          : Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). (type:uint8_t)
        pitch                     : Pitch angle unitless (-1..1, positive: up, negative: down, NaN to be ignored). (type:float)
        yaw                       : Yaw angle unitless (-1..1, positive: to the right, negative: to the left, NaN to be ignored). (type:float)
        pitch_rate                : Pitch angular rate unitless (-1..1, positive: up, negative: down, NaN to be ignored). (type:float)
        yaw_rate                  : Yaw angular rate unitless (-1..1, positive: to the right, negative: to the left, NaN to be ignored). (type:float)

        """
        self.send(self.gimbal_manager_set_manual_control_encode(target_system, target_component, flags, gimbal_device_id, pitch, yaw, pitch_rate, yaw_rate), force_mavlink1=force_mavlink1)

## wifi_config_ap_encode
    def wifi_config_ap_encode(self, ssid: bytes, password: bytes) -> MAVLink_wifi_config_ap_message:
        """
        Configure WiFi AP SSID, password, and mode. This message is re-emitted
        as an acknowledgement by the AP. The message may also be
        explicitly requested using MAV_CMD_REQUEST_MESSAGE

        ssid                      : Name of Wi-Fi network (SSID). Blank to leave it unchanged when setting. Current SSID when sent back as a response. (type:char)
        password                  : Password. Blank for an open AP. MD5 hash when message is sent back as a response. (type:char)

        """
        return MAVLink_wifi_config_ap_message(ssid, password)

## wifi_config_ap_send
    def wifi_config_ap_send(self, ssid: bytes, password: bytes, force_mavlink1: bool = False) -> None:
        """
        Configure WiFi AP SSID, password, and mode. This message is re-emitted
        as an acknowledgement by the AP. The message may also be
        explicitly requested using MAV_CMD_REQUEST_MESSAGE

        ssid                      : Name of Wi-Fi network (SSID). Blank to leave it unchanged when setting. Current SSID when sent back as a response. (type:char)
        password                  : Password. Blank for an open AP. MD5 hash when message is sent back as a response. (type:char)

        """
        self.send(self.wifi_config_ap_encode(ssid, password), force_mavlink1=force_mavlink1)

## ais_vessel_encode
    def ais_vessel_encode(self, MMSI: int, lat: int, lon: int, COG: int, heading: int, velocity: int, turn_rate: int, navigational_status: int, type: int, dimension_bow: int, dimension_stern: int, dimension_port: int, dimension_starboard: int, callsign: bytes, name: bytes, tslc: int, flags: int) -> MAVLink_ais_vessel_message:
        """
        The location and information of an AIS vessel

        MMSI                      : Mobile Marine Service Identifier, 9 decimal digits (type:uint32_t)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        COG                       : Course over ground [cdeg] (type:uint16_t)
        heading                   : True heading [cdeg] (type:uint16_t)
        velocity                  : Speed over ground [cm/s] (type:uint16_t)
        turn_rate                 : Turn rate [cdeg/s] (type:int8_t)
        navigational_status        : Navigational status (type:uint8_t, values:AIS_NAV_STATUS)
        type                      : Type of vessels (type:uint8_t, values:AIS_TYPE)
        dimension_bow             : Distance from lat/lon location to bow [m] (type:uint16_t)
        dimension_stern           : Distance from lat/lon location to stern [m] (type:uint16_t)
        dimension_port            : Distance from lat/lon location to port side [m] (type:uint8_t)
        dimension_starboard        : Distance from lat/lon location to starboard side [m] (type:uint8_t)
        callsign                  : The vessel callsign (type:char)
        name                      : The vessel name (type:char)
        tslc                      : Time since last communication in seconds [s] (type:uint16_t)
        flags                     : Bitmask to indicate various statuses including valid data fields (type:uint16_t, values:AIS_FLAGS)

        """
        return MAVLink_ais_vessel_message(MMSI, lat, lon, COG, heading, velocity, turn_rate, navigational_status, type, dimension_bow, dimension_stern, dimension_port, dimension_starboard, callsign, name, tslc, flags)

## ais_vessel_send
    def ais_vessel_send(self, MMSI: int, lat: int, lon: int, COG: int, heading: int, velocity: int, turn_rate: int, navigational_status: int, type: int, dimension_bow: int, dimension_stern: int, dimension_port: int, dimension_starboard: int, callsign: bytes, name: bytes, tslc: int, flags: int, force_mavlink1: bool = False) -> None:
        """
        The location and information of an AIS vessel

        MMSI                      : Mobile Marine Service Identifier, 9 decimal digits (type:uint32_t)
        lat                       : Latitude [degE7] (type:int32_t)
        lon                       : Longitude [degE7] (type:int32_t)
        COG                       : Course over ground [cdeg] (type:uint16_t)
        heading                   : True heading [cdeg] (type:uint16_t)
        velocity                  : Speed over ground [cm/s] (type:uint16_t)
        turn_rate                 : Turn rate [cdeg/s] (type:int8_t)
        navigational_status        : Navigational status (type:uint8_t, values:AIS_NAV_STATUS)
        type                      : Type of vessels (type:uint8_t, values:AIS_TYPE)
        dimension_bow             : Distance from lat/lon location to bow [m] (type:uint16_t)
        dimension_stern           : Distance from lat/lon location to stern [m] (type:uint16_t)
        dimension_port            : Distance from lat/lon location to port side [m] (type:uint8_t)
        dimension_starboard        : Distance from lat/lon location to starboard side [m] (type:uint8_t)
        callsign                  : The vessel callsign (type:char)
        name                      : The vessel name (type:char)
        tslc                      : Time since last communication in seconds [s] (type:uint16_t)
        flags                     : Bitmask to indicate various statuses including valid data fields (type:uint16_t, values:AIS_FLAGS)

        """
        self.send(self.ais_vessel_encode(MMSI, lat, lon, COG, heading, velocity, turn_rate, navigational_status, type, dimension_bow, dimension_stern, dimension_port, dimension_starboard, callsign, name, tslc, flags), force_mavlink1=force_mavlink1)

## uavcan_node_status_encode
    def uavcan_node_status_encode(self, time_usec: int, uptime_sec: int, health: int, mode: int, sub_mode: int, vendor_specific_status_code: int) -> MAVLink_uavcan_node_status_message:
        """
        General status information of an UAVCAN node. Please refer to the
        definition of the UAVCAN message "uavcan.protocol.NodeStatus"
        for the background information. The UAVCAN specification is
        available at http://uavcan.org.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        uptime_sec                : Time since the start-up of the node. [s] (type:uint32_t)
        health                    : Generalized node health status. (type:uint8_t, values:UAVCAN_NODE_HEALTH)
        mode                      : Generalized operating mode. (type:uint8_t, values:UAVCAN_NODE_MODE)
        sub_mode                  : Not used currently. (type:uint8_t)
        vendor_specific_status_code        : Vendor-specific status information. (type:uint16_t)

        """
        return MAVLink_uavcan_node_status_message(time_usec, uptime_sec, health, mode, sub_mode, vendor_specific_status_code)

## uavcan_node_status_send
    def uavcan_node_status_send(self, time_usec: int, uptime_sec: int, health: int, mode: int, sub_mode: int, vendor_specific_status_code: int, force_mavlink1: bool = False) -> None:
        """
        General status information of an UAVCAN node. Please refer to the
        definition of the UAVCAN message "uavcan.protocol.NodeStatus"
        for the background information. The UAVCAN specification is
        available at http://uavcan.org.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        uptime_sec                : Time since the start-up of the node. [s] (type:uint32_t)
        health                    : Generalized node health status. (type:uint8_t, values:UAVCAN_NODE_HEALTH)
        mode                      : Generalized operating mode. (type:uint8_t, values:UAVCAN_NODE_MODE)
        sub_mode                  : Not used currently. (type:uint8_t)
        vendor_specific_status_code        : Vendor-specific status information. (type:uint16_t)

        """
        self.send(self.uavcan_node_status_encode(time_usec, uptime_sec, health, mode, sub_mode, vendor_specific_status_code), force_mavlink1=force_mavlink1)

## uavcan_node_info_encode
    def uavcan_node_info_encode(self, time_usec: int, uptime_sec: int, name: bytes, hw_version_major: int, hw_version_minor: int, hw_unique_id: Sequence[int], sw_version_major: int, sw_version_minor: int, sw_vcs_commit: int) -> MAVLink_uavcan_node_info_message:
        """
        General information describing a particular UAVCAN node. Please refer
        to the definition of the UAVCAN service
        "uavcan.protocol.GetNodeInfo" for the background information.
        This message should be emitted by the system whenever a new
        node appears online, or an existing node reboots.
        Additionally, it can be emitted upon request from the other
        end of the MAVLink channel (see MAV_CMD_UAVCAN_GET_NODE_INFO).
        It is also not prohibited to emit this message unconditionally
        at a low frequency. The UAVCAN specification is available at
        http://uavcan.org.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        uptime_sec                : Time since the start-up of the node. [s] (type:uint32_t)
        name                      : Node name string. For example, "sapog.px4.io". (type:char)
        hw_version_major          : Hardware major version number. (type:uint8_t)
        hw_version_minor          : Hardware minor version number. (type:uint8_t)
        hw_unique_id              : Hardware unique 128-bit ID. (type:uint8_t)
        sw_version_major          : Software major version number. (type:uint8_t)
        sw_version_minor          : Software minor version number. (type:uint8_t)
        sw_vcs_commit             : Version control system (VCS) revision identifier (e.g. git short commit hash). 0 if unknown. (type:uint32_t)

        """
        return MAVLink_uavcan_node_info_message(time_usec, uptime_sec, name, hw_version_major, hw_version_minor, hw_unique_id, sw_version_major, sw_version_minor, sw_vcs_commit)

## uavcan_node_info_send
    def uavcan_node_info_send(self, time_usec: int, uptime_sec: int, name: bytes, hw_version_major: int, hw_version_minor: int, hw_unique_id: Sequence[int], sw_version_major: int, sw_version_minor: int, sw_vcs_commit: int, force_mavlink1: bool = False) -> None:
        """
        General information describing a particular UAVCAN node. Please refer
        to the definition of the UAVCAN service
        "uavcan.protocol.GetNodeInfo" for the background information.
        This message should be emitted by the system whenever a new
        node appears online, or an existing node reboots.
        Additionally, it can be emitted upon request from the other
        end of the MAVLink channel (see MAV_CMD_UAVCAN_GET_NODE_INFO).
        It is also not prohibited to emit this message unconditionally
        at a low frequency. The UAVCAN specification is available at
        http://uavcan.org.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        uptime_sec                : Time since the start-up of the node. [s] (type:uint32_t)
        name                      : Node name string. For example, "sapog.px4.io". (type:char)
        hw_version_major          : Hardware major version number. (type:uint8_t)
        hw_version_minor          : Hardware minor version number. (type:uint8_t)
        hw_unique_id              : Hardware unique 128-bit ID. (type:uint8_t)
        sw_version_major          : Software major version number. (type:uint8_t)
        sw_version_minor          : Software minor version number. (type:uint8_t)
        sw_vcs_commit             : Version control system (VCS) revision identifier (e.g. git short commit hash). 0 if unknown. (type:uint32_t)

        """
        self.send(self.uavcan_node_info_encode(time_usec, uptime_sec, name, hw_version_major, hw_version_minor, hw_unique_id, sw_version_major, sw_version_minor, sw_vcs_commit), force_mavlink1=force_mavlink1)

## param_ext_request_read_encode
    def param_ext_request_read_encode(self, target_system: int, target_component: int, param_id: bytes, param_index: int) -> MAVLink_param_ext_request_read_message:
        """
        Request to read the value of a parameter with either the param_id
        string id or param_index. PARAM_EXT_VALUE should be emitted in
        response.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_index               : Parameter index. Set to -1 to use the Parameter ID field as identifier (else param_id will be ignored) (type:int16_t)

        """
        return MAVLink_param_ext_request_read_message(target_system, target_component, param_id, param_index)

## param_ext_request_read_send
    def param_ext_request_read_send(self, target_system: int, target_component: int, param_id: bytes, param_index: int, force_mavlink1: bool = False) -> None:
        """
        Request to read the value of a parameter with either the param_id
        string id or param_index. PARAM_EXT_VALUE should be emitted in
        response.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_index               : Parameter index. Set to -1 to use the Parameter ID field as identifier (else param_id will be ignored) (type:int16_t)

        """
        self.send(self.param_ext_request_read_encode(target_system, target_component, param_id, param_index), force_mavlink1=force_mavlink1)

## param_ext_request_list_encode
    def param_ext_request_list_encode(self, target_system: int, target_component: int) -> MAVLink_param_ext_request_list_message:
        """
        Request all parameters of this component. All parameters should be
        emitted in response as PARAM_EXT_VALUE.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)

        """
        return MAVLink_param_ext_request_list_message(target_system, target_component)

## param_ext_request_list_send
    def param_ext_request_list_send(self, target_system: int, target_component: int, force_mavlink1: bool = False) -> None:
        """
        Request all parameters of this component. All parameters should be
        emitted in response as PARAM_EXT_VALUE.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)

        """
        self.send(self.param_ext_request_list_encode(target_system, target_component), force_mavlink1=force_mavlink1)

## param_ext_value_encode
    def param_ext_value_encode(self, param_id: bytes, param_value: bytes, param_type: int, param_count: int, param_index: int) -> MAVLink_param_ext_value_message:
        """
        Emit the value of a parameter. The inclusion of param_count and
        param_index in the message allows the recipient to keep track
        of received parameters and allows them to re-request missing
        parameters after a loss or timeout.

        param_id                  : Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Parameter value (type:char)
        param_type                : Parameter type. (type:uint8_t, values:MAV_PARAM_EXT_TYPE)
        param_count               : Total number of parameters (type:uint16_t)
        param_index               : Index of this parameter (type:uint16_t)

        """
        return MAVLink_param_ext_value_message(param_id, param_value, param_type, param_count, param_index)

## param_ext_value_send
    def param_ext_value_send(self, param_id: bytes, param_value: bytes, param_type: int, param_count: int, param_index: int, force_mavlink1: bool = False) -> None:
        """
        Emit the value of a parameter. The inclusion of param_count and
        param_index in the message allows the recipient to keep track
        of received parameters and allows them to re-request missing
        parameters after a loss or timeout.

        param_id                  : Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Parameter value (type:char)
        param_type                : Parameter type. (type:uint8_t, values:MAV_PARAM_EXT_TYPE)
        param_count               : Total number of parameters (type:uint16_t)
        param_index               : Index of this parameter (type:uint16_t)

        """
        self.send(self.param_ext_value_encode(param_id, param_value, param_type, param_count, param_index), force_mavlink1=force_mavlink1)

## param_ext_set_encode
    def param_ext_set_encode(self, target_system: int, target_component: int, param_id: bytes, param_value: bytes, param_type: int) -> MAVLink_param_ext_set_message:
        """
        Set a parameter value. In order to deal with message loss (and
        retransmission of PARAM_EXT_SET), when setting a parameter
        value and the new value is the same as the current value, you
        will immediately get a PARAM_ACK_ACCEPTED response. If the
        current state is PARAM_ACK_IN_PROGRESS, you will accordingly
        receive a PARAM_ACK_IN_PROGRESS in response.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Parameter value (type:char)
        param_type                : Parameter type. (type:uint8_t, values:MAV_PARAM_EXT_TYPE)

        """
        return MAVLink_param_ext_set_message(target_system, target_component, param_id, param_value, param_type)

## param_ext_set_send
    def param_ext_set_send(self, target_system: int, target_component: int, param_id: bytes, param_value: bytes, param_type: int, force_mavlink1: bool = False) -> None:
        """
        Set a parameter value. In order to deal with message loss (and
        retransmission of PARAM_EXT_SET), when setting a parameter
        value and the new value is the same as the current value, you
        will immediately get a PARAM_ACK_ACCEPTED response. If the
        current state is PARAM_ACK_IN_PROGRESS, you will accordingly
        receive a PARAM_ACK_IN_PROGRESS in response.

        target_system             : System ID (type:uint8_t)
        target_component          : Component ID (type:uint8_t)
        param_id                  : Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Parameter value (type:char)
        param_type                : Parameter type. (type:uint8_t, values:MAV_PARAM_EXT_TYPE)

        """
        self.send(self.param_ext_set_encode(target_system, target_component, param_id, param_value, param_type), force_mavlink1=force_mavlink1)

## param_ext_ack_encode
    def param_ext_ack_encode(self, param_id: bytes, param_value: bytes, param_type: int, param_result: int) -> MAVLink_param_ext_ack_message:
        """
        Response from a PARAM_EXT_SET message.

        param_id                  : Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Parameter value (new value if PARAM_ACK_ACCEPTED, current value otherwise) (type:char)
        param_type                : Parameter type. (type:uint8_t, values:MAV_PARAM_EXT_TYPE)
        param_result              : Result code. (type:uint8_t, values:PARAM_ACK)

        """
        return MAVLink_param_ext_ack_message(param_id, param_value, param_type, param_result)

## param_ext_ack_send
    def param_ext_ack_send(self, param_id: bytes, param_value: bytes, param_type: int, param_result: int, force_mavlink1: bool = False) -> None:
        """
        Response from a PARAM_EXT_SET message.

        param_id                  : Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string (type:char)
        param_value               : Parameter value (new value if PARAM_ACK_ACCEPTED, current value otherwise) (type:char)
        param_type                : Parameter type. (type:uint8_t, values:MAV_PARAM_EXT_TYPE)
        param_result              : Result code. (type:uint8_t, values:PARAM_ACK)

        """
        self.send(self.param_ext_ack_encode(param_id, param_value, param_type, param_result), force_mavlink1=force_mavlink1)

## obstacle_distance_encode
    def obstacle_distance_encode(self, time_usec: int, sensor_type: int, distances: Sequence[int], increment: int, min_distance: int, max_distance: int, increment_f: float = 0, angle_offset: float = 0, frame: int = 0) -> MAVLink_obstacle_distance_message:
        """
        Obstacle distances in front of the sensor, starting from the left in
        increment degrees to the right

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        sensor_type               : Class id of the distance sensor type. (type:uint8_t, values:MAV_DISTANCE_SENSOR)
        distances                 : Distance of obstacles around the vehicle with index 0 corresponding to north + angle_offset, unless otherwise specified in the frame. A value of 0 is valid and means that the obstacle is practically touching the sensor. A value of max_distance +1 means no obstacle is present. A value of UINT16_MAX for unknown/not used. In a array element, one unit corresponds to 1cm. [cm] (type:uint16_t)
        increment                 : Angular width in degrees of each array element. Increment direction is clockwise. This field is ignored if increment_f is non-zero. [deg] (type:uint8_t)
        min_distance              : Minimum distance the sensor can measure. [cm] (type:uint16_t)
        max_distance              : Maximum distance the sensor can measure. [cm] (type:uint16_t)
        increment_f               : Angular width in degrees of each array element as a float. If non-zero then this value is used instead of the uint8_t increment field. Positive is clockwise direction, negative is counter-clockwise. [deg] (type:float)
        angle_offset              : Relative angle offset of the 0-index element in the distances array. Value of 0 corresponds to forward. Positive is clockwise direction, negative is counter-clockwise. [deg] (type:float)
        frame                     : Coordinate frame of reference for the yaw rotation and offset of the sensor data. Defaults to MAV_FRAME_GLOBAL, which is north aligned. For body-mounted sensors use MAV_FRAME_BODY_FRD, which is vehicle front aligned. (type:uint8_t, values:MAV_FRAME)

        """
        return MAVLink_obstacle_distance_message(time_usec, sensor_type, distances, increment, min_distance, max_distance, increment_f, angle_offset, frame)

## obstacle_distance_send
    def obstacle_distance_send(self, time_usec: int, sensor_type: int, distances: Sequence[int], increment: int, min_distance: int, max_distance: int, increment_f: float = 0, angle_offset: float = 0, frame: int = 0, force_mavlink1: bool = False) -> None:
        """
        Obstacle distances in front of the sensor, starting from the left in
        increment degrees to the right

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        sensor_type               : Class id of the distance sensor type. (type:uint8_t, values:MAV_DISTANCE_SENSOR)
        distances                 : Distance of obstacles around the vehicle with index 0 corresponding to north + angle_offset, unless otherwise specified in the frame. A value of 0 is valid and means that the obstacle is practically touching the sensor. A value of max_distance +1 means no obstacle is present. A value of UINT16_MAX for unknown/not used. In a array element, one unit corresponds to 1cm. [cm] (type:uint16_t)
        increment                 : Angular width in degrees of each array element. Increment direction is clockwise. This field is ignored if increment_f is non-zero. [deg] (type:uint8_t)
        min_distance              : Minimum distance the sensor can measure. [cm] (type:uint16_t)
        max_distance              : Maximum distance the sensor can measure. [cm] (type:uint16_t)
        increment_f               : Angular width in degrees of each array element as a float. If non-zero then this value is used instead of the uint8_t increment field. Positive is clockwise direction, negative is counter-clockwise. [deg] (type:float)
        angle_offset              : Relative angle offset of the 0-index element in the distances array. Value of 0 corresponds to forward. Positive is clockwise direction, negative is counter-clockwise. [deg] (type:float)
        frame                     : Coordinate frame of reference for the yaw rotation and offset of the sensor data. Defaults to MAV_FRAME_GLOBAL, which is north aligned. For body-mounted sensors use MAV_FRAME_BODY_FRD, which is vehicle front aligned. (type:uint8_t, values:MAV_FRAME)

        """
        self.send(self.obstacle_distance_encode(time_usec, sensor_type, distances, increment, min_distance, max_distance, increment_f, angle_offset, frame), force_mavlink1=force_mavlink1)

## odometry_encode
    def odometry_encode(self, time_usec: int, frame_id: int, child_frame_id: int, x: float, y: float, z: float, q: Sequence[float], vx: float, vy: float, vz: float, rollspeed: float, pitchspeed: float, yawspeed: float, pose_covariance: Sequence[float], velocity_covariance: Sequence[float], reset_counter: int = 0, estimator_type: int = 0, quality: int = 0) -> MAVLink_odometry_message:
        """
        Odometry message to communicate odometry information with an external
        interface. Fits ROS REP 147 standard for aerial vehicles
        (http://www.ros.org/reps/rep-0147.html).

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        frame_id                  : Coordinate frame of reference for the pose data. (type:uint8_t, values:MAV_FRAME)
        child_frame_id            : Coordinate frame of reference for the velocity in free space (twist) data. (type:uint8_t, values:MAV_FRAME)
        x                         : X Position [m] (type:float)
        y                         : Y Position [m] (type:float)
        z                         : Z Position [m] (type:float)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation) (type:float)
        vx                        : X linear speed [m/s] (type:float)
        vy                        : Y linear speed [m/s] (type:float)
        vz                        : Z linear speed [m/s] (type:float)
        rollspeed                 : Roll angular speed [rad/s] (type:float)
        pitchspeed                : Pitch angular speed [rad/s] (type:float)
        yawspeed                  : Yaw angular speed [rad/s] (type:float)
        pose_covariance           : Row-major representation of a 6x6 pose cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        velocity_covariance        : Row-major representation of a 6x6 velocity cross-covariance matrix upper right triangle (states: vx, vy, vz, rollspeed, pitchspeed, yawspeed; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        reset_counter             : Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. (type:uint8_t)
        estimator_type            : Type of estimator that is providing the odometry. (type:uint8_t, values:MAV_ESTIMATOR_TYPE)
        quality                   : Optional odometry quality metric as a percentage. -1 = odometry has failed, 0 = unknown/unset quality, 1 = worst quality, 100 = best quality [%] (type:int8_t)

        """
        return MAVLink_odometry_message(time_usec, frame_id, child_frame_id, x, y, z, q, vx, vy, vz, rollspeed, pitchspeed, yawspeed, pose_covariance, velocity_covariance, reset_counter, estimator_type, quality)

## odometry_send
    def odometry_send(self, time_usec: int, frame_id: int, child_frame_id: int, x: float, y: float, z: float, q: Sequence[float], vx: float, vy: float, vz: float, rollspeed: float, pitchspeed: float, yawspeed: float, pose_covariance: Sequence[float], velocity_covariance: Sequence[float], reset_counter: int = 0, estimator_type: int = 0, quality: int = 0, force_mavlink1: bool = False) -> None:
        """
        Odometry message to communicate odometry information with an external
        interface. Fits ROS REP 147 standard for aerial vehicles
        (http://www.ros.org/reps/rep-0147.html).

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        frame_id                  : Coordinate frame of reference for the pose data. (type:uint8_t, values:MAV_FRAME)
        child_frame_id            : Coordinate frame of reference for the velocity in free space (twist) data. (type:uint8_t, values:MAV_FRAME)
        x                         : X Position [m] (type:float)
        y                         : Y Position [m] (type:float)
        z                         : Z Position [m] (type:float)
        q                         : Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation) (type:float)
        vx                        : X linear speed [m/s] (type:float)
        vy                        : Y linear speed [m/s] (type:float)
        vz                        : Z linear speed [m/s] (type:float)
        rollspeed                 : Roll angular speed [rad/s] (type:float)
        pitchspeed                : Pitch angular speed [rad/s] (type:float)
        yawspeed                  : Yaw angular speed [rad/s] (type:float)
        pose_covariance           : Row-major representation of a 6x6 pose cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        velocity_covariance        : Row-major representation of a 6x6 velocity cross-covariance matrix upper right triangle (states: vx, vy, vz, rollspeed, pitchspeed, yawspeed; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. (type:float)
        reset_counter             : Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. (type:uint8_t)
        estimator_type            : Type of estimator that is providing the odometry. (type:uint8_t, values:MAV_ESTIMATOR_TYPE)
        quality                   : Optional odometry quality metric as a percentage. -1 = odometry has failed, 0 = unknown/unset quality, 1 = worst quality, 100 = best quality [%] (type:int8_t)

        """
        self.send(self.odometry_encode(time_usec, frame_id, child_frame_id, x, y, z, q, vx, vy, vz, rollspeed, pitchspeed, yawspeed, pose_covariance, velocity_covariance, reset_counter, estimator_type, quality), force_mavlink1=force_mavlink1)

## trajectory_representation_waypoints_encode
    def trajectory_representation_waypoints_encode(self, time_usec: int, valid_points: int, pos_x: Sequence[float], pos_y: Sequence[float], pos_z: Sequence[float], vel_x: Sequence[float], vel_y: Sequence[float], vel_z: Sequence[float], acc_x: Sequence[float], acc_y: Sequence[float], acc_z: Sequence[float], pos_yaw: Sequence[float], vel_yaw: Sequence[float], command: Sequence[int]) -> MAVLink_trajectory_representation_waypoints_message:
        """
        Describe a trajectory using an array of up-to 5 waypoints in the local
        frame (MAV_FRAME_LOCAL_NED).

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        valid_points              : Number of valid points (up-to 5 waypoints are possible) (type:uint8_t)
        pos_x                     : X-coordinate of waypoint, set to NaN if not being used [m] (type:float)
        pos_y                     : Y-coordinate of waypoint, set to NaN if not being used [m] (type:float)
        pos_z                     : Z-coordinate of waypoint, set to NaN if not being used [m] (type:float)
        vel_x                     : X-velocity of waypoint, set to NaN if not being used [m/s] (type:float)
        vel_y                     : Y-velocity of waypoint, set to NaN if not being used [m/s] (type:float)
        vel_z                     : Z-velocity of waypoint, set to NaN if not being used [m/s] (type:float)
        acc_x                     : X-acceleration of waypoint, set to NaN if not being used [m/s/s] (type:float)
        acc_y                     : Y-acceleration of waypoint, set to NaN if not being used [m/s/s] (type:float)
        acc_z                     : Z-acceleration of waypoint, set to NaN if not being used [m/s/s] (type:float)
        pos_yaw                   : Yaw angle, set to NaN if not being used [rad] (type:float)
        vel_yaw                   : Yaw rate, set to NaN if not being used [rad/s] (type:float)
        command                   : MAV_CMD command id of waypoint, set to UINT16_MAX if not being used. (type:uint16_t, values:MAV_CMD)

        """
        return MAVLink_trajectory_representation_waypoints_message(time_usec, valid_points, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z, pos_yaw, vel_yaw, command)

## trajectory_representation_waypoints_send
    def trajectory_representation_waypoints_send(self, time_usec: int, valid_points: int, pos_x: Sequence[float], pos_y: Sequence[float], pos_z: Sequence[float], vel_x: Sequence[float], vel_y: Sequence[float], vel_z: Sequence[float], acc_x: Sequence[float], acc_y: Sequence[float], acc_z: Sequence[float], pos_yaw: Sequence[float], vel_yaw: Sequence[float], command: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Describe a trajectory using an array of up-to 5 waypoints in the local
        frame (MAV_FRAME_LOCAL_NED).

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        valid_points              : Number of valid points (up-to 5 waypoints are possible) (type:uint8_t)
        pos_x                     : X-coordinate of waypoint, set to NaN if not being used [m] (type:float)
        pos_y                     : Y-coordinate of waypoint, set to NaN if not being used [m] (type:float)
        pos_z                     : Z-coordinate of waypoint, set to NaN if not being used [m] (type:float)
        vel_x                     : X-velocity of waypoint, set to NaN if not being used [m/s] (type:float)
        vel_y                     : Y-velocity of waypoint, set to NaN if not being used [m/s] (type:float)
        vel_z                     : Z-velocity of waypoint, set to NaN if not being used [m/s] (type:float)
        acc_x                     : X-acceleration of waypoint, set to NaN if not being used [m/s/s] (type:float)
        acc_y                     : Y-acceleration of waypoint, set to NaN if not being used [m/s/s] (type:float)
        acc_z                     : Z-acceleration of waypoint, set to NaN if not being used [m/s/s] (type:float)
        pos_yaw                   : Yaw angle, set to NaN if not being used [rad] (type:float)
        vel_yaw                   : Yaw rate, set to NaN if not being used [rad/s] (type:float)
        command                   : MAV_CMD command id of waypoint, set to UINT16_MAX if not being used. (type:uint16_t, values:MAV_CMD)

        """
        self.send(self.trajectory_representation_waypoints_encode(time_usec, valid_points, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z, pos_yaw, vel_yaw, command), force_mavlink1=force_mavlink1)

## trajectory_representation_bezier_encode
    def trajectory_representation_bezier_encode(self, time_usec: int, valid_points: int, pos_x: Sequence[float], pos_y: Sequence[float], pos_z: Sequence[float], delta: Sequence[float], pos_yaw: Sequence[float]) -> MAVLink_trajectory_representation_bezier_message:
        """
        Describe a trajectory using an array of up-to 5 bezier control points
        in the local frame (MAV_FRAME_LOCAL_NED).

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        valid_points              : Number of valid control points (up-to 5 points are possible) (type:uint8_t)
        pos_x                     : X-coordinate of bezier control points. Set to NaN if not being used [m] (type:float)
        pos_y                     : Y-coordinate of bezier control points. Set to NaN if not being used [m] (type:float)
        pos_z                     : Z-coordinate of bezier control points. Set to NaN if not being used [m] (type:float)
        delta                     : Bezier time horizon. Set to NaN if velocity/acceleration should not be incorporated [s] (type:float)
        pos_yaw                   : Yaw. Set to NaN for unchanged [rad] (type:float)

        """
        return MAVLink_trajectory_representation_bezier_message(time_usec, valid_points, pos_x, pos_y, pos_z, delta, pos_yaw)

## trajectory_representation_bezier_send
    def trajectory_representation_bezier_send(self, time_usec: int, valid_points: int, pos_x: Sequence[float], pos_y: Sequence[float], pos_z: Sequence[float], delta: Sequence[float], pos_yaw: Sequence[float], force_mavlink1: bool = False) -> None:
        """
        Describe a trajectory using an array of up-to 5 bezier control points
        in the local frame (MAV_FRAME_LOCAL_NED).

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        valid_points              : Number of valid control points (up-to 5 points are possible) (type:uint8_t)
        pos_x                     : X-coordinate of bezier control points. Set to NaN if not being used [m] (type:float)
        pos_y                     : Y-coordinate of bezier control points. Set to NaN if not being used [m] (type:float)
        pos_z                     : Z-coordinate of bezier control points. Set to NaN if not being used [m] (type:float)
        delta                     : Bezier time horizon. Set to NaN if velocity/acceleration should not be incorporated [s] (type:float)
        pos_yaw                   : Yaw. Set to NaN for unchanged [rad] (type:float)

        """
        self.send(self.trajectory_representation_bezier_encode(time_usec, valid_points, pos_x, pos_y, pos_z, delta, pos_yaw), force_mavlink1=force_mavlink1)

## isbd_link_status_encode
    def isbd_link_status_encode(self, timestamp: int, last_heartbeat: int, failed_sessions: int, successful_sessions: int, signal_quality: int, ring_pending: int, tx_session_pending: int, rx_session_pending: int) -> MAVLink_isbd_link_status_message:
        """
        Status of the Iridium SBD link.

        timestamp                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        last_heartbeat            : Timestamp of the last successful sbd session. The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        failed_sessions           : Number of failed SBD sessions. (type:uint16_t)
        successful_sessions        : Number of successful SBD sessions. (type:uint16_t)
        signal_quality            : Signal quality equal to the number of bars displayed on the ISU signal strength indicator. Range is 0 to 5, where 0 indicates no signal and 5 indicates maximum signal strength. (type:uint8_t)
        ring_pending              : 1: Ring call pending, 0: No call pending. (type:uint8_t)
        tx_session_pending        : 1: Transmission session pending, 0: No transmission session pending. (type:uint8_t)
        rx_session_pending        : 1: Receiving session pending, 0: No receiving session pending. (type:uint8_t)

        """
        return MAVLink_isbd_link_status_message(timestamp, last_heartbeat, failed_sessions, successful_sessions, signal_quality, ring_pending, tx_session_pending, rx_session_pending)

## isbd_link_status_send
    def isbd_link_status_send(self, timestamp: int, last_heartbeat: int, failed_sessions: int, successful_sessions: int, signal_quality: int, ring_pending: int, tx_session_pending: int, rx_session_pending: int, force_mavlink1: bool = False) -> None:
        """
        Status of the Iridium SBD link.

        timestamp                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        last_heartbeat            : Timestamp of the last successful sbd session. The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        failed_sessions           : Number of failed SBD sessions. (type:uint16_t)
        successful_sessions        : Number of successful SBD sessions. (type:uint16_t)
        signal_quality            : Signal quality equal to the number of bars displayed on the ISU signal strength indicator. Range is 0 to 5, where 0 indicates no signal and 5 indicates maximum signal strength. (type:uint8_t)
        ring_pending              : 1: Ring call pending, 0: No call pending. (type:uint8_t)
        tx_session_pending        : 1: Transmission session pending, 0: No transmission session pending. (type:uint8_t)
        rx_session_pending        : 1: Receiving session pending, 0: No receiving session pending. (type:uint8_t)

        """
        self.send(self.isbd_link_status_encode(timestamp, last_heartbeat, failed_sessions, successful_sessions, signal_quality, ring_pending, tx_session_pending, rx_session_pending), force_mavlink1=force_mavlink1)

## raw_rpm_encode
    def raw_rpm_encode(self, index: int, frequency: float) -> MAVLink_raw_rpm_message:
        """
        RPM sensor data message.

        index                     : Index of this RPM sensor (0-indexed) (type:uint8_t)
        frequency                 : Indicated rate [rpm] (type:float)

        """
        return MAVLink_raw_rpm_message(index, frequency)

## raw_rpm_send
    def raw_rpm_send(self, index: int, frequency: float, force_mavlink1: bool = False) -> None:
        """
        RPM sensor data message.

        index                     : Index of this RPM sensor (0-indexed) (type:uint8_t)
        frequency                 : Indicated rate [rpm] (type:float)

        """
        self.send(self.raw_rpm_encode(index, frequency), force_mavlink1=force_mavlink1)

## utm_global_position_encode
    def utm_global_position_encode(self, time: int, uas_id: Sequence[int], lat: int, lon: int, alt: int, relative_alt: int, vx: int, vy: int, vz: int, h_acc: int, v_acc: int, vel_acc: int, next_lat: int, next_lon: int, next_alt: int, update_rate: int, flight_state: int, flags: int) -> MAVLink_utm_global_position_message:
        """
        The global position resulting from GPS and sensor fusion.

        time                      : Time of applicability of position (microseconds since UNIX epoch). [us] (type:uint64_t)
        uas_id                    : Unique UAS ID. (type:uint8_t)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (WGS84) [mm] (type:int32_t)
        relative_alt              : Altitude above ground [mm] (type:int32_t)
        vx                        : Ground X speed (latitude, positive north) [cm/s] (type:int16_t)
        vy                        : Ground Y speed (longitude, positive east) [cm/s] (type:int16_t)
        vz                        : Ground Z speed (altitude, positive down) [cm/s] (type:int16_t)
        h_acc                     : Horizontal position uncertainty (standard deviation) [mm] (type:uint16_t)
        v_acc                     : Altitude uncertainty (standard deviation) [mm] (type:uint16_t)
        vel_acc                   : Speed uncertainty (standard deviation) [cm/s] (type:uint16_t)
        next_lat                  : Next waypoint, latitude (WGS84) [degE7] (type:int32_t)
        next_lon                  : Next waypoint, longitude (WGS84) [degE7] (type:int32_t)
        next_alt                  : Next waypoint, altitude (WGS84) [mm] (type:int32_t)
        update_rate               : Time until next update. Set to 0 if unknown or in data driven mode. [cs] (type:uint16_t)
        flight_state              : Flight state (type:uint8_t, values:UTM_FLIGHT_STATE)
        flags                     : Bitwise OR combination of the data available flags. (type:uint8_t, values:UTM_DATA_AVAIL_FLAGS)

        """
        return MAVLink_utm_global_position_message(time, uas_id, lat, lon, alt, relative_alt, vx, vy, vz, h_acc, v_acc, vel_acc, next_lat, next_lon, next_alt, update_rate, flight_state, flags)

## utm_global_position_send
    def utm_global_position_send(self, time: int, uas_id: Sequence[int], lat: int, lon: int, alt: int, relative_alt: int, vx: int, vy: int, vz: int, h_acc: int, v_acc: int, vel_acc: int, next_lat: int, next_lon: int, next_alt: int, update_rate: int, flight_state: int, flags: int, force_mavlink1: bool = False) -> None:
        """
        The global position resulting from GPS and sensor fusion.

        time                      : Time of applicability of position (microseconds since UNIX epoch). [us] (type:uint64_t)
        uas_id                    : Unique UAS ID. (type:uint8_t)
        lat                       : Latitude (WGS84) [degE7] (type:int32_t)
        lon                       : Longitude (WGS84) [degE7] (type:int32_t)
        alt                       : Altitude (WGS84) [mm] (type:int32_t)
        relative_alt              : Altitude above ground [mm] (type:int32_t)
        vx                        : Ground X speed (latitude, positive north) [cm/s] (type:int16_t)
        vy                        : Ground Y speed (longitude, positive east) [cm/s] (type:int16_t)
        vz                        : Ground Z speed (altitude, positive down) [cm/s] (type:int16_t)
        h_acc                     : Horizontal position uncertainty (standard deviation) [mm] (type:uint16_t)
        v_acc                     : Altitude uncertainty (standard deviation) [mm] (type:uint16_t)
        vel_acc                   : Speed uncertainty (standard deviation) [cm/s] (type:uint16_t)
        next_lat                  : Next waypoint, latitude (WGS84) [degE7] (type:int32_t)
        next_lon                  : Next waypoint, longitude (WGS84) [degE7] (type:int32_t)
        next_alt                  : Next waypoint, altitude (WGS84) [mm] (type:int32_t)
        update_rate               : Time until next update. Set to 0 if unknown or in data driven mode. [cs] (type:uint16_t)
        flight_state              : Flight state (type:uint8_t, values:UTM_FLIGHT_STATE)
        flags                     : Bitwise OR combination of the data available flags. (type:uint8_t, values:UTM_DATA_AVAIL_FLAGS)

        """
        self.send(self.utm_global_position_encode(time, uas_id, lat, lon, alt, relative_alt, vx, vy, vz, h_acc, v_acc, vel_acc, next_lat, next_lon, next_alt, update_rate, flight_state, flags), force_mavlink1=force_mavlink1)

## debug_float_array_encode
    def debug_float_array_encode(self, time_usec: int, name: bytes, array_id: int, data: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)) -> MAVLink_debug_float_array_message:
        """
        Large debug/prototyping array. The message uses the maximum available
        payload for data. The array_id and name fields are used to
        discriminate between messages in code and in user interfaces
        (respectively). Do not use in production code.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        name                      : Name, for human-friendly display in a Ground Control Station (type:char)
        array_id                  : Unique ID used to discriminate between arrays (type:uint16_t)
        data                      : data (type:float)

        """
        return MAVLink_debug_float_array_message(time_usec, name, array_id, data)

## debug_float_array_send
    def debug_float_array_send(self, time_usec: int, name: bytes, array_id: int, data: Sequence[float] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), force_mavlink1: bool = False) -> None:
        """
        Large debug/prototyping array. The message uses the maximum available
        payload for data. The array_id and name fields are used to
        discriminate between messages in code and in user interfaces
        (respectively). Do not use in production code.

        time_usec                 : Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. [us] (type:uint64_t)
        name                      : Name, for human-friendly display in a Ground Control Station (type:char)
        array_id                  : Unique ID used to discriminate between arrays (type:uint16_t)
        data                      : data (type:float)

        """
        self.send(self.debug_float_array_encode(time_usec, name, array_id, data), force_mavlink1=force_mavlink1)

## smart_battery_info_encode
    def smart_battery_info_encode(self, id: int, battery_function: int, type: int, capacity_full_specification: int, capacity_full: int, cycle_count: int, serial_number: bytes, device_name: bytes, weight: int, discharge_minimum_voltage: int, charging_minimum_voltage: int, resting_minimum_voltage: int, charging_maximum_voltage: int = 0, cells_in_series: int = 0, discharge_maximum_current: int = 0, discharge_maximum_burst_current: int = 0, manufacture_date: bytes = b"") -> MAVLink_smart_battery_info_message:
        """
        Smart Battery information (static/infrequent update). Use for updates
        from: smart battery to flight stack, flight stack to GCS. Use
        BATTERY_STATUS for smart battery frequent updates.

        id                        : Battery ID (type:uint8_t)
        battery_function          : Function of the battery (type:uint8_t, values:MAV_BATTERY_FUNCTION)
        type                      : Type (chemistry) of the battery (type:uint8_t, values:MAV_BATTERY_TYPE)
        capacity_full_specification        : Capacity when full according to manufacturer, -1: field not provided. [mAh] (type:int32_t)
        capacity_full             : Capacity when full (accounting for battery degradation), -1: field not provided. [mAh] (type:int32_t)
        cycle_count               : Charge/discharge cycle count. UINT16_MAX: field not provided. (type:uint16_t)
        serial_number             : Serial number in ASCII characters, 0 terminated. All 0: field not provided. (type:char)
        device_name               : Static device name in ASCII characters, 0 terminated. All 0: field not provided. Encode as manufacturer name then product name separated using an underscore. (type:char)
        weight                    : Battery weight. 0: field not provided. [g] (type:uint16_t)
        discharge_minimum_voltage        : Minimum per-cell voltage when discharging. If not supplied set to UINT16_MAX value. [mV] (type:uint16_t)
        charging_minimum_voltage        : Minimum per-cell voltage when charging. If not supplied set to UINT16_MAX value. [mV] (type:uint16_t)
        resting_minimum_voltage        : Minimum per-cell voltage when resting. If not supplied set to UINT16_MAX value. [mV] (type:uint16_t)
        charging_maximum_voltage        : Maximum per-cell voltage when charged. 0: field not provided. [mV] (type:uint16_t)
        cells_in_series           : Number of battery cells in series. 0: field not provided. (type:uint8_t)
        discharge_maximum_current        : Maximum pack discharge current. 0: field not provided. [mA] (type:uint32_t)
        discharge_maximum_burst_current        : Maximum pack discharge burst current. 0: field not provided. [mA] (type:uint32_t)
        manufacture_date          : Manufacture date (DD/MM/YYYY) in ASCII characters, 0 terminated. All 0: field not provided. (type:char)

        """
        return MAVLink_smart_battery_info_message(id, battery_function, type, capacity_full_specification, capacity_full, cycle_count, serial_number, device_name, weight, discharge_minimum_voltage, charging_minimum_voltage, resting_minimum_voltage, charging_maximum_voltage, cells_in_series, discharge_maximum_current, discharge_maximum_burst_current, manufacture_date)

## smart_battery_info_send
    def smart_battery_info_send(self, id: int, battery_function: int, type: int, capacity_full_specification: int, capacity_full: int, cycle_count: int, serial_number: bytes, device_name: bytes, weight: int, discharge_minimum_voltage: int, charging_minimum_voltage: int, resting_minimum_voltage: int, charging_maximum_voltage: int = 0, cells_in_series: int = 0, discharge_maximum_current: int = 0, discharge_maximum_burst_current: int = 0, manufacture_date: bytes = b"", force_mavlink1: bool = False) -> None:
        """
        Smart Battery information (static/infrequent update). Use for updates
        from: smart battery to flight stack, flight stack to GCS. Use
        BATTERY_STATUS for smart battery frequent updates.

        id                        : Battery ID (type:uint8_t)
        battery_function          : Function of the battery (type:uint8_t, values:MAV_BATTERY_FUNCTION)
        type                      : Type (chemistry) of the battery (type:uint8_t, values:MAV_BATTERY_TYPE)
        capacity_full_specification        : Capacity when full according to manufacturer, -1: field not provided. [mAh] (type:int32_t)
        capacity_full             : Capacity when full (accounting for battery degradation), -1: field not provided. [mAh] (type:int32_t)
        cycle_count               : Charge/discharge cycle count. UINT16_MAX: field not provided. (type:uint16_t)
        serial_number             : Serial number in ASCII characters, 0 terminated. All 0: field not provided. (type:char)
        device_name               : Static device name in ASCII characters, 0 terminated. All 0: field not provided. Encode as manufacturer name then product name separated using an underscore. (type:char)
        weight                    : Battery weight. 0: field not provided. [g] (type:uint16_t)
        discharge_minimum_voltage        : Minimum per-cell voltage when discharging. If not supplied set to UINT16_MAX value. [mV] (type:uint16_t)
        charging_minimum_voltage        : Minimum per-cell voltage when charging. If not supplied set to UINT16_MAX value. [mV] (type:uint16_t)
        resting_minimum_voltage        : Minimum per-cell voltage when resting. If not supplied set to UINT16_MAX value. [mV] (type:uint16_t)
        charging_maximum_voltage        : Maximum per-cell voltage when charged. 0: field not provided. [mV] (type:uint16_t)
        cells_in_series           : Number of battery cells in series. 0: field not provided. (type:uint8_t)
        discharge_maximum_current        : Maximum pack discharge current. 0: field not provided. [mA] (type:uint32_t)
        discharge_maximum_burst_current        : Maximum pack discharge burst current. 0: field not provided. [mA] (type:uint32_t)
        manufacture_date          : Manufacture date (DD/MM/YYYY) in ASCII characters, 0 terminated. All 0: field not provided. (type:char)

        """
        self.send(self.smart_battery_info_encode(id, battery_function, type, capacity_full_specification, capacity_full, cycle_count, serial_number, device_name, weight, discharge_minimum_voltage, charging_minimum_voltage, resting_minimum_voltage, charging_maximum_voltage, cells_in_series, discharge_maximum_current, discharge_maximum_burst_current, manufacture_date), force_mavlink1=force_mavlink1)

## generator_status_encode
    def generator_status_encode(self, status: int, generator_speed: int, battery_current: float, load_current: float, power_generated: float, bus_voltage: float, rectifier_temperature: int, bat_current_setpoint: float, generator_temperature: int, runtime: int, time_until_maintenance: int) -> MAVLink_generator_status_message:
        """
        Telemetry of power generation system. Alternator or mechanical
        generator.

        status                    : Status flags. (type:uint64_t, values:MAV_GENERATOR_STATUS_FLAG)
        generator_speed           : Speed of electrical generator or alternator. UINT16_MAX: field not provided. [rpm] (type:uint16_t)
        battery_current           : Current into/out of battery. Positive for out. Negative for in. NaN: field not provided. [A] (type:float)
        load_current              : Current going to the UAV. If battery current not available this is the DC current from the generator. Positive for out. Negative for in. NaN: field not provided [A] (type:float)
        power_generated           : The power being generated. NaN: field not provided [W] (type:float)
        bus_voltage               : Voltage of the bus seen at the generator, or battery bus if battery bus is controlled by generator and at a different voltage to main bus. [V] (type:float)
        rectifier_temperature        : The temperature of the rectifier or power converter. INT16_MAX: field not provided. [degC] (type:int16_t)
        bat_current_setpoint        : The target battery current. Positive for out. Negative for in. NaN: field not provided [A] (type:float)
        generator_temperature        : The temperature of the mechanical motor, fuel cell core or generator. INT16_MAX: field not provided. [degC] (type:int16_t)
        runtime                   : Seconds this generator has run since it was rebooted. UINT32_MAX: field not provided. [s] (type:uint32_t)
        time_until_maintenance        : Seconds until this generator requires maintenance.  A negative value indicates maintenance is past-due. INT32_MAX: field not provided. [s] (type:int32_t)

        """
        return MAVLink_generator_status_message(status, generator_speed, battery_current, load_current, power_generated, bus_voltage, rectifier_temperature, bat_current_setpoint, generator_temperature, runtime, time_until_maintenance)

## generator_status_send
    def generator_status_send(self, status: int, generator_speed: int, battery_current: float, load_current: float, power_generated: float, bus_voltage: float, rectifier_temperature: int, bat_current_setpoint: float, generator_temperature: int, runtime: int, time_until_maintenance: int, force_mavlink1: bool = False) -> None:
        """
        Telemetry of power generation system. Alternator or mechanical
        generator.

        status                    : Status flags. (type:uint64_t, values:MAV_GENERATOR_STATUS_FLAG)
        generator_speed           : Speed of electrical generator or alternator. UINT16_MAX: field not provided. [rpm] (type:uint16_t)
        battery_current           : Current into/out of battery. Positive for out. Negative for in. NaN: field not provided. [A] (type:float)
        load_current              : Current going to the UAV. If battery current not available this is the DC current from the generator. Positive for out. Negative for in. NaN: field not provided [A] (type:float)
        power_generated           : The power being generated. NaN: field not provided [W] (type:float)
        bus_voltage               : Voltage of the bus seen at the generator, or battery bus if battery bus is controlled by generator and at a different voltage to main bus. [V] (type:float)
        rectifier_temperature        : The temperature of the rectifier or power converter. INT16_MAX: field not provided. [degC] (type:int16_t)
        bat_current_setpoint        : The target battery current. Positive for out. Negative for in. NaN: field not provided [A] (type:float)
        generator_temperature        : The temperature of the mechanical motor, fuel cell core or generator. INT16_MAX: field not provided. [degC] (type:int16_t)
        runtime                   : Seconds this generator has run since it was rebooted. UINT32_MAX: field not provided. [s] (type:uint32_t)
        time_until_maintenance        : Seconds until this generator requires maintenance.  A negative value indicates maintenance is past-due. INT32_MAX: field not provided. [s] (type:int32_t)

        """
        self.send(self.generator_status_encode(status, generator_speed, battery_current, load_current, power_generated, bus_voltage, rectifier_temperature, bat_current_setpoint, generator_temperature, runtime, time_until_maintenance), force_mavlink1=force_mavlink1)

## actuator_output_status_encode
    def actuator_output_status_encode(self, time_usec: int, active: int, actuator: Sequence[float]) -> MAVLink_actuator_output_status_message:
        """
        The raw values of the actuator outputs (e.g. on Pixhawk, from MAIN,
        AUX ports). This message supersedes SERVO_OUTPUT_RAW.

        time_usec                 : Timestamp (since system boot). [us] (type:uint64_t)
        active                    : Active outputs (type:uint32_t)
        actuator                  : Servo / motor output array values. Zero values indicate unused channels. (type:float)

        """
        return MAVLink_actuator_output_status_message(time_usec, active, actuator)

## actuator_output_status_send
    def actuator_output_status_send(self, time_usec: int, active: int, actuator: Sequence[float], force_mavlink1: bool = False) -> None:
        """
        The raw values of the actuator outputs (e.g. on Pixhawk, from MAIN,
        AUX ports). This message supersedes SERVO_OUTPUT_RAW.

        time_usec                 : Timestamp (since system boot). [us] (type:uint64_t)
        active                    : Active outputs (type:uint32_t)
        actuator                  : Servo / motor output array values. Zero values indicate unused channels. (type:float)

        """
        self.send(self.actuator_output_status_encode(time_usec, active, actuator), force_mavlink1=force_mavlink1)

## relay_status_encode
    def relay_status_encode(self, time_boot_ms: int, on: int, present: int) -> MAVLink_relay_status_message:
        """
        Reports the on/off state of relays, as controlled by
        MAV_CMD_DO_SET_RELAY.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        on                        : Relay states.  Relay instance numbers are represented as individual bits in this mask by offset. (type:uint16_t)
        present                   : Relay present.  Relay instance numbers are represented as individual bits in this mask by offset.  Bits will be true if a relay instance is configured. (type:uint16_t)

        """
        return MAVLink_relay_status_message(time_boot_ms, on, present)

## relay_status_send
    def relay_status_send(self, time_boot_ms: int, on: int, present: int, force_mavlink1: bool = False) -> None:
        """
        Reports the on/off state of relays, as controlled by
        MAV_CMD_DO_SET_RELAY.

        time_boot_ms              : Timestamp (time since system boot). [ms] (type:uint32_t)
        on                        : Relay states.  Relay instance numbers are represented as individual bits in this mask by offset. (type:uint16_t)
        present                   : Relay present.  Relay instance numbers are represented as individual bits in this mask by offset.  Bits will be true if a relay instance is configured. (type:uint16_t)

        """
        self.send(self.relay_status_encode(time_boot_ms, on, present), force_mavlink1=force_mavlink1)

## tunnel_encode
    def tunnel_encode(self, target_system: int, target_component: int, payload_type: int, payload_length: int, payload: Sequence[int]) -> MAVLink_tunnel_message:
        """
        Message for transporting "arbitrary" variable-length data from one
        component to another (broadcast is not forbidden, but
        discouraged). The encoding of the data is usually extension
        specific, i.e. determined by the source, and is usually not
        documented as part of the MAVLink specification.

        target_system             : System ID (can be 0 for broadcast, but this is discouraged) (type:uint8_t)
        target_component          : Component ID (can be 0 for broadcast, but this is discouraged) (type:uint8_t)
        payload_type              : A code that identifies the content of the payload (0 for unknown, which is the default). If this code is less than 32768, it is a 'registered' payload type and the corresponding code should be added to the MAV_TUNNEL_PAYLOAD_TYPE enum. Software creators can register blocks of types as needed. Codes greater than 32767 are considered local experiments and should not be checked in to any widely distributed codebase. (type:uint16_t, values:MAV_TUNNEL_PAYLOAD_TYPE)
        payload_length            : Length of the data transported in payload (type:uint8_t)
        payload                   : Variable length payload. The payload length is defined by payload_length. The entire content of this block is opaque unless you understand the encoding specified by payload_type. (type:uint8_t)

        """
        return MAVLink_tunnel_message(target_system, target_component, payload_type, payload_length, payload)

## tunnel_send
    def tunnel_send(self, target_system: int, target_component: int, payload_type: int, payload_length: int, payload: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Message for transporting "arbitrary" variable-length data from one
        component to another (broadcast is not forbidden, but
        discouraged). The encoding of the data is usually extension
        specific, i.e. determined by the source, and is usually not
        documented as part of the MAVLink specification.

        target_system             : System ID (can be 0 for broadcast, but this is discouraged) (type:uint8_t)
        target_component          : Component ID (can be 0 for broadcast, but this is discouraged) (type:uint8_t)
        payload_type              : A code that identifies the content of the payload (0 for unknown, which is the default). If this code is less than 32768, it is a 'registered' payload type and the corresponding code should be added to the MAV_TUNNEL_PAYLOAD_TYPE enum. Software creators can register blocks of types as needed. Codes greater than 32767 are considered local experiments and should not be checked in to any widely distributed codebase. (type:uint16_t, values:MAV_TUNNEL_PAYLOAD_TYPE)
        payload_length            : Length of the data transported in payload (type:uint8_t)
        payload                   : Variable length payload. The payload length is defined by payload_length. The entire content of this block is opaque unless you understand the encoding specified by payload_type. (type:uint8_t)

        """
        self.send(self.tunnel_encode(target_system, target_component, payload_type, payload_length, payload), force_mavlink1=force_mavlink1)

## can_frame_encode
    def can_frame_encode(self, target_system: int, target_component: int, bus: int, len: int, id: int, data: Sequence[int]) -> MAVLink_can_frame_message:
        """
        A forwarded CAN frame as requested by MAV_CMD_CAN_FORWARD.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        bus                       : Bus number (type:uint8_t)
        len                       : Frame length (type:uint8_t)
        id                        : Frame ID (type:uint32_t)
        data                      : Frame data (type:uint8_t)

        """
        return MAVLink_can_frame_message(target_system, target_component, bus, len, id, data)

## can_frame_send
    def can_frame_send(self, target_system: int, target_component: int, bus: int, len: int, id: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        A forwarded CAN frame as requested by MAV_CMD_CAN_FORWARD.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        bus                       : Bus number (type:uint8_t)
        len                       : Frame length (type:uint8_t)
        id                        : Frame ID (type:uint32_t)
        data                      : Frame data (type:uint8_t)

        """
        self.send(self.can_frame_encode(target_system, target_component, bus, len, id, data), force_mavlink1=force_mavlink1)

## canfd_frame_encode
    def canfd_frame_encode(self, target_system: int, target_component: int, bus: int, len: int, id: int, data: Sequence[int]) -> MAVLink_canfd_frame_message:
        """
        A forwarded CANFD frame as requested by MAV_CMD_CAN_FORWARD. These are
        separated from CAN_FRAME as they need different handling (eg.
        TAO handling)

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        bus                       : bus number (type:uint8_t)
        len                       : Frame length (type:uint8_t)
        id                        : Frame ID (type:uint32_t)
        data                      : Frame data (type:uint8_t)

        """
        return MAVLink_canfd_frame_message(target_system, target_component, bus, len, id, data)

## canfd_frame_send
    def canfd_frame_send(self, target_system: int, target_component: int, bus: int, len: int, id: int, data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        A forwarded CANFD frame as requested by MAV_CMD_CAN_FORWARD. These are
        separated from CAN_FRAME as they need different handling (eg.
        TAO handling)

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        bus                       : bus number (type:uint8_t)
        len                       : Frame length (type:uint8_t)
        id                        : Frame ID (type:uint32_t)
        data                      : Frame data (type:uint8_t)

        """
        self.send(self.canfd_frame_encode(target_system, target_component, bus, len, id, data), force_mavlink1=force_mavlink1)

## can_filter_modify_encode
    def can_filter_modify_encode(self, target_system: int, target_component: int, bus: int, operation: int, num_ids: int, ids: Sequence[int]) -> MAVLink_can_filter_modify_message:
        """
        Modify the filter of what CAN messages to forward over the mavlink.
        This can be used to make CAN forwarding work well on low
        bandwidth links. The filtering is applied on bits 8 to 24 of
        the CAN id (2nd and 3rd bytes) which corresponds to the
        DroneCAN message ID for DroneCAN. Filters with more than 16
        IDs can be constructed by sending multiple CAN_FILTER_MODIFY
        messages.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        bus                       : bus number (type:uint8_t)
        operation                 : what operation to perform on the filter list. See CAN_FILTER_OP enum. (type:uint8_t, values:CAN_FILTER_OP)
        num_ids                   : number of IDs in filter list (type:uint8_t)
        ids                       : filter IDs, length num_ids (type:uint16_t)

        """
        return MAVLink_can_filter_modify_message(target_system, target_component, bus, operation, num_ids, ids)

## can_filter_modify_send
    def can_filter_modify_send(self, target_system: int, target_component: int, bus: int, operation: int, num_ids: int, ids: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Modify the filter of what CAN messages to forward over the mavlink.
        This can be used to make CAN forwarding work well on low
        bandwidth links. The filtering is applied on bits 8 to 24 of
        the CAN id (2nd and 3rd bytes) which corresponds to the
        DroneCAN message ID for DroneCAN. Filters with more than 16
        IDs can be constructed by sending multiple CAN_FILTER_MODIFY
        messages.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        bus                       : bus number (type:uint8_t)
        operation                 : what operation to perform on the filter list. See CAN_FILTER_OP enum. (type:uint8_t, values:CAN_FILTER_OP)
        num_ids                   : number of IDs in filter list (type:uint8_t)
        ids                       : filter IDs, length num_ids (type:uint16_t)

        """
        self.send(self.can_filter_modify_encode(target_system, target_component, bus, operation, num_ids, ids), force_mavlink1=force_mavlink1)

## wheel_distance_encode
    def wheel_distance_encode(self, time_usec: int, count: int, distance: Sequence[float]) -> MAVLink_wheel_distance_message:
        """
        Cumulative distance traveled for each reported wheel.

        time_usec                 : Timestamp (synced to UNIX time or since system boot). [us] (type:uint64_t)
        count                     : Number of wheels reported. (type:uint8_t)
        distance                  : Distance reported by individual wheel encoders. Forward rotations increase values, reverse rotations decrease them. Not all wheels will necessarily have wheel encoders; the mapping of encoders to wheel positions must be agreed/understood by the endpoints. [m] (type:double)

        """
        return MAVLink_wheel_distance_message(time_usec, count, distance)

## wheel_distance_send
    def wheel_distance_send(self, time_usec: int, count: int, distance: Sequence[float], force_mavlink1: bool = False) -> None:
        """
        Cumulative distance traveled for each reported wheel.

        time_usec                 : Timestamp (synced to UNIX time or since system boot). [us] (type:uint64_t)
        count                     : Number of wheels reported. (type:uint8_t)
        distance                  : Distance reported by individual wheel encoders. Forward rotations increase values, reverse rotations decrease them. Not all wheels will necessarily have wheel encoders; the mapping of encoders to wheel positions must be agreed/understood by the endpoints. [m] (type:double)

        """
        self.send(self.wheel_distance_encode(time_usec, count, distance), force_mavlink1=force_mavlink1)

## winch_status_encode
    def winch_status_encode(self, time_usec: int, line_length: float, speed: float, tension: float, voltage: float, current: float, temperature: int, status: int) -> MAVLink_winch_status_message:
        """
        Winch status.

        time_usec                 : Timestamp (synced to UNIX time or since system boot). [us] (type:uint64_t)
        line_length               : Length of line released. NaN if unknown [m] (type:float)
        speed                     : Speed line is being released or retracted. Positive values if being released, negative values if being retracted, NaN if unknown [m/s] (type:float)
        tension                   : Tension on the line. NaN if unknown [kg] (type:float)
        voltage                   : Voltage of the battery supplying the winch. NaN if unknown [V] (type:float)
        current                   : Current draw from the winch. NaN if unknown [A] (type:float)
        temperature               : Temperature of the motor. INT16_MAX if unknown [degC] (type:int16_t)
        status                    : Status flags (type:uint32_t, values:MAV_WINCH_STATUS_FLAG)

        """
        return MAVLink_winch_status_message(time_usec, line_length, speed, tension, voltage, current, temperature, status)

## winch_status_send
    def winch_status_send(self, time_usec: int, line_length: float, speed: float, tension: float, voltage: float, current: float, temperature: int, status: int, force_mavlink1: bool = False) -> None:
        """
        Winch status.

        time_usec                 : Timestamp (synced to UNIX time or since system boot). [us] (type:uint64_t)
        line_length               : Length of line released. NaN if unknown [m] (type:float)
        speed                     : Speed line is being released or retracted. Positive values if being released, negative values if being retracted, NaN if unknown [m/s] (type:float)
        tension                   : Tension on the line. NaN if unknown [kg] (type:float)
        voltage                   : Voltage of the battery supplying the winch. NaN if unknown [V] (type:float)
        current                   : Current draw from the winch. NaN if unknown [A] (type:float)
        temperature               : Temperature of the motor. INT16_MAX if unknown [degC] (type:int16_t)
        status                    : Status flags (type:uint32_t, values:MAV_WINCH_STATUS_FLAG)

        """
        self.send(self.winch_status_encode(time_usec, line_length, speed, tension, voltage, current, temperature, status), force_mavlink1=force_mavlink1)

## open_drone_id_basic_id_encode
    def open_drone_id_basic_id_encode(self, target_system: int, target_component: int, id_or_mac: Sequence[int], id_type: int, ua_type: int, uas_id: Sequence[int]) -> MAVLink_open_drone_id_basic_id_message:
        """
        Data for filling the OpenDroneID Basic ID message. This and the below
        messages are primarily meant for feeding data to/from an
        OpenDroneID implementation. E.g.
        https://github.com/opendroneid/opendroneid-core-c. These
        messages are compatible with the ASTM F3411 Remote ID standard
        and the ASD-STAN prEN 4709-002 Direct Remote ID standard.
        Additional information and usage of these messages is
        documented at https://mavlink.io/en/services/opendroneid.html.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        id_type                   : Indicates the format for the uas_id field of this message. (type:uint8_t, values:MAV_ODID_ID_TYPE)
        ua_type                   : Indicates the type of UA (Unmanned Aircraft). (type:uint8_t, values:MAV_ODID_UA_TYPE)
        uas_id                    : UAS (Unmanned Aircraft System) ID following the format specified by id_type. Shall be filled with nulls in the unused portion of the field. (type:uint8_t)

        """
        return MAVLink_open_drone_id_basic_id_message(target_system, target_component, id_or_mac, id_type, ua_type, uas_id)

## open_drone_id_basic_id_send
    def open_drone_id_basic_id_send(self, target_system: int, target_component: int, id_or_mac: Sequence[int], id_type: int, ua_type: int, uas_id: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Data for filling the OpenDroneID Basic ID message. This and the below
        messages are primarily meant for feeding data to/from an
        OpenDroneID implementation. E.g.
        https://github.com/opendroneid/opendroneid-core-c. These
        messages are compatible with the ASTM F3411 Remote ID standard
        and the ASD-STAN prEN 4709-002 Direct Remote ID standard.
        Additional information and usage of these messages is
        documented at https://mavlink.io/en/services/opendroneid.html.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        id_type                   : Indicates the format for the uas_id field of this message. (type:uint8_t, values:MAV_ODID_ID_TYPE)
        ua_type                   : Indicates the type of UA (Unmanned Aircraft). (type:uint8_t, values:MAV_ODID_UA_TYPE)
        uas_id                    : UAS (Unmanned Aircraft System) ID following the format specified by id_type. Shall be filled with nulls in the unused portion of the field. (type:uint8_t)

        """
        self.send(self.open_drone_id_basic_id_encode(target_system, target_component, id_or_mac, id_type, ua_type, uas_id), force_mavlink1=force_mavlink1)

## open_drone_id_location_encode
    def open_drone_id_location_encode(self, target_system: int, target_component: int, id_or_mac: Sequence[int], status: int, direction: int, speed_horizontal: int, speed_vertical: int, latitude: int, longitude: int, altitude_barometric: float, altitude_geodetic: float, height_reference: int, height: float, horizontal_accuracy: int, vertical_accuracy: int, barometer_accuracy: int, speed_accuracy: int, timestamp: float, timestamp_accuracy: int) -> MAVLink_open_drone_id_location_message:
        """
        Data for filling the OpenDroneID Location message. The float data
        types are 32-bit IEEE 754. The Location message provides the
        location, altitude, direction and speed of the aircraft.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        status                    : Indicates whether the unmanned aircraft is on the ground or in the air. (type:uint8_t, values:MAV_ODID_STATUS)
        direction                 : Direction over ground (not heading, but direction of movement) measured clockwise from true North: 0 - 35999 centi-degrees. If unknown: 36100 centi-degrees. [cdeg] (type:uint16_t)
        speed_horizontal          : Ground speed. Positive only. If unknown: 25500 cm/s. If speed is larger than 25425 cm/s, use 25425 cm/s. [cm/s] (type:uint16_t)
        speed_vertical            : The vertical speed. Up is positive. If unknown: 6300 cm/s. If speed is larger than 6200 cm/s, use 6200 cm/s. If lower than -6200 cm/s, use -6200 cm/s. [cm/s] (type:int16_t)
        latitude                  : Current latitude of the unmanned aircraft. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        longitude                 : Current longitude of the unmanned aircraft. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        altitude_barometric        : The altitude calculated from the barometric pressure. Reference is against 29.92inHg or 1013.2mb. If unknown: -1000 m. [m] (type:float)
        altitude_geodetic         : The geodetic altitude as defined by WGS84. If unknown: -1000 m. [m] (type:float)
        height_reference          : Indicates the reference point for the height field. (type:uint8_t, values:MAV_ODID_HEIGHT_REF)
        height                    : The current height of the unmanned aircraft above the take-off location or the ground as indicated by height_reference. If unknown: -1000 m. [m] (type:float)
        horizontal_accuracy        : The accuracy of the horizontal position. (type:uint8_t, values:MAV_ODID_HOR_ACC)
        vertical_accuracy         : The accuracy of the vertical position. (type:uint8_t, values:MAV_ODID_VER_ACC)
        barometer_accuracy        : The accuracy of the barometric altitude. (type:uint8_t, values:MAV_ODID_VER_ACC)
        speed_accuracy            : The accuracy of the horizontal and vertical speed. (type:uint8_t, values:MAV_ODID_SPEED_ACC)
        timestamp                 : Seconds after the full hour with reference to UTC time. Typically the GPS outputs a time-of-week value in milliseconds. First convert that to UTC and then convert for this field using ((float) (time_week_ms % (60*60*1000))) / 1000. If unknown: 0xFFFF. [s] (type:float)
        timestamp_accuracy        : The accuracy of the timestamps. (type:uint8_t, values:MAV_ODID_TIME_ACC)

        """
        return MAVLink_open_drone_id_location_message(target_system, target_component, id_or_mac, status, direction, speed_horizontal, speed_vertical, latitude, longitude, altitude_barometric, altitude_geodetic, height_reference, height, horizontal_accuracy, vertical_accuracy, barometer_accuracy, speed_accuracy, timestamp, timestamp_accuracy)

## open_drone_id_location_send
    def open_drone_id_location_send(self, target_system: int, target_component: int, id_or_mac: Sequence[int], status: int, direction: int, speed_horizontal: int, speed_vertical: int, latitude: int, longitude: int, altitude_barometric: float, altitude_geodetic: float, height_reference: int, height: float, horizontal_accuracy: int, vertical_accuracy: int, barometer_accuracy: int, speed_accuracy: int, timestamp: float, timestamp_accuracy: int, force_mavlink1: bool = False) -> None:
        """
        Data for filling the OpenDroneID Location message. The float data
        types are 32-bit IEEE 754. The Location message provides the
        location, altitude, direction and speed of the aircraft.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        status                    : Indicates whether the unmanned aircraft is on the ground or in the air. (type:uint8_t, values:MAV_ODID_STATUS)
        direction                 : Direction over ground (not heading, but direction of movement) measured clockwise from true North: 0 - 35999 centi-degrees. If unknown: 36100 centi-degrees. [cdeg] (type:uint16_t)
        speed_horizontal          : Ground speed. Positive only. If unknown: 25500 cm/s. If speed is larger than 25425 cm/s, use 25425 cm/s. [cm/s] (type:uint16_t)
        speed_vertical            : The vertical speed. Up is positive. If unknown: 6300 cm/s. If speed is larger than 6200 cm/s, use 6200 cm/s. If lower than -6200 cm/s, use -6200 cm/s. [cm/s] (type:int16_t)
        latitude                  : Current latitude of the unmanned aircraft. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        longitude                 : Current longitude of the unmanned aircraft. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        altitude_barometric        : The altitude calculated from the barometric pressure. Reference is against 29.92inHg or 1013.2mb. If unknown: -1000 m. [m] (type:float)
        altitude_geodetic         : The geodetic altitude as defined by WGS84. If unknown: -1000 m. [m] (type:float)
        height_reference          : Indicates the reference point for the height field. (type:uint8_t, values:MAV_ODID_HEIGHT_REF)
        height                    : The current height of the unmanned aircraft above the take-off location or the ground as indicated by height_reference. If unknown: -1000 m. [m] (type:float)
        horizontal_accuracy        : The accuracy of the horizontal position. (type:uint8_t, values:MAV_ODID_HOR_ACC)
        vertical_accuracy         : The accuracy of the vertical position. (type:uint8_t, values:MAV_ODID_VER_ACC)
        barometer_accuracy        : The accuracy of the barometric altitude. (type:uint8_t, values:MAV_ODID_VER_ACC)
        speed_accuracy            : The accuracy of the horizontal and vertical speed. (type:uint8_t, values:MAV_ODID_SPEED_ACC)
        timestamp                 : Seconds after the full hour with reference to UTC time. Typically the GPS outputs a time-of-week value in milliseconds. First convert that to UTC and then convert for this field using ((float) (time_week_ms % (60*60*1000))) / 1000. If unknown: 0xFFFF. [s] (type:float)
        timestamp_accuracy        : The accuracy of the timestamps. (type:uint8_t, values:MAV_ODID_TIME_ACC)

        """
        self.send(self.open_drone_id_location_encode(target_system, target_component, id_or_mac, status, direction, speed_horizontal, speed_vertical, latitude, longitude, altitude_barometric, altitude_geodetic, height_reference, height, horizontal_accuracy, vertical_accuracy, barometer_accuracy, speed_accuracy, timestamp, timestamp_accuracy), force_mavlink1=force_mavlink1)

## open_drone_id_authentication_encode
    def open_drone_id_authentication_encode(self, target_system: int, target_component: int, id_or_mac: Sequence[int], authentication_type: int, data_page: int, last_page_index: int, length: int, timestamp: int, authentication_data: Sequence[int]) -> MAVLink_open_drone_id_authentication_message:
        """
        Data for filling the OpenDroneID Authentication message. The
        Authentication Message defines a field that can provide a
        means of authenticity for the identity of the UAS (Unmanned
        Aircraft System). The Authentication message can have two
        different formats. For data page 0, the fields PageCount,
        Length and TimeStamp are present and AuthData is only 17
        bytes. For data page 1 through 15, PageCount, Length and
        TimeStamp are not present and the size of AuthData is 23
        bytes.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        authentication_type        : Indicates the type of authentication. (type:uint8_t, values:MAV_ODID_AUTH_TYPE)
        data_page                 : Allowed range is 0 - 15. (type:uint8_t)
        last_page_index           : This field is only present for page 0. Allowed range is 0 - 15. See the description of struct ODID_Auth_data at https://github.com/opendroneid/opendroneid-core-c/blob/master/libopendroneid/opendroneid.h. (type:uint8_t)
        length                    : This field is only present for page 0. Total bytes of authentication_data from all data pages. See the description of struct ODID_Auth_data at https://github.com/opendroneid/opendroneid-core-c/blob/master/libopendroneid/opendroneid.h. [bytes] (type:uint8_t)
        timestamp                 : This field is only present for page 0. 32 bit Unix Timestamp in seconds since 00:00:00 01/01/2019. [s] (type:uint32_t)
        authentication_data        : Opaque authentication data. For page 0, the size is only 17 bytes. For other pages, the size is 23 bytes. Shall be filled with nulls in the unused portion of the field. (type:uint8_t)

        """
        return MAVLink_open_drone_id_authentication_message(target_system, target_component, id_or_mac, authentication_type, data_page, last_page_index, length, timestamp, authentication_data)

## open_drone_id_authentication_send
    def open_drone_id_authentication_send(self, target_system: int, target_component: int, id_or_mac: Sequence[int], authentication_type: int, data_page: int, last_page_index: int, length: int, timestamp: int, authentication_data: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Data for filling the OpenDroneID Authentication message. The
        Authentication Message defines a field that can provide a
        means of authenticity for the identity of the UAS (Unmanned
        Aircraft System). The Authentication message can have two
        different formats. For data page 0, the fields PageCount,
        Length and TimeStamp are present and AuthData is only 17
        bytes. For data page 1 through 15, PageCount, Length and
        TimeStamp are not present and the size of AuthData is 23
        bytes.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        authentication_type        : Indicates the type of authentication. (type:uint8_t, values:MAV_ODID_AUTH_TYPE)
        data_page                 : Allowed range is 0 - 15. (type:uint8_t)
        last_page_index           : This field is only present for page 0. Allowed range is 0 - 15. See the description of struct ODID_Auth_data at https://github.com/opendroneid/opendroneid-core-c/blob/master/libopendroneid/opendroneid.h. (type:uint8_t)
        length                    : This field is only present for page 0. Total bytes of authentication_data from all data pages. See the description of struct ODID_Auth_data at https://github.com/opendroneid/opendroneid-core-c/blob/master/libopendroneid/opendroneid.h. [bytes] (type:uint8_t)
        timestamp                 : This field is only present for page 0. 32 bit Unix Timestamp in seconds since 00:00:00 01/01/2019. [s] (type:uint32_t)
        authentication_data        : Opaque authentication data. For page 0, the size is only 17 bytes. For other pages, the size is 23 bytes. Shall be filled with nulls in the unused portion of the field. (type:uint8_t)

        """
        self.send(self.open_drone_id_authentication_encode(target_system, target_component, id_or_mac, authentication_type, data_page, last_page_index, length, timestamp, authentication_data), force_mavlink1=force_mavlink1)

## open_drone_id_self_id_encode
    def open_drone_id_self_id_encode(self, target_system: int, target_component: int, id_or_mac: Sequence[int], description_type: int, description: bytes) -> MAVLink_open_drone_id_self_id_message:
        """
        Data for filling the OpenDroneID Self ID message. The Self ID Message
        is an opportunity for the operator to (optionally) declare
        their identity and purpose of the flight. This message can
        provide additional information that could reduce the threat
        profile of a UA (Unmanned Aircraft) flying in a particular
        area or manner. This message can also be used to provide
        optional additional clarification in an emergency/remote ID
        system failure situation.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        description_type          : Indicates the type of the description field. (type:uint8_t, values:MAV_ODID_DESC_TYPE)
        description               : Text description or numeric value expressed as ASCII characters. Shall be filled with nulls in the unused portion of the field. (type:char)

        """
        return MAVLink_open_drone_id_self_id_message(target_system, target_component, id_or_mac, description_type, description)

## open_drone_id_self_id_send
    def open_drone_id_self_id_send(self, target_system: int, target_component: int, id_or_mac: Sequence[int], description_type: int, description: bytes, force_mavlink1: bool = False) -> None:
        """
        Data for filling the OpenDroneID Self ID message. The Self ID Message
        is an opportunity for the operator to (optionally) declare
        their identity and purpose of the flight. This message can
        provide additional information that could reduce the threat
        profile of a UA (Unmanned Aircraft) flying in a particular
        area or manner. This message can also be used to provide
        optional additional clarification in an emergency/remote ID
        system failure situation.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        description_type          : Indicates the type of the description field. (type:uint8_t, values:MAV_ODID_DESC_TYPE)
        description               : Text description or numeric value expressed as ASCII characters. Shall be filled with nulls in the unused portion of the field. (type:char)

        """
        self.send(self.open_drone_id_self_id_encode(target_system, target_component, id_or_mac, description_type, description), force_mavlink1=force_mavlink1)

## open_drone_id_system_encode
    def open_drone_id_system_encode(self, target_system: int, target_component: int, id_or_mac: Sequence[int], operator_location_type: int, classification_type: int, operator_latitude: int, operator_longitude: int, area_count: int, area_radius: int, area_ceiling: float, area_floor: float, category_eu: int, class_eu: int, operator_altitude_geo: float, timestamp: int) -> MAVLink_open_drone_id_system_message:
        """
        Data for filling the OpenDroneID System message. The System Message
        contains general system information including the operator
        location/altitude and possible aircraft group and/or
        category/class information.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        operator_location_type        : Specifies the operator location type. (type:uint8_t, values:MAV_ODID_OPERATOR_LOCATION_TYPE)
        classification_type        : Specifies the classification type of the UA. (type:uint8_t, values:MAV_ODID_CLASSIFICATION_TYPE)
        operator_latitude         : Latitude of the operator. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        operator_longitude        : Longitude of the operator. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        area_count                : Number of aircraft in the area, group or formation (default 1). (type:uint16_t)
        area_radius               : Radius of the cylindrical area of the group or formation (default 0). [m] (type:uint16_t)
        area_ceiling              : Area Operations Ceiling relative to WGS84. If unknown: -1000 m. [m] (type:float)
        area_floor                : Area Operations Floor relative to WGS84. If unknown: -1000 m. [m] (type:float)
        category_eu               : When classification_type is MAV_ODID_CLASSIFICATION_TYPE_EU, specifies the category of the UA. (type:uint8_t, values:MAV_ODID_CATEGORY_EU)
        class_eu                  : When classification_type is MAV_ODID_CLASSIFICATION_TYPE_EU, specifies the class of the UA. (type:uint8_t, values:MAV_ODID_CLASS_EU)
        operator_altitude_geo        : Geodetic altitude of the operator relative to WGS84. If unknown: -1000 m. [m] (type:float)
        timestamp                 : 32 bit Unix Timestamp in seconds since 00:00:00 01/01/2019. [s] (type:uint32_t)

        """
        return MAVLink_open_drone_id_system_message(target_system, target_component, id_or_mac, operator_location_type, classification_type, operator_latitude, operator_longitude, area_count, area_radius, area_ceiling, area_floor, category_eu, class_eu, operator_altitude_geo, timestamp)

## open_drone_id_system_send
    def open_drone_id_system_send(self, target_system: int, target_component: int, id_or_mac: Sequence[int], operator_location_type: int, classification_type: int, operator_latitude: int, operator_longitude: int, area_count: int, area_radius: int, area_ceiling: float, area_floor: float, category_eu: int, class_eu: int, operator_altitude_geo: float, timestamp: int, force_mavlink1: bool = False) -> None:
        """
        Data for filling the OpenDroneID System message. The System Message
        contains general system information including the operator
        location/altitude and possible aircraft group and/or
        category/class information.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        operator_location_type        : Specifies the operator location type. (type:uint8_t, values:MAV_ODID_OPERATOR_LOCATION_TYPE)
        classification_type        : Specifies the classification type of the UA. (type:uint8_t, values:MAV_ODID_CLASSIFICATION_TYPE)
        operator_latitude         : Latitude of the operator. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        operator_longitude        : Longitude of the operator. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        area_count                : Number of aircraft in the area, group or formation (default 1). (type:uint16_t)
        area_radius               : Radius of the cylindrical area of the group or formation (default 0). [m] (type:uint16_t)
        area_ceiling              : Area Operations Ceiling relative to WGS84. If unknown: -1000 m. [m] (type:float)
        area_floor                : Area Operations Floor relative to WGS84. If unknown: -1000 m. [m] (type:float)
        category_eu               : When classification_type is MAV_ODID_CLASSIFICATION_TYPE_EU, specifies the category of the UA. (type:uint8_t, values:MAV_ODID_CATEGORY_EU)
        class_eu                  : When classification_type is MAV_ODID_CLASSIFICATION_TYPE_EU, specifies the class of the UA. (type:uint8_t, values:MAV_ODID_CLASS_EU)
        operator_altitude_geo        : Geodetic altitude of the operator relative to WGS84. If unknown: -1000 m. [m] (type:float)
        timestamp                 : 32 bit Unix Timestamp in seconds since 00:00:00 01/01/2019. [s] (type:uint32_t)

        """
        self.send(self.open_drone_id_system_encode(target_system, target_component, id_or_mac, operator_location_type, classification_type, operator_latitude, operator_longitude, area_count, area_radius, area_ceiling, area_floor, category_eu, class_eu, operator_altitude_geo, timestamp), force_mavlink1=force_mavlink1)

## open_drone_id_operator_id_encode
    def open_drone_id_operator_id_encode(self, target_system: int, target_component: int, id_or_mac: Sequence[int], operator_id_type: int, operator_id: bytes) -> MAVLink_open_drone_id_operator_id_message:
        """
        Data for filling the OpenDroneID Operator ID message, which contains
        the CAA (Civil Aviation Authority) issued operator ID.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        operator_id_type          : Indicates the type of the operator_id field. (type:uint8_t, values:MAV_ODID_OPERATOR_ID_TYPE)
        operator_id               : Text description or numeric value expressed as ASCII characters. Shall be filled with nulls in the unused portion of the field. (type:char)

        """
        return MAVLink_open_drone_id_operator_id_message(target_system, target_component, id_or_mac, operator_id_type, operator_id)

## open_drone_id_operator_id_send
    def open_drone_id_operator_id_send(self, target_system: int, target_component: int, id_or_mac: Sequence[int], operator_id_type: int, operator_id: bytes, force_mavlink1: bool = False) -> None:
        """
        Data for filling the OpenDroneID Operator ID message, which contains
        the CAA (Civil Aviation Authority) issued operator ID.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        operator_id_type          : Indicates the type of the operator_id field. (type:uint8_t, values:MAV_ODID_OPERATOR_ID_TYPE)
        operator_id               : Text description or numeric value expressed as ASCII characters. Shall be filled with nulls in the unused portion of the field. (type:char)

        """
        self.send(self.open_drone_id_operator_id_encode(target_system, target_component, id_or_mac, operator_id_type, operator_id), force_mavlink1=force_mavlink1)

## open_drone_id_arm_status_encode
    def open_drone_id_arm_status_encode(self, status: int, error: bytes) -> MAVLink_open_drone_id_arm_status_message:
        """
        Status from the transmitter telling the flight controller if the
        remote ID system is ready for arming.

        status                    : Status level indicating if arming is allowed. (type:uint8_t, values:MAV_ODID_ARM_STATUS)
        error                     : Text error message, should be empty if status is good to arm. Fill with nulls in unused portion. (type:char)

        """
        return MAVLink_open_drone_id_arm_status_message(status, error)

## open_drone_id_arm_status_send
    def open_drone_id_arm_status_send(self, status: int, error: bytes, force_mavlink1: bool = False) -> None:
        """
        Status from the transmitter telling the flight controller if the
        remote ID system is ready for arming.

        status                    : Status level indicating if arming is allowed. (type:uint8_t, values:MAV_ODID_ARM_STATUS)
        error                     : Text error message, should be empty if status is good to arm. Fill with nulls in unused portion. (type:char)

        """
        self.send(self.open_drone_id_arm_status_encode(status, error), force_mavlink1=force_mavlink1)

## open_drone_id_message_pack_encode
    def open_drone_id_message_pack_encode(self, target_system: int, target_component: int, id_or_mac: Sequence[int], single_message_size: int, msg_pack_size: int, messages: Sequence[int]) -> MAVLink_open_drone_id_message_pack_message:
        """
        An OpenDroneID message pack is a container for multiple encoded
        OpenDroneID messages (i.e. not in the format given for the
        above message descriptions but after encoding into the
        compressed OpenDroneID byte format). Used e.g. when
        transmitting on Bluetooth 5.0 Long Range/Extended Advertising
        or on WiFi Neighbor Aware Networking or on WiFi Beacon.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        single_message_size        : This field must currently always be equal to 25 (bytes), since all encoded OpenDroneID messages are specified to have this length. [bytes] (type:uint8_t)
        msg_pack_size             : Number of encoded messages in the pack (not the number of bytes). Allowed range is 1 - 9. (type:uint8_t)
        messages                  : Concatenation of encoded OpenDroneID messages. Shall be filled with nulls in the unused portion of the field. (type:uint8_t)

        """
        return MAVLink_open_drone_id_message_pack_message(target_system, target_component, id_or_mac, single_message_size, msg_pack_size, messages)

## open_drone_id_message_pack_send
    def open_drone_id_message_pack_send(self, target_system: int, target_component: int, id_or_mac: Sequence[int], single_message_size: int, msg_pack_size: int, messages: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        An OpenDroneID message pack is a container for multiple encoded
        OpenDroneID messages (i.e. not in the format given for the
        above message descriptions but after encoding into the
        compressed OpenDroneID byte format). Used e.g. when
        transmitting on Bluetooth 5.0 Long Range/Extended Advertising
        or on WiFi Neighbor Aware Networking or on WiFi Beacon.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        id_or_mac                 : Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. (type:uint8_t)
        single_message_size        : This field must currently always be equal to 25 (bytes), since all encoded OpenDroneID messages are specified to have this length. [bytes] (type:uint8_t)
        msg_pack_size             : Number of encoded messages in the pack (not the number of bytes). Allowed range is 1 - 9. (type:uint8_t)
        messages                  : Concatenation of encoded OpenDroneID messages. Shall be filled with nulls in the unused portion of the field. (type:uint8_t)

        """
        self.send(self.open_drone_id_message_pack_encode(target_system, target_component, id_or_mac, single_message_size, msg_pack_size, messages), force_mavlink1=force_mavlink1)

## open_drone_id_system_update_encode
    def open_drone_id_system_update_encode(self, target_system: int, target_component: int, operator_latitude: int, operator_longitude: int, operator_altitude_geo: float, timestamp: int) -> MAVLink_open_drone_id_system_update_message:
        """
        Update the data in the OPEN_DRONE_ID_SYSTEM message with new location
        information. This can be sent to update the location
        information for the operator when no other information in the
        SYSTEM message has changed. This message allows for efficient
        operation on radio links which have limited uplink bandwidth
        while meeting requirements for update frequency of the
        operator location.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        operator_latitude         : Latitude of the operator. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        operator_longitude        : Longitude of the operator. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        operator_altitude_geo        : Geodetic altitude of the operator relative to WGS84. If unknown: -1000 m. [m] (type:float)
        timestamp                 : 32 bit Unix Timestamp in seconds since 00:00:00 01/01/2019. [s] (type:uint32_t)

        """
        return MAVLink_open_drone_id_system_update_message(target_system, target_component, operator_latitude, operator_longitude, operator_altitude_geo, timestamp)

## open_drone_id_system_update_send
    def open_drone_id_system_update_send(self, target_system: int, target_component: int, operator_latitude: int, operator_longitude: int, operator_altitude_geo: float, timestamp: int, force_mavlink1: bool = False) -> None:
        """
        Update the data in the OPEN_DRONE_ID_SYSTEM message with new location
        information. This can be sent to update the location
        information for the operator when no other information in the
        SYSTEM message has changed. This message allows for efficient
        operation on radio links which have limited uplink bandwidth
        while meeting requirements for update frequency of the
        operator location.

        target_system             : System ID (0 for broadcast). (type:uint8_t)
        target_component          : Component ID (0 for broadcast). (type:uint8_t)
        operator_latitude         : Latitude of the operator. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        operator_longitude        : Longitude of the operator. If unknown: 0 (both Lat/Lon). [degE7] (type:int32_t)
        operator_altitude_geo        : Geodetic altitude of the operator relative to WGS84. If unknown: -1000 m. [m] (type:float)
        timestamp                 : 32 bit Unix Timestamp in seconds since 00:00:00 01/01/2019. [s] (type:uint32_t)

        """
        self.send(self.open_drone_id_system_update_encode(target_system, target_component, operator_latitude, operator_longitude, operator_altitude_geo, timestamp), force_mavlink1=force_mavlink1)

## hygrometer_sensor_encode
    def hygrometer_sensor_encode(self, id: int, temperature: int, humidity: int) -> MAVLink_hygrometer_sensor_message:
        """
        Temperature and humidity from hygrometer.

        id                        : Hygrometer ID (type:uint8_t)
        temperature               : Temperature [cdegC] (type:int16_t)
        humidity                  : Humidity [c%] (type:uint16_t)

        """
        return MAVLink_hygrometer_sensor_message(id, temperature, humidity)

## hygrometer_sensor_send
    def hygrometer_sensor_send(self, id: int, temperature: int, humidity: int, force_mavlink1: bool = False) -> None:
        """
        Temperature and humidity from hygrometer.

        id                        : Hygrometer ID (type:uint8_t)
        temperature               : Temperature [cdegC] (type:int16_t)
        humidity                  : Humidity [c%] (type:uint16_t)

        """
        self.send(self.hygrometer_sensor_encode(id, temperature, humidity), force_mavlink1=force_mavlink1)

## uavionix_adsb_out_cfg_encode
    def uavionix_adsb_out_cfg_encode(self, ICAO: int, callsign: bytes, emitterType: int, aircraftSize: int, gpsOffsetLat: int, gpsOffsetLon: int, stallSpeed: int, rfSelect: int) -> MAVLink_uavionix_adsb_out_cfg_message:
        """
        Static data to configure the ADS-B transponder (send within 10 sec of
        a POR and every 10 sec thereafter)

        ICAO                      : Vehicle address (24 bit) (type:uint32_t)
        callsign                  : Vehicle identifier (8 characters, null terminated, valid characters are A-Z, 0-9, " " only) (type:char)
        emitterType               : Transmitting vehicle type. See ADSB_EMITTER_TYPE enum (type:uint8_t, values:ADSB_EMITTER_TYPE)
        aircraftSize              : Aircraft length and width encoding (table 2-35 of DO-282B) (type:uint8_t, values:UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE)
        gpsOffsetLat              : GPS antenna lateral offset (table 2-36 of DO-282B) (type:uint8_t, values:UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT)
        gpsOffsetLon              : GPS antenna longitudinal offset from nose [if non-zero, take position (in meters) divide by 2 and add one] (table 2-37 DO-282B) (type:uint8_t, values:UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON)
        stallSpeed                : Aircraft stall speed in cm/s [cm/s] (type:uint16_t)
        rfSelect                  : ADS-B transponder receiver and transmit enable flags (type:uint8_t, values:UAVIONIX_ADSB_OUT_RF_SELECT)

        """
        return MAVLink_uavionix_adsb_out_cfg_message(ICAO, callsign, emitterType, aircraftSize, gpsOffsetLat, gpsOffsetLon, stallSpeed, rfSelect)

## uavionix_adsb_out_cfg_send
    def uavionix_adsb_out_cfg_send(self, ICAO: int, callsign: bytes, emitterType: int, aircraftSize: int, gpsOffsetLat: int, gpsOffsetLon: int, stallSpeed: int, rfSelect: int, force_mavlink1: bool = False) -> None:
        """
        Static data to configure the ADS-B transponder (send within 10 sec of
        a POR and every 10 sec thereafter)

        ICAO                      : Vehicle address (24 bit) (type:uint32_t)
        callsign                  : Vehicle identifier (8 characters, null terminated, valid characters are A-Z, 0-9, " " only) (type:char)
        emitterType               : Transmitting vehicle type. See ADSB_EMITTER_TYPE enum (type:uint8_t, values:ADSB_EMITTER_TYPE)
        aircraftSize              : Aircraft length and width encoding (table 2-35 of DO-282B) (type:uint8_t, values:UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE)
        gpsOffsetLat              : GPS antenna lateral offset (table 2-36 of DO-282B) (type:uint8_t, values:UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT)
        gpsOffsetLon              : GPS antenna longitudinal offset from nose [if non-zero, take position (in meters) divide by 2 and add one] (table 2-37 DO-282B) (type:uint8_t, values:UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON)
        stallSpeed                : Aircraft stall speed in cm/s [cm/s] (type:uint16_t)
        rfSelect                  : ADS-B transponder receiver and transmit enable flags (type:uint8_t, values:UAVIONIX_ADSB_OUT_RF_SELECT)

        """
        self.send(self.uavionix_adsb_out_cfg_encode(ICAO, callsign, emitterType, aircraftSize, gpsOffsetLat, gpsOffsetLon, stallSpeed, rfSelect), force_mavlink1=force_mavlink1)

## uavionix_adsb_out_dynamic_encode
    def uavionix_adsb_out_dynamic_encode(self, utcTime: int, gpsLat: int, gpsLon: int, gpsAlt: int, gpsFix: int, numSats: int, baroAltMSL: int, accuracyHor: int, accuracyVert: int, accuracyVel: int, velVert: int, velNS: int, VelEW: int, emergencyStatus: int, state: int, squawk: int) -> MAVLink_uavionix_adsb_out_dynamic_message:
        """
        Dynamic data used to generate ADS-B out transponder data (send at 5Hz)

        utcTime                   : UTC time in seconds since GPS epoch (Jan 6, 1980). If unknown set to UINT32_MAX [s] (type:uint32_t)
        gpsLat                    : Latitude WGS84 (deg * 1E7). If unknown set to INT32_MAX [degE7] (type:int32_t)
        gpsLon                    : Longitude WGS84 (deg * 1E7). If unknown set to INT32_MAX [degE7] (type:int32_t)
        gpsAlt                    : Altitude (WGS84). UP +ve. If unknown set to INT32_MAX [mm] (type:int32_t)
        gpsFix                    : 0-1: no fix, 2: 2D fix, 3: 3D fix, 4: DGPS, 5: RTK (type:uint8_t, values:UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX)
        numSats                   : Number of satellites visible. If unknown set to UINT8_MAX (type:uint8_t)
        baroAltMSL                : Barometric pressure altitude (MSL) relative to a standard atmosphere of 1013.2 mBar and NOT bar corrected altitude (m * 1E-3). (up +ve). If unknown set to INT32_MAX [mbar] (type:int32_t)
        accuracyHor               : Horizontal accuracy in mm (m * 1E-3). If unknown set to UINT32_MAX [mm] (type:uint32_t)
        accuracyVert              : Vertical accuracy in cm. If unknown set to UINT16_MAX [cm] (type:uint16_t)
        accuracyVel               : Velocity accuracy in mm/s (m * 1E-3). If unknown set to UINT16_MAX [mm/s] (type:uint16_t)
        velVert                   : GPS vertical speed in cm/s. If unknown set to INT16_MAX [cm/s] (type:int16_t)
        velNS                     : North-South velocity over ground in cm/s North +ve. If unknown set to INT16_MAX [cm/s] (type:int16_t)
        VelEW                     : East-West velocity over ground in cm/s East +ve. If unknown set to INT16_MAX [cm/s] (type:int16_t)
        emergencyStatus           : Emergency status (type:uint8_t, values:UAVIONIX_ADSB_EMERGENCY_STATUS)
        state                     : ADS-B transponder dynamic input state flags (type:uint16_t, values:UAVIONIX_ADSB_OUT_DYNAMIC_STATE)
        squawk                    : Mode A code (typically 1200 [0x04B0] for VFR) (type:uint16_t)

        """
        return MAVLink_uavionix_adsb_out_dynamic_message(utcTime, gpsLat, gpsLon, gpsAlt, gpsFix, numSats, baroAltMSL, accuracyHor, accuracyVert, accuracyVel, velVert, velNS, VelEW, emergencyStatus, state, squawk)

## uavionix_adsb_out_dynamic_send
    def uavionix_adsb_out_dynamic_send(self, utcTime: int, gpsLat: int, gpsLon: int, gpsAlt: int, gpsFix: int, numSats: int, baroAltMSL: int, accuracyHor: int, accuracyVert: int, accuracyVel: int, velVert: int, velNS: int, VelEW: int, emergencyStatus: int, state: int, squawk: int, force_mavlink1: bool = False) -> None:
        """
        Dynamic data used to generate ADS-B out transponder data (send at 5Hz)

        utcTime                   : UTC time in seconds since GPS epoch (Jan 6, 1980). If unknown set to UINT32_MAX [s] (type:uint32_t)
        gpsLat                    : Latitude WGS84 (deg * 1E7). If unknown set to INT32_MAX [degE7] (type:int32_t)
        gpsLon                    : Longitude WGS84 (deg * 1E7). If unknown set to INT32_MAX [degE7] (type:int32_t)
        gpsAlt                    : Altitude (WGS84). UP +ve. If unknown set to INT32_MAX [mm] (type:int32_t)
        gpsFix                    : 0-1: no fix, 2: 2D fix, 3: 3D fix, 4: DGPS, 5: RTK (type:uint8_t, values:UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX)
        numSats                   : Number of satellites visible. If unknown set to UINT8_MAX (type:uint8_t)
        baroAltMSL                : Barometric pressure altitude (MSL) relative to a standard atmosphere of 1013.2 mBar and NOT bar corrected altitude (m * 1E-3). (up +ve). If unknown set to INT32_MAX [mbar] (type:int32_t)
        accuracyHor               : Horizontal accuracy in mm (m * 1E-3). If unknown set to UINT32_MAX [mm] (type:uint32_t)
        accuracyVert              : Vertical accuracy in cm. If unknown set to UINT16_MAX [cm] (type:uint16_t)
        accuracyVel               : Velocity accuracy in mm/s (m * 1E-3). If unknown set to UINT16_MAX [mm/s] (type:uint16_t)
        velVert                   : GPS vertical speed in cm/s. If unknown set to INT16_MAX [cm/s] (type:int16_t)
        velNS                     : North-South velocity over ground in cm/s North +ve. If unknown set to INT16_MAX [cm/s] (type:int16_t)
        VelEW                     : East-West velocity over ground in cm/s East +ve. If unknown set to INT16_MAX [cm/s] (type:int16_t)
        emergencyStatus           : Emergency status (type:uint8_t, values:UAVIONIX_ADSB_EMERGENCY_STATUS)
        state                     : ADS-B transponder dynamic input state flags (type:uint16_t, values:UAVIONIX_ADSB_OUT_DYNAMIC_STATE)
        squawk                    : Mode A code (typically 1200 [0x04B0] for VFR) (type:uint16_t)

        """
        self.send(self.uavionix_adsb_out_dynamic_encode(utcTime, gpsLat, gpsLon, gpsAlt, gpsFix, numSats, baroAltMSL, accuracyHor, accuracyVert, accuracyVel, velVert, velNS, VelEW, emergencyStatus, state, squawk), force_mavlink1=force_mavlink1)

## uavionix_adsb_transceiver_health_report_encode
    def uavionix_adsb_transceiver_health_report_encode(self, rfHealth: int) -> MAVLink_uavionix_adsb_transceiver_health_report_message:
        """
        Transceiver heartbeat with health report (updated every 10s)

        rfHealth                  : ADS-B transponder messages (type:uint8_t, values:UAVIONIX_ADSB_RF_HEALTH)

        """
        return MAVLink_uavionix_adsb_transceiver_health_report_message(rfHealth)

## uavionix_adsb_transceiver_health_report_send
    def uavionix_adsb_transceiver_health_report_send(self, rfHealth: int, force_mavlink1: bool = False) -> None:
        """
        Transceiver heartbeat with health report (updated every 10s)

        rfHealth                  : ADS-B transponder messages (type:uint8_t, values:UAVIONIX_ADSB_RF_HEALTH)

        """
        self.send(self.uavionix_adsb_transceiver_health_report_encode(rfHealth), force_mavlink1=force_mavlink1)

## uavionix_adsb_out_cfg_registration_encode
    def uavionix_adsb_out_cfg_registration_encode(self, registration: bytes) -> MAVLink_uavionix_adsb_out_cfg_registration_message:
        """
        Aircraft Registration.

        registration              : Aircraft Registration (ASCII string A-Z, 0-9 only), e.g. "N8644B ". Trailing spaces (0x20) only. This is null-terminated. (type:char)

        """
        return MAVLink_uavionix_adsb_out_cfg_registration_message(registration)

## uavionix_adsb_out_cfg_registration_send
    def uavionix_adsb_out_cfg_registration_send(self, registration: bytes, force_mavlink1: bool = False) -> None:
        """
        Aircraft Registration.

        registration              : Aircraft Registration (ASCII string A-Z, 0-9 only), e.g. "N8644B ". Trailing spaces (0x20) only. This is null-terminated. (type:char)

        """
        self.send(self.uavionix_adsb_out_cfg_registration_encode(registration), force_mavlink1=force_mavlink1)

## uavionix_adsb_out_cfg_flightid_encode
    def uavionix_adsb_out_cfg_flightid_encode(self, flight_id: bytes) -> MAVLink_uavionix_adsb_out_cfg_flightid_message:
        """
        Flight Identification for ADSB-Out vehicles.

        flight_id                 : Flight Identification: 8 ASCII characters, '0' through '9', 'A' through 'Z' or space. Spaces (0x20) used as a trailing pad character, or when call sign is unavailable. Reflects Control message setting. This is null-terminated. (type:char)

        """
        return MAVLink_uavionix_adsb_out_cfg_flightid_message(flight_id)

## uavionix_adsb_out_cfg_flightid_send
    def uavionix_adsb_out_cfg_flightid_send(self, flight_id: bytes, force_mavlink1: bool = False) -> None:
        """
        Flight Identification for ADSB-Out vehicles.

        flight_id                 : Flight Identification: 8 ASCII characters, '0' through '9', 'A' through 'Z' or space. Spaces (0x20) used as a trailing pad character, or when call sign is unavailable. Reflects Control message setting. This is null-terminated. (type:char)

        """
        self.send(self.uavionix_adsb_out_cfg_flightid_encode(flight_id), force_mavlink1=force_mavlink1)

## uavionix_adsb_get_encode
    def uavionix_adsb_get_encode(self, ReqMessageId: int) -> MAVLink_uavionix_adsb_get_message:
        """
        Request messages.

        ReqMessageId              : Message ID to request. Supports any message in this 10000-10099 range (type:uint32_t)

        """
        return MAVLink_uavionix_adsb_get_message(ReqMessageId)

## uavionix_adsb_get_send
    def uavionix_adsb_get_send(self, ReqMessageId: int, force_mavlink1: bool = False) -> None:
        """
        Request messages.

        ReqMessageId              : Message ID to request. Supports any message in this 10000-10099 range (type:uint32_t)

        """
        self.send(self.uavionix_adsb_get_encode(ReqMessageId), force_mavlink1=force_mavlink1)

## uavionix_adsb_out_control_encode
    def uavionix_adsb_out_control_encode(self, state: int, baroAltMSL: int, squawk: int, emergencyStatus: int, flight_id: bytes, x_bit: int) -> MAVLink_uavionix_adsb_out_control_message:
        """
        Control message with all data sent in UCP control message.

        state                     : ADS-B transponder control state flags (type:uint8_t, values:UAVIONIX_ADSB_OUT_CONTROL_STATE)
        baroAltMSL                : Barometric pressure altitude (MSL) relative to a standard atmosphere of 1013.2 mBar and NOT bar corrected altitude (m * 1E-3). (up +ve). If unknown set to INT32_MAX [mbar] (type:int32_t)
        squawk                    : Mode A code (typically 1200 [0x04B0] for VFR) (type:uint16_t)
        emergencyStatus           : Emergency status (type:uint8_t, values:UAVIONIX_ADSB_EMERGENCY_STATUS)
        flight_id                 : Flight Identification: 8 ASCII characters, '0' through '9', 'A' through 'Z' or space. Spaces (0x20) used as a trailing pad character, or when call sign is unavailable. (type:char)
        x_bit                     : X-Bit enable (military transponders only) (type:uint8_t, values:UAVIONIX_ADSB_XBIT)

        """
        return MAVLink_uavionix_adsb_out_control_message(state, baroAltMSL, squawk, emergencyStatus, flight_id, x_bit)

## uavionix_adsb_out_control_send
    def uavionix_adsb_out_control_send(self, state: int, baroAltMSL: int, squawk: int, emergencyStatus: int, flight_id: bytes, x_bit: int, force_mavlink1: bool = False) -> None:
        """
        Control message with all data sent in UCP control message.

        state                     : ADS-B transponder control state flags (type:uint8_t, values:UAVIONIX_ADSB_OUT_CONTROL_STATE)
        baroAltMSL                : Barometric pressure altitude (MSL) relative to a standard atmosphere of 1013.2 mBar and NOT bar corrected altitude (m * 1E-3). (up +ve). If unknown set to INT32_MAX [mbar] (type:int32_t)
        squawk                    : Mode A code (typically 1200 [0x04B0] for VFR) (type:uint16_t)
        emergencyStatus           : Emergency status (type:uint8_t, values:UAVIONIX_ADSB_EMERGENCY_STATUS)
        flight_id                 : Flight Identification: 8 ASCII characters, '0' through '9', 'A' through 'Z' or space. Spaces (0x20) used as a trailing pad character, or when call sign is unavailable. (type:char)
        x_bit                     : X-Bit enable (military transponders only) (type:uint8_t, values:UAVIONIX_ADSB_XBIT)

        """
        self.send(self.uavionix_adsb_out_control_encode(state, baroAltMSL, squawk, emergencyStatus, flight_id, x_bit), force_mavlink1=force_mavlink1)

## uavionix_adsb_out_status_encode
    def uavionix_adsb_out_status_encode(self, state: int, squawk: int, NIC_NACp: int, boardTemp: int, fault: int, flight_id: bytes) -> MAVLink_uavionix_adsb_out_status_message:
        """
        Status message with information from UCP Heartbeat and Status
        messages.

        state                     : ADS-B transponder status state flags (type:uint8_t, values:UAVIONIX_ADSB_OUT_STATUS_STATE)
        squawk                    : Mode A code (typically 1200 [0x04B0] for VFR) (type:uint16_t)
        NIC_NACp                  : Integrity and Accuracy of traffic reported as a 4-bit value for each field (NACp 7:4, NIC 3:0) and encoded by Containment Radius (HPL) and Estimated Position Uncertainty (HFOM), respectively (type:uint8_t, values:UAVIONIX_ADSB_OUT_STATUS_NIC_NACP)
        boardTemp                 : Board temperature in C (type:uint8_t)
        fault                     : ADS-B transponder fault flags (type:uint8_t, values:UAVIONIX_ADSB_OUT_STATUS_FAULT)
        flight_id                 : Flight Identification: 8 ASCII characters, '0' through '9', 'A' through 'Z' or space. Spaces (0x20) used as a trailing pad character, or when call sign is unavailable. (type:char)

        """
        return MAVLink_uavionix_adsb_out_status_message(state, squawk, NIC_NACp, boardTemp, fault, flight_id)

## uavionix_adsb_out_status_send
    def uavionix_adsb_out_status_send(self, state: int, squawk: int, NIC_NACp: int, boardTemp: int, fault: int, flight_id: bytes, force_mavlink1: bool = False) -> None:
        """
        Status message with information from UCP Heartbeat and Status
        messages.

        state                     : ADS-B transponder status state flags (type:uint8_t, values:UAVIONIX_ADSB_OUT_STATUS_STATE)
        squawk                    : Mode A code (typically 1200 [0x04B0] for VFR) (type:uint16_t)
        NIC_NACp                  : Integrity and Accuracy of traffic reported as a 4-bit value for each field (NACp 7:4, NIC 3:0) and encoded by Containment Radius (HPL) and Estimated Position Uncertainty (HFOM), respectively (type:uint8_t, values:UAVIONIX_ADSB_OUT_STATUS_NIC_NACP)
        boardTemp                 : Board temperature in C (type:uint8_t)
        fault                     : ADS-B transponder fault flags (type:uint8_t, values:UAVIONIX_ADSB_OUT_STATUS_FAULT)
        flight_id                 : Flight Identification: 8 ASCII characters, '0' through '9', 'A' through 'Z' or space. Spaces (0x20) used as a trailing pad character, or when call sign is unavailable. (type:char)

        """
        self.send(self.uavionix_adsb_out_status_encode(state, squawk, NIC_NACp, boardTemp, fault, flight_id), force_mavlink1=force_mavlink1)

## icarous_heartbeat_encode
    def icarous_heartbeat_encode(self, status: int) -> MAVLink_icarous_heartbeat_message:
        """
        ICAROUS heartbeat

        status                    : See the FMS_STATE enum. (type:uint8_t, values:ICAROUS_FMS_STATE)

        """
        return MAVLink_icarous_heartbeat_message(status)

## icarous_heartbeat_send
    def icarous_heartbeat_send(self, status: int, force_mavlink1: bool = False) -> None:
        """
        ICAROUS heartbeat

        status                    : See the FMS_STATE enum. (type:uint8_t, values:ICAROUS_FMS_STATE)

        """
        self.send(self.icarous_heartbeat_encode(status), force_mavlink1=force_mavlink1)

## icarous_kinematic_bands_encode
    def icarous_kinematic_bands_encode(self, numBands: int, type1: int, min1: float, max1: float, type2: int, min2: float, max2: float, type3: int, min3: float, max3: float, type4: int, min4: float, max4: float, type5: int, min5: float, max5: float) -> MAVLink_icarous_kinematic_bands_message:
        """
        Kinematic multi bands (track) output from Daidalus

        numBands                  : Number of track bands (type:int8_t)
        type1                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min1                      : min angle (degrees) [deg] (type:float)
        max1                      : max angle (degrees) [deg] (type:float)
        type2                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min2                      : min angle (degrees) [deg] (type:float)
        max2                      : max angle (degrees) [deg] (type:float)
        type3                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min3                      : min angle (degrees) [deg] (type:float)
        max3                      : max angle (degrees) [deg] (type:float)
        type4                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min4                      : min angle (degrees) [deg] (type:float)
        max4                      : max angle (degrees) [deg] (type:float)
        type5                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min5                      : min angle (degrees) [deg] (type:float)
        max5                      : max angle (degrees) [deg] (type:float)

        """
        return MAVLink_icarous_kinematic_bands_message(numBands, type1, min1, max1, type2, min2, max2, type3, min3, max3, type4, min4, max4, type5, min5, max5)

## icarous_kinematic_bands_send
    def icarous_kinematic_bands_send(self, numBands: int, type1: int, min1: float, max1: float, type2: int, min2: float, max2: float, type3: int, min3: float, max3: float, type4: int, min4: float, max4: float, type5: int, min5: float, max5: float, force_mavlink1: bool = False) -> None:
        """
        Kinematic multi bands (track) output from Daidalus

        numBands                  : Number of track bands (type:int8_t)
        type1                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min1                      : min angle (degrees) [deg] (type:float)
        max1                      : max angle (degrees) [deg] (type:float)
        type2                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min2                      : min angle (degrees) [deg] (type:float)
        max2                      : max angle (degrees) [deg] (type:float)
        type3                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min3                      : min angle (degrees) [deg] (type:float)
        max3                      : max angle (degrees) [deg] (type:float)
        type4                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min4                      : min angle (degrees) [deg] (type:float)
        max4                      : max angle (degrees) [deg] (type:float)
        type5                     : See the TRACK_BAND_TYPES enum. (type:uint8_t, values:ICAROUS_TRACK_BAND_TYPES)
        min5                      : min angle (degrees) [deg] (type:float)
        max5                      : max angle (degrees) [deg] (type:float)

        """
        self.send(self.icarous_kinematic_bands_encode(numBands, type1, min1, max1, type2, min2, max2, type3, min3, max3, type4, min4, max4, type5, min5, max5), force_mavlink1=force_mavlink1)

## loweheiser_gov_efi_encode
    def loweheiser_gov_efi_encode(self, volt_batt: float, curr_batt: float, curr_gen: float, curr_rot: float, fuel_level: float, throttle: float, runtime: int, until_maintenance: int, rectifier_temp: float, generator_temp: float, efi_batt: float, efi_rpm: float, efi_pw: float, efi_fuel_flow: float, efi_fuel_consumed: float, efi_baro: float, efi_mat: float, efi_clt: float, efi_tps: float, efi_exhaust_gas_temperature: float, efi_index: int, generator_status: int, efi_status: int) -> MAVLink_loweheiser_gov_efi_message:
        """
        Composite EFI and Governor data from Loweheiser equipment.  This
        message is created by the EFI unit based on its own data and
        data received from a governor attached to that EFI unit.

        volt_batt                 : Generator Battery voltage. [V] (type:float)
        curr_batt                 : Generator Battery current. [A] (type:float)
        curr_gen                  : Current being produced by generator. [A] (type:float)
        curr_rot                  : Load current being consumed by the UAV (sum of curr_gen and curr_batt) [A] (type:float)
        fuel_level                : Generator fuel remaining in litres. [l] (type:float)
        throttle                  : Throttle Output. [%] (type:float)
        runtime                   : Seconds this generator has run since it was rebooted. [s] (type:uint32_t)
        until_maintenance         : Seconds until this generator requires maintenance.  A negative value indicates maintenance is past due. [s] (type:int32_t)
        rectifier_temp            : The Temperature of the rectifier. [degC] (type:float)
        generator_temp            : The temperature of the mechanical motor, fuel cell core or generator. [degC] (type:float)
        efi_batt                  : EFI Supply Voltage. [V] (type:float)
        efi_rpm                   : Motor RPM. [rpm] (type:float)
        efi_pw                    : Injector pulse-width in milliseconds. [ms] (type:float)
        efi_fuel_flow             : Fuel flow rate in litres/hour. (type:float)
        efi_fuel_consumed         : Fuel consumed. [l] (type:float)
        efi_baro                  : Atmospheric pressure. [kPa] (type:float)
        efi_mat                   : Manifold Air Temperature. [degC] (type:float)
        efi_clt                   : Cylinder Head Temperature. [degC] (type:float)
        efi_tps                   : Throttle Position. [%] (type:float)
        efi_exhaust_gas_temperature        : Exhaust gas temperature. [degC] (type:float)
        efi_index                 : EFI index. (type:uint8_t)
        generator_status          : Generator status. (type:uint16_t)
        efi_status                : EFI status. (type:uint16_t)

        """
        return MAVLink_loweheiser_gov_efi_message(volt_batt, curr_batt, curr_gen, curr_rot, fuel_level, throttle, runtime, until_maintenance, rectifier_temp, generator_temp, efi_batt, efi_rpm, efi_pw, efi_fuel_flow, efi_fuel_consumed, efi_baro, efi_mat, efi_clt, efi_tps, efi_exhaust_gas_temperature, efi_index, generator_status, efi_status)

## loweheiser_gov_efi_send
    def loweheiser_gov_efi_send(self, volt_batt: float, curr_batt: float, curr_gen: float, curr_rot: float, fuel_level: float, throttle: float, runtime: int, until_maintenance: int, rectifier_temp: float, generator_temp: float, efi_batt: float, efi_rpm: float, efi_pw: float, efi_fuel_flow: float, efi_fuel_consumed: float, efi_baro: float, efi_mat: float, efi_clt: float, efi_tps: float, efi_exhaust_gas_temperature: float, efi_index: int, generator_status: int, efi_status: int, force_mavlink1: bool = False) -> None:
        """
        Composite EFI and Governor data from Loweheiser equipment.  This
        message is created by the EFI unit based on its own data and
        data received from a governor attached to that EFI unit.

        volt_batt                 : Generator Battery voltage. [V] (type:float)
        curr_batt                 : Generator Battery current. [A] (type:float)
        curr_gen                  : Current being produced by generator. [A] (type:float)
        curr_rot                  : Load current being consumed by the UAV (sum of curr_gen and curr_batt) [A] (type:float)
        fuel_level                : Generator fuel remaining in litres. [l] (type:float)
        throttle                  : Throttle Output. [%] (type:float)
        runtime                   : Seconds this generator has run since it was rebooted. [s] (type:uint32_t)
        until_maintenance         : Seconds until this generator requires maintenance.  A negative value indicates maintenance is past due. [s] (type:int32_t)
        rectifier_temp            : The Temperature of the rectifier. [degC] (type:float)
        generator_temp            : The temperature of the mechanical motor, fuel cell core or generator. [degC] (type:float)
        efi_batt                  : EFI Supply Voltage. [V] (type:float)
        efi_rpm                   : Motor RPM. [rpm] (type:float)
        efi_pw                    : Injector pulse-width in milliseconds. [ms] (type:float)
        efi_fuel_flow             : Fuel flow rate in litres/hour. (type:float)
        efi_fuel_consumed         : Fuel consumed. [l] (type:float)
        efi_baro                  : Atmospheric pressure. [kPa] (type:float)
        efi_mat                   : Manifold Air Temperature. [degC] (type:float)
        efi_clt                   : Cylinder Head Temperature. [degC] (type:float)
        efi_tps                   : Throttle Position. [%] (type:float)
        efi_exhaust_gas_temperature        : Exhaust gas temperature. [degC] (type:float)
        efi_index                 : EFI index. (type:uint8_t)
        generator_status          : Generator status. (type:uint16_t)
        efi_status                : EFI status. (type:uint16_t)

        """
        self.send(self.loweheiser_gov_efi_encode(volt_batt, curr_batt, curr_gen, curr_rot, fuel_level, throttle, runtime, until_maintenance, rectifier_temp, generator_temp, efi_batt, efi_rpm, efi_pw, efi_fuel_flow, efi_fuel_consumed, efi_baro, efi_mat, efi_clt, efi_tps, efi_exhaust_gas_temperature, efi_index, generator_status, efi_status), force_mavlink1=force_mavlink1)

## cubepilot_raw_rc_encode
    def cubepilot_raw_rc_encode(self, rc_raw: Sequence[int]) -> MAVLink_cubepilot_raw_rc_message:
        """
        Raw RC Data

        rc_raw                    :  (type:uint8_t)

        """
        return MAVLink_cubepilot_raw_rc_message(rc_raw)

## cubepilot_raw_rc_send
    def cubepilot_raw_rc_send(self, rc_raw: Sequence[int], force_mavlink1: bool = False) -> None:
        """
        Raw RC Data

        rc_raw                    :  (type:uint8_t)

        """
        self.send(self.cubepilot_raw_rc_encode(rc_raw), force_mavlink1=force_mavlink1)

## herelink_video_stream_information_encode
    def herelink_video_stream_information_encode(self, camera_id: int, status: int, framerate: float, resolution_h: int, resolution_v: int, bitrate: int, rotation: int, uri: bytes) -> MAVLink_herelink_video_stream_information_message:
        """
        Information about video stream

        camera_id                 : Video Stream ID (1 for first, 2 for second, etc.) (type:uint8_t)
        status                    : Number of streams available. (type:uint8_t)
        framerate                 : Frame rate. [Hz] (type:float)
        resolution_h              : Horizontal resolution. [pix] (type:uint16_t)
        resolution_v              : Vertical resolution. [pix] (type:uint16_t)
        bitrate                   : Bit rate. [bits/s] (type:uint32_t)
        rotation                  : Video image rotation clockwise. [deg] (type:uint16_t)
        uri                       : Video stream URI (TCP or RTSP URI ground station should connect to) or port number (UDP port ground station should listen to). (type:char)

        """
        return MAVLink_herelink_video_stream_information_message(camera_id, status, framerate, resolution_h, resolution_v, bitrate, rotation, uri)

## herelink_video_stream_information_send
    def herelink_video_stream_information_send(self, camera_id: int, status: int, framerate: float, resolution_h: int, resolution_v: int, bitrate: int, rotation: int, uri: bytes, force_mavlink1: bool = False) -> None:
        """
        Information about video stream

        camera_id                 : Video Stream ID (1 for first, 2 for second, etc.) (type:uint8_t)
        status                    : Number of streams available. (type:uint8_t)
        framerate                 : Frame rate. [Hz] (type:float)
        resolution_h              : Horizontal resolution. [pix] (type:uint16_t)
        resolution_v              : Vertical resolution. [pix] (type:uint16_t)
        bitrate                   : Bit rate. [bits/s] (type:uint32_t)
        rotation                  : Video image rotation clockwise. [deg] (type:uint16_t)
        uri                       : Video stream URI (TCP or RTSP URI ground station should connect to) or port number (UDP port ground station should listen to). (type:char)

        """
        self.send(self.herelink_video_stream_information_encode(camera_id, status, framerate, resolution_h, resolution_v, bitrate, rotation, uri), force_mavlink1=force_mavlink1)

## herelink_telem_encode
    def herelink_telem_encode(self, rssi: int, snr: int, rf_freq: int, link_bw: int, link_rate: int, cpu_temp: int, board_temp: int) -> MAVLink_herelink_telem_message:
        """
        Herelink Telemetry

        rssi                      :  (type:uint8_t)
        snr                       :  (type:int16_t)
        rf_freq                   :  (type:uint32_t)
        link_bw                   :  (type:uint32_t)
        link_rate                 :  (type:uint32_t)
        cpu_temp                  :  (type:int16_t)
        board_temp                :  (type:int16_t)

        """
        return MAVLink_herelink_telem_message(rssi, snr, rf_freq, link_bw, link_rate, cpu_temp, board_temp)

## herelink_telem_send
    def herelink_telem_send(self, rssi: int, snr: int, rf_freq: int, link_bw: int, link_rate: int, cpu_temp: int, board_temp: int, force_mavlink1: bool = False) -> None:
        """
        Herelink Telemetry

        rssi                      :  (type:uint8_t)
        snr                       :  (type:int16_t)
        rf_freq                   :  (type:uint32_t)
        link_bw                   :  (type:uint32_t)
        link_rate                 :  (type:uint32_t)
        cpu_temp                  :  (type:int16_t)
        board_temp                :  (type:int16_t)

        """
        self.send(self.herelink_telem_encode(rssi, snr, rf_freq, link_bw, link_rate, cpu_temp, board_temp), force_mavlink1=force_mavlink1)

## cubepilot_firmware_update_start_encode
    def cubepilot_firmware_update_start_encode(self, target_system: int, target_component: int, size: int, crc: int) -> MAVLink_cubepilot_firmware_update_start_message:
        """
        Start firmware update with encapsulated data.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        size                      : FW Size. [bytes] (type:uint32_t)
        crc                       : FW CRC. (type:uint32_t)

        """
        return MAVLink_cubepilot_firmware_update_start_message(target_system, target_component, size, crc)

## cubepilot_firmware_update_start_send
    def cubepilot_firmware_update_start_send(self, target_system: int, target_component: int, size: int, crc: int, force_mavlink1: bool = False) -> None:
        """
        Start firmware update with encapsulated data.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        size                      : FW Size. [bytes] (type:uint32_t)
        crc                       : FW CRC. (type:uint32_t)

        """
        self.send(self.cubepilot_firmware_update_start_encode(target_system, target_component, size, crc), force_mavlink1=force_mavlink1)

## cubepilot_firmware_update_resp_encode
    def cubepilot_firmware_update_resp_encode(self, target_system: int, target_component: int, offset: int) -> MAVLink_cubepilot_firmware_update_resp_message:
        """
        offset response to encapsulated data.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        offset                    : FW Offset. [bytes] (type:uint32_t)

        """
        return MAVLink_cubepilot_firmware_update_resp_message(target_system, target_component, offset)

## cubepilot_firmware_update_resp_send
    def cubepilot_firmware_update_resp_send(self, target_system: int, target_component: int, offset: int, force_mavlink1: bool = False) -> None:
        """
        offset response to encapsulated data.

        target_system             : System ID. (type:uint8_t)
        target_component          : Component ID. (type:uint8_t)
        offset                    : FW Offset. [bytes] (type:uint32_t)

        """
        self.send(self.cubepilot_firmware_update_resp_encode(target_system, target_component, offset), force_mavlink1=force_mavlink1)

## airlink_auth_encode
    def airlink_auth_encode(self, login: bytes, password: bytes) -> MAVLink_airlink_auth_message:
        """
        Authorization package

        login                     : Login (type:char)
        password                  : Password (type:char)

        """
        return MAVLink_airlink_auth_message(login, password)

## airlink_auth_send
    def airlink_auth_send(self, login: bytes, password: bytes, force_mavlink1: bool = False) -> None:
        """
        Authorization package

        login                     : Login (type:char)
        password                  : Password (type:char)

        """
        self.send(self.airlink_auth_encode(login, password), force_mavlink1=force_mavlink1)

## airlink_auth_response_encode
    def airlink_auth_response_encode(self, resp_type: int) -> MAVLink_airlink_auth_response_message:
        """
        Response to the authorization request

        resp_type                 : Response type (type:uint8_t, values:AIRLINK_AUTH_RESPONSE_TYPE)

        """
        return MAVLink_airlink_auth_response_message(resp_type)

## airlink_auth_response_send
    def airlink_auth_response_send(self, resp_type: int, force_mavlink1: bool = False) -> None:
        """
        Response to the authorization request

        resp_type                 : Response type (type:uint8_t, values:AIRLINK_AUTH_RESPONSE_TYPE)

        """
        self.send(self.airlink_auth_response_encode(resp_type), force_mavlink1=force_mavlink1)

## heartbeat_encode
    def heartbeat_encode(self, type: int, autopilot: int, base_mode: int, custom_mode: int, system_status: int, mavlink_version: int = 3) -> MAVLink_heartbeat_message:
        """
        The heartbeat message shows that a system or component is present and
        responding. The type and autopilot fields (along with the
        message component id), allow the receiving system to treat
        further messages from this system appropriately (e.g. by
        laying out the user interface based on the autopilot). This
        microservice is documented at
        https://mavlink.io/en/services/heartbeat.html

        type                      : Vehicle or component type. For a flight controller component the vehicle type (quadrotor, helicopter, etc.). For other components the component type (e.g. camera, gimbal, etc.). This should be used in preference to component id for identifying the component type. (type:uint8_t, values:MAV_TYPE)
        autopilot                 : Autopilot type / class. Use MAV_AUTOPILOT_INVALID for components that are not flight controllers. (type:uint8_t, values:MAV_AUTOPILOT)
        base_mode                 : System mode bitmap. (type:uint8_t, values:MAV_MODE_FLAG)
        custom_mode               : A bitfield for use for autopilot-specific flags (type:uint32_t)
        system_status             : System status flag. (type:uint8_t, values:MAV_STATE)
        mavlink_version           : MAVLink version, not writable by user, gets added by protocol because of magic data type: uint8_t_mavlink_version (type:uint8_t)

        """
        return MAVLink_heartbeat_message(type, autopilot, base_mode, custom_mode, system_status, mavlink_version)

## heartbeat_send
    def heartbeat_send(self, type: int, autopilot: int, base_mode: int, custom_mode: int, system_status: int, mavlink_version: int = 3, force_mavlink1: bool = False) -> None:
        """
        The heartbeat message shows that a system or component is present and
        responding. The type and autopilot fields (along with the
        message component id), allow the receiving system to treat
        further messages from this system appropriately (e.g. by
        laying out the user interface based on the autopilot). This
        microservice is documented at
        https://mavlink.io/en/services/heartbeat.html

        type                      : Vehicle or component type. For a flight controller component the vehicle type (quadrotor, helicopter, etc.). For other components the component type (e.g. camera, gimbal, etc.). This should be used in preference to component id for identifying the component type. (type:uint8_t, values:MAV_TYPE)
        autopilot                 : Autopilot type / class. Use MAV_AUTOPILOT_INVALID for components that are not flight controllers. (type:uint8_t, values:MAV_AUTOPILOT)
        base_mode                 : System mode bitmap. (type:uint8_t, values:MAV_MODE_FLAG)
        custom_mode               : A bitfield for use for autopilot-specific flags (type:uint32_t)
        system_status             : System status flag. (type:uint8_t, values:MAV_STATE)
        mavlink_version           : MAVLink version, not writable by user, gets added by protocol because of magic data type: uint8_t_mavlink_version (type:uint8_t)

        """
        self.send(self.heartbeat_encode(type, autopilot, base_mode, custom_mode, system_status, mavlink_version), force_mavlink1=force_mavlink1)

## __dict__
Attribute type: mappingproxy

## __weakref__
Attribute type: getset_descriptor

## __new__
Attribute type: builtin_function_or_method

## __repr__
Attribute type: wrapper_descriptor

## __hash__
Attribute type: wrapper_descriptor

## __str__
Attribute type: wrapper_descriptor

## __getattribute__
Attribute type: wrapper_descriptor

## __setattr__
Attribute type: wrapper_descriptor

## __delattr__
Attribute type: wrapper_descriptor

## __lt__
Attribute type: wrapper_descriptor

## __le__
Attribute type: wrapper_descriptor

## __eq__
Attribute type: wrapper_descriptor

## __ne__
Attribute type: wrapper_descriptor

## __gt__
Attribute type: wrapper_descriptor

## __ge__
Attribute type: wrapper_descriptor

## __reduce_ex__
Attribute type: method_descriptor

## __reduce__
Attribute type: method_descriptor

## __getstate__
Attribute type: method_descriptor

## __subclasshook__
Attribute type: builtin_function_or_method

## __init_subclass__
Attribute type: builtin_function_or_method

## __format__
Attribute type: method_descriptor

## __sizeof__
Attribute type: method_descriptor

## __dir__
Attribute type: method_descriptor

## __class__
Attribute type: type
