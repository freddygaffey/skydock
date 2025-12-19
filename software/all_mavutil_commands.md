## seq
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

## file
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

## srcSystem
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

## srcComponent
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

## callback
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

## callback_args
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

## callback_kwargs
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

## send_callback
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

## send_callback_args
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

## send_callback_kwargs
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

## buf
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

## buf_index
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

## expected_length
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

## have_prefix_error
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

## robust_parsing
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

## protocol_marker
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

## little_endian
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

## crc_extra
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

## sort_fields
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

## total_packets_sent
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

## total_bytes_sent
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

## total_packets_received
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

## total_bytes_received
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

## total_receive_errors
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

## startup_time
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

## signing
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

## mav20_unpacker
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

## mav10_unpacker
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

## mav20_h3_unpacker
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

## mav_csum_unpacker
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

## mav_sign_unpacker
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

## __module__
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

## __doc__
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

## __init__
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

## set_callback
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

## set_send_callback
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

## send
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

## buf_len
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

## bytes_needed
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

## _MAVLink__callbacks
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

## parse_char
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

## _MAVLink__parse_char_legacy
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

## parse_buffer
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

## check_signature
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

## decode
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

## sensor_offsets_encode
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

## sensor_offsets_send
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

## set_mag_offsets_encode
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

## set_mag_offsets_send
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

## meminfo_encode
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

## meminfo_send
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

## ap_adc_encode
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

## ap_adc_send
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

## digicam_configure_encode
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

## digicam_configure_send
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

## digicam_control_encode
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

## digicam_control_send
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

## mount_configure_encode
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

## mount_configure_send
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

## mount_control_encode
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

## mount_control_send
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

## mount_status_encode
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

## mount_status_send
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

## fence_point_encode
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

## fence_point_send
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

## fence_fetch_point_encode
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

## fence_fetch_point_send
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

## ahrs_encode
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

## ahrs_send
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

## simstate_encode
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

## simstate_send
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

## hwstatus_encode
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

## hwstatus_send
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

## radio_encode
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

## radio_send
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

## limits_status_encode
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

## limits_status_send
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

## wind_encode
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

## wind_send
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

## data16_encode
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

## data16_send
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

## data32_encode
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

## data32_send
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

## data64_encode
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

## data64_send
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

## data96_encode
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

## data96_send
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

## rangefinder_encode
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

## rangefinder_send
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

## airspeed_autocal_encode
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

## airspeed_autocal_send
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

## rally_point_encode
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

## rally_point_send
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

## rally_fetch_point_encode
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

## rally_fetch_point_send
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

## compassmot_status_encode
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

## compassmot_status_send
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

## ahrs2_encode
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

## ahrs2_send
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

## camera_status_encode
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

## camera_status_send
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

## camera_feedback_encode
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

## camera_feedback_send
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

## battery2_encode
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

## battery2_send
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

## ahrs3_encode
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

## ahrs3_send
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

## autopilot_version_request_encode
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

## autopilot_version_request_send
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

## remote_log_data_block_encode
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

## remote_log_data_block_send
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

## remote_log_block_status_encode
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

## remote_log_block_status_send
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

## led_control_encode
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

## led_control_send
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

## mag_cal_progress_encode
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

## mag_cal_progress_send
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

## ekf_status_report_encode
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

## ekf_status_report_send
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

## pid_tuning_encode
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

## pid_tuning_send
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

## deepstall_encode
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

## deepstall_send
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

## gimbal_report_encode
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

## gimbal_report_send
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

## gimbal_control_encode
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

## gimbal_control_send
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

## gimbal_torque_cmd_report_encode
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

## gimbal_torque_cmd_report_send
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

## gopro_heartbeat_encode
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

## gopro_heartbeat_send
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

## gopro_get_request_encode
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

## gopro_get_request_send
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

## gopro_get_response_encode
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

## gopro_get_response_send
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

## gopro_set_request_encode
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

## gopro_set_request_send
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

## gopro_set_response_encode
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

## gopro_set_response_send
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

## rpm_encode
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

## rpm_send
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

## device_op_read_encode
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

## device_op_read_send
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

## device_op_read_reply_encode
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

## device_op_read_reply_send
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

## device_op_write_encode
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

## device_op_write_send
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

## device_op_write_reply_encode
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

