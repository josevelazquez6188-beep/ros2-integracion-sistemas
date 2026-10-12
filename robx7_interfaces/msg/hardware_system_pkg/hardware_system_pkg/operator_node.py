
import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


class OperatorNode(Node):
    def __init__(self):
        super().__init__('operator_node')

        self.client = self.create_client(
            Trigger,
            '/check_system'
        )

        self.waiting = False
        self.timer = self.create_timer(
            3.0,
            self.check_status
        )

    def check_status(self):
        if self.waiting:
            return

        if not self.client.service_is_ready():
            self.get_logger().info('Esperando al Monitor...')
            return

        self.waiting = True
        future = self.client.call_async(Trigger.Request())
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        self.waiting = False

        try:
            response = future.result()

            if response.success:
                self.get_logger().info(response.message)
            else:
                self.get_logger().warning(response.message)

        except Exception as error:
            self.get_logger().error(f'Error: {error}')


def main(args=None):
    rclpy.init(args=args)
    node = OperatorNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
