
import rclpy
from rclpy.node import Node
from robx7_interfaces.msg import HardwareStatus


class HardwareEmulator(Node):
    def __init__(self):
        super().__init__('hardware_emulator')

        self.publisher = self.create_publisher(
            HardwareStatus,
            '/hardware_status',
            10
        )

        self.counter = 0
        self.timer = self.create_timer(1.0, self.publish_status)

    def publish_status(self):
        msg = HardwareStatus()

        # Simular cambios de temperatura.
        msg.temperatura = 35 + (self.counter % 56)
        msg.motores_listos = msg.temperatura < 80

        if msg.temperatura >= 80:
            msg.debug_msg = 'Fallo de sensor'
        elif msg.temperatura >= 60:
            msg.debug_msg = 'Calentando'
        else:
            msg.debug_msg = 'Operacion normal'

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Temperatura: {msg.temperatura} | '
            f'Motores listos: {msg.motores_listos} | '
            f'{msg.debug_msg}'
        )

        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = HardwareEmulator()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