## device_op_write_reply_send
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

## secure_command_encode
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

## secure_command_send
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

## secure_command_reply_encode
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

## secure_command_reply_send
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

## adap_tuning_encode
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

## adap_tuning_send
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

## vision_position_delta_encode
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

## vision_position_delta_send
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

## aoa_ssa_encode
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

## aoa_ssa_send
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

## esc_telemetry_1_to_4_encode
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

## esc_telemetry_1_to_4_send
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

## esc_telemetry_5_to_8_encode
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

## esc_telemetry_5_to_8_send
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

## esc_telemetry_9_to_12_encode
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

## esc_telemetry_9_to_12_send
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

## osd_param_config_encode
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

## osd_param_config_send
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

## osd_param_config_reply_encode
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

## osd_param_config_reply_send
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

## osd_param_show_config_encode
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

## osd_param_show_config_send
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

## osd_param_show_config_reply_encode
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

## osd_param_show_config_reply_send
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

## obstacle_distance_3d_encode
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

## obstacle_distance_3d_send
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

## water_depth_encode
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

## water_depth_send
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

## mcu_status_encode
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

## mcu_status_send
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

## esc_telemetry_13_to_16_encode
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

## esc_telemetry_13_to_16_send
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

## esc_telemetry_17_to_20_encode
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

## esc_telemetry_17_to_20_send
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

## esc_telemetry_21_to_24_encode
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

## esc_telemetry_21_to_24_send
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

## esc_telemetry_25_to_28_encode
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

## esc_telemetry_25_to_28_send
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

## esc_telemetry_29_to_32_encode
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

## esc_telemetry_29_to_32_send
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

## sys_status_encode
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

## sys_status_send
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

## system_time_encode
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

## system_time_send
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

## ping_encode
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

## ping_send
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

## change_operator_control_encode
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

## change_operator_control_send
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

## change_operator_control_ack_encode
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

## change_operator_control_ack_send
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

## auth_key_encode
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

## auth_key_send
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

## set_mode_encode
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

## set_mode_send
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

## param_request_read_encode
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

## param_request_read_send
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

## param_request_list_encode
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

## param_request_list_send
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

## param_value_encode
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

## param_value_send
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

## param_set_encode
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

## param_set_send
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

## gps_raw_int_encode
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

## gps_raw_int_send
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

## gps_status_encode
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

## gps_status_send
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

## scaled_imu_encode
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

## scaled_imu_send
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

## raw_imu_encode
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

## raw_imu_send
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

## raw_pressure_encode
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

## raw_pressure_send
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

## scaled_pressure_encode
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

## scaled_pressure_send
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

## attitude_encode
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

## attitude_send
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

## attitude_quaternion_encode
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

## attitude_quaternion_send
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

## local_position_ned_encode
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

## local_position_ned_send
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

## global_position_int_encode
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

## global_position_int_send
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

## rc_channels_scaled_encode
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

## rc_channels_scaled_send
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

## rc_channels_raw_encode
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

## rc_channels_raw_send
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

## servo_output_raw_encode
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

## servo_output_raw_send
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

## mission_request_partial_list_encode
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

## mission_request_partial_list_send
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

## mission_write_partial_list_encode
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

## mission_write_partial_list_send
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

## mission_item_encode
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

## mission_item_send
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

## mission_request_encode
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

## mission_request_send
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

## mission_set_current_encode
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

## mission_set_current_send
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

## mission_current_encode
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

## mission_current_send
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

## mission_request_list_encode
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

## mission_request_list_send
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

## mission_count_encode
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

## mission_count_send
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

## mission_clear_all_encode
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

## mission_clear_all_send
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

## mission_item_reached_encode
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

## mission_item_reached_send
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

## mission_ack_encode
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

## mission_ack_send
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

## set_gps_global_origin_encode
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

## set_gps_global_origin_send
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

## gps_global_origin_encode
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

## gps_global_origin_send
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

## param_map_rc_encode
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

## param_map_rc_send
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

## mission_request_int_encode
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

## mission_request_int_send
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

## safety_set_allowed_area_encode
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

## safety_set_allowed_area_send
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

## safety_allowed_area_encode
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

## safety_allowed_area_send
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

## attitude_quaternion_cov_encode
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

## attitude_quaternion_cov_send
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

