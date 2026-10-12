
import rclpy
from rclpy.node import Node
from robx7_interfaces.msg import HardwareStatus
from std_srvs.srv import Trigger


class MonitorNode(Node):
    def __init__(self):
        super().__init__('monitor_node')

        self.declare_parameter('umbral_temperatura', 50)
        self.umbral = self.get_parameter(
            'umbral_temperatura'
        ).value

        self.temperatura = None
        self.motores_listos = False

        self.subscription = self.create_subscription(
            HardwareStatus,
            '/hardware_status',
            self.callback_status,
            10
        )

        self.service = self.create_service(
            Trigger,
            '/check_system',
            self.check_system
        )

        self.get_logger().info(
            f'Monitor iniciado. Umbral: {self.umbral}'
        )

    def callback_status(self, msg):
        self.temperatura = msg.temperatura
        self.motores_listos = msg.motores_listos

        if msg.temperatura > self.umbral:
            self.get_logger().warning(
                f'Temperatura alta: {msg.temperatura}'
            )

    def check_system(self, request, response):
        if self.temperatura is None:
            response.success = False
            response.message = 'Sin datos del hardware'
        elif (
            self.temperatura <= self.umbral
            and self.motores_listos
        ):
            response.success = True
            response.message = 'Autorizacion de movimiento concedida'
        else:
            response.success = False
            response.message = (
                'Bloqueo por temperatura alta '
                'o motores no listos'
            )

        return response


def main(args=None):
    rclpy.init(args=args)
    node = MonitorNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