## nav_controller_output_encode
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

## nav_controller_output_send
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

## global_position_int_cov_encode
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

## global_position_int_cov_send
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

## local_position_ned_cov_encode
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

## local_position_ned_cov_send
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

## rc_channels_encode
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

## rc_channels_send
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

## request_data_stream_encode
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

## request_data_stream_send
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

## data_stream_encode
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

## data_stream_send
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

## manual_control_encode
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

## manual_control_send
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

## rc_channels_override_encode
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

## rc_channels_override_send
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

## mission_item_int_encode
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

## mission_item_int_send
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

## vfr_hud_encode
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

## vfr_hud_send
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

## command_int_encode
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

## command_int_send
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

## command_long_encode
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

## command_long_send
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

## command_ack_encode
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

## command_ack_send
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

## manual_setpoint_encode
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

## manual_setpoint_send
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

## set_attitude_target_encode
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

## set_attitude_target_send
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

## attitude_target_encode
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

## attitude_target_send
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

## set_position_target_local_ned_encode
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

## set_position_target_local_ned_send
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

## position_target_local_ned_encode
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

## position_target_local_ned_send
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

## set_position_target_global_int_encode
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

## set_position_target_global_int_send
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

## position_target_global_int_encode
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

## position_target_global_int_send
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

## local_position_ned_system_global_offset_encode
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

## local_position_ned_system_global_offset_send
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

## hil_state_encode
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

## hil_state_send
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

## hil_controls_encode
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

## hil_controls_send
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

## hil_rc_inputs_raw_encode
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

## hil_rc_inputs_raw_send
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

## hil_actuator_controls_encode
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

## hil_actuator_controls_send
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

## optical_flow_encode
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

## optical_flow_send
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

## global_vision_position_estimate_encode
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

## global_vision_position_estimate_send
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

## vision_position_estimate_encode
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

## vision_position_estimate_send
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

## vision_speed_estimate_encode
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

## vision_speed_estimate_send
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

## vicon_position_estimate_encode
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

## vicon_position_estimate_send
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

## highres_imu_encode
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

## highres_imu_send
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

## optical_flow_rad_encode
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

## optical_flow_rad_send
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

## hil_sensor_encode
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

## hil_sensor_send
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

## sim_state_encode
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

## sim_state_send
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

## radio_status_encode
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

## radio_status_send
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

## file_transfer_protocol_encode
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

## file_transfer_protocol_send
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

## timesync_encode
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

## timesync_send
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

## camera_trigger_encode
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

## camera_trigger_send
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

## hil_gps_encode
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

## hil_gps_send
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

## hil_optical_flow_encode
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

## hil_optical_flow_send
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

## hil_state_quaternion_encode
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

## hil_state_quaternion_send
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

## scaled_imu2_encode
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

## scaled_imu2_send
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

## log_request_list_encode
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

## log_request_list_send
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

## log_entry_encode
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

## log_entry_send
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

## log_request_data_encode
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

## log_request_data_send
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

## log_data_encode
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

## log_data_send
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

## log_erase_encode
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

## log_erase_send
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

## log_request_end_encode
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

## log_request_end_send
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

## gps_inject_data_encode
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

## gps_inject_data_send
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

## gps2_raw_encode
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

## gps2_raw_send
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

## power_status_encode
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

## power_status_send
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

## serial_control_encode
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

## serial_control_send
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

## gps_rtk_encode
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

## gps_rtk_send
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

## gps2_rtk_encode
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

## gps2_rtk_send
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

## scaled_imu3_encode
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

## scaled_imu3_send
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

## data_transmission_handshake_encode
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

## data_transmission_handshake_send
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

## encapsulated_data_encode
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

## encapsulated_data_send
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

## distance_sensor_encode
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

## distance_sensor_send
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

## terrain_request_encode
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

## terrain_request_send
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

## terrain_data_encode
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

## terrain_data_send
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

## terrain_check_encode
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

## terrain_check_send
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

## terrain_report_encode
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

## terrain_report_send
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

## scaled_pressure2_encode
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

## scaled_pressure2_send
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

## att_pos_mocap_encode
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

## att_pos_mocap_send
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

## set_actuator_control_target_encode
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

## set_actuator_control_target_send
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

## actuator_control_target_encode
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

## actuator_control_target_send
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

## altitude_encode
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

## altitude_send
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

## resource_request_encode
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

## resource_request_send
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

## scaled_pressure3_encode
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

## scaled_pressure3_send
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

## follow_target_encode
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

## follow_target_send
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

## control_system_state_encode
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

## control_system_state_send
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

## battery_status_encode
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

## battery_status_send
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

## autopilot_version_encode
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

## autopilot_version_send
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

## landing_target_encode
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

## landing_target_send
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

## fence_status_encode
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

## fence_status_send
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

## mag_cal_report_encode
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

## mag_cal_report_send
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

## efi_status_encode
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

## efi_status_send
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

## estimator_status_encode
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

## estimator_status_send
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

## wind_cov_encode
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

## wind_cov_send
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

## gps_input_encode
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

## gps_input_send
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

## gps_rtcm_data_encode
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

## gps_rtcm_data_send
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

## high_latency_encode
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

## high_latency_send
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

## high_latency2_encode
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

## high_latency2_send
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

## vibration_encode
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

## vibration_send
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

## home_position_encode
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

## home_position_send
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

## set_home_position_encode
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

## set_home_position_send
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

## message_interval_encode
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

## message_interval_send
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

## extended_sys_state_encode
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

## extended_sys_state_send
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

## adsb_vehicle_encode
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

## adsb_vehicle_send
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

## collision_encode
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

## collision_send
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

## v2_extension_encode
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

## v2_extension_send
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

## memory_vect_encode
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

## memory_vect_send
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

## debug_vect_encode
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

## debug_vect_send
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

## named_value_float_encode
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

## named_value_float_send
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

## named_value_int_encode
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

## named_value_int_send
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

## statustext_encode
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

## debug_send
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

## setup_signing_encode
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

## setup_signing_send
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

## button_change_encode
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

## button_change_send
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

## play_tune_encode
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

## play_tune_send
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

## camera_information_encode
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

## camera_information_send
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

## camera_settings_encode
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

## camera_settings_send
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

## storage_information_encode
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

## storage_information_send
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

## camera_capture_status_encode
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

## camera_capture_status_send
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

## camera_image_captured_encode
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

## camera_image_captured_send
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

## flight_information_encode
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

## flight_information_send
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

## mount_orientation_encode
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

## mount_orientation_send
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

## logging_data_encode
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

## logging_data_send
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

## logging_data_acked_encode
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

## logging_data_acked_send
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

## logging_ack_encode
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

## logging_ack_send
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

## video_stream_information_encode
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

## video_stream_information_send
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

## video_stream_status_encode
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

## video_stream_status_send
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

## camera_fov_status_encode
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

## camera_fov_status_send
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

## camera_tracking_image_status_encode
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

## camera_tracking_image_status_send
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

## camera_tracking_geo_status_encode
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

## camera_tracking_geo_status_send
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

## camera_thermal_range_encode
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

## camera_thermal_range_send
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

## gimbal_manager_information_encode
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

## gimbal_manager_information_send
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

## gimbal_manager_status_encode
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

## gimbal_manager_status_send
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

## gimbal_manager_set_attitude_encode
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

## gimbal_manager_set_attitude_send
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

## gimbal_device_information_encode
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

## gimbal_device_information_send
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

## gimbal_device_set_attitude_encode
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

## gimbal_device_set_attitude_send
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

## gimbal_device_attitude_status_encode
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

## gimbal_device_attitude_status_send
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

## autopilot_state_for_gimbal_device_encode
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

## autopilot_state_for_gimbal_device_send
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

## gimbal_manager_set_pitchyaw_encode
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

## gimbal_manager_set_pitchyaw_send
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

## gimbal_manager_set_manual_control_encode
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

## gimbal_manager_set_manual_control_send
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

## wifi_config_ap_encode
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

## wifi_config_ap_send
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

## ais_vessel_encode
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

## ais_vessel_send
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

## uavcan_node_status_encode
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

## uavcan_node_status_send
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

## uavcan_node_info_encode
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

## uavcan_node_info_send
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

## param_ext_request_read_encode
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

## param_ext_request_read_send
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

## param_ext_request_list_encode
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

## param_ext_request_list_send
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

## param_ext_value_encode
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

## param_ext_value_send
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

## param_ext_set_encode
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

## param_ext_set_send
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

## param_ext_ack_encode
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

## param_ext_ack_send
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

## obstacle_distance_encode
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

## obstacle_distance_send
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

## odometry_encode
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

## odometry_send
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

## trajectory_representation_waypoints_encode
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

## trajectory_representation_waypoints_send
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

## trajectory_representation_bezier_encode
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

## trajectory_representation_bezier_send
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

## isbd_link_status_encode
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

## isbd_link_status_send
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

## raw_rpm_encode
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

## raw_rpm_send
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

## utm_global_position_encode
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

## utm_global_position_send
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

## debug_float_array_encode
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

## debug_float_array_send
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

## smart_battery_info_encode
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

## smart_battery_info_send
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

## generator_status_encode
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

## generator_status_send
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

## actuator_output_status_encode
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

## actuator_output_status_send
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

## relay_status_encode
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

## relay_status_send
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

## tunnel_encode
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

## tunnel_send
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

## can_frame_encode
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

## can_frame_send
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

## canfd_frame_encode
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

## canfd_frame_send
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

## can_filter_modify_encode
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

## can_filter_modify_send
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

## wheel_distance_encode
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

## wheel_distance_send
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

## winch_status_encode
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

## winch_status_send
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

## open_drone_id_basic_id_encode
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

## open_drone_id_basic_id_send
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

## open_drone_id_location_encode
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

## open_drone_id_location_send
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

## open_drone_id_authentication_encode
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

## open_drone_id_authentication_send
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

## open_drone_id_self_id_encode
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

## open_drone_id_self_id_send
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

## open_drone_id_system_encode
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

## open_drone_id_system_send
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

## open_drone_id_operator_id_encode
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

## open_drone_id_operator_id_send
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

## open_drone_id_arm_status_encode
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

## open_drone_id_arm_status_send
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

## open_drone_id_message_pack_encode
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

## open_drone_id_message_pack_send
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

## open_drone_id_system_update_encode
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

## open_drone_id_system_update_send
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

## hygrometer_sensor_encode
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

## hygrometer_sensor_send
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

## uavionix_adsb_out_cfg_encode
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

## uavionix_adsb_out_cfg_send
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

## uavionix_adsb_out_dynamic_encode
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

## uavionix_adsb_out_dynamic_send
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

## uavionix_adsb_transceiver_health_report_encode
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

## uavionix_adsb_transceiver_health_report_send
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

## uavionix_adsb_out_cfg_registration_encode
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

## uavionix_adsb_out_cfg_registration_send
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

## uavionix_adsb_out_cfg_flightid_encode
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

## uavionix_adsb_out_cfg_flightid_send
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

## uavionix_adsb_get_encode
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

## uavionix_adsb_get_send
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

## uavionix_adsb_out_control_encode
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

## uavionix_adsb_out_control_send
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

## uavionix_adsb_out_status_encode
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

## uavionix_adsb_out_status_send
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

## icarous_heartbeat_encode
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

## icarous_heartbeat_send
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

## icarous_kinematic_bands_encode
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

## icarous_kinematic_bands_send
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

## loweheiser_gov_efi_encode
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

## loweheiser_gov_efi_send
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

## cubepilot_raw_rc_encode
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

## cubepilot_raw_rc_send
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

## herelink_video_stream_information_encode
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

## herelink_video_stream_information_send
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

## herelink_telem_encode
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

## herelink_telem_send
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

## cubepilot_firmware_update_start_encode
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

## cubepilot_firmware_update_start_send
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

## cubepilot_firmware_update_resp_encode
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

## cubepilot_firmware_update_resp_send
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

## airlink_auth_encode
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

## airlink_auth_send
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

## airlink_auth_response_encode
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

## airlink_auth_response_send
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

## heartbeat_encode
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

## heartbeat_send
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

## __dict__
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

## __weakref__
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

## __new__
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

## __repr__
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

## __hash__
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

## __str__
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

## __getattribute__
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

## __setattr__
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

## __delattr__
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

## __lt__
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

## __le__
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

## __eq__
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

## __ne__
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

## __gt__
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

## __ge__
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

## __reduce_ex__
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

## __reduce__
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

## __getstate__
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

## __subclasshook__
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

## __init_subclass__
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

## __format__
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

## __sizeof__
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

## __dir__
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

## __class__
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

